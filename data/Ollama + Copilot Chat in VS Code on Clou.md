Ollama + Copilot Chat in VS Code on Cloud Run: A DevOps Cookbook
This cookbook provides a step-by-step guide for deploying a solution that embeds a local Large Language Model (Ollama with Llama3) alongside GitHub Copilot Chat within a VS Code environment, exposed as an HTTP service for external consumption. This setup is designed for Vertex AI practitioners looking to leverage local LLMs and Copilot's capabilities in a custom, accessible manner.

Infra
The core infrastructure will involve a Docker container running on Google Cloud Run. Cloud Run offers a fully managed compute platform that automatically scales with your traffic, making it ideal for this kind of stateless or near-stateless service.

Docker
The Dockerfile sets up an Ubuntu base image, installs code-server (VS Code in a browser), configures necessary extensions, installs Ollama, pulls the Llama3 model, and prepares the environment for our bridging service.

Dockerfile

# Use a recent Ubuntu image
FROM ubuntu:24.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV OLLAMA_HOST=0.0.0.0:11434
ENV OLLAMA_MODELS=/root/.ollama/models

# Install dependencies
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    gnupg \
    procps \
    git \
    nodejs \
    npm \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install code-server (VS Code in a browser)
RUN curl -fsSL https://code-server.dev/install.sh | sh

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Install VS Code extensions
# Note: GitHub Copilot Chat requires a valid GitHub Copilot subscription.
# The `ms-vscs-remote.vscode-remote-containers` extension might not be strictly
# necessary for this setup as we're running everything in one container,
# but it's often useful in dev workflows.
RUN code-server --install-extension GitHub.copilot \
    --install-extension GitHub.copilot-chat \
    --install-extension continue.continue

# Pull the Llama3:8b model for Ollama
RUN ollama pull llama3:8b

# Create a directory for our Node.js service
RUN mkdir /app
WORKDIR /app

# Copy package.json and package-lock.json first to leverage Docker cache
COPY package*.json ./

# Install Node.js dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose ports
EXPOSE 8080 # For the Node.js bridge service
EXPOSE 11434 # For Ollama API

# Start Ollama in the background
CMD bash -c "ollama serve & npm start"
Explanation:

ubuntu:24.04: A stable and recent base image.
code-server: Provides VS Code accessible via a web browser.
ollama: The local LLM server.
GitHub.copilot-chat, continue.continue: Essential VS Code extensions for our use case.
ollama pull llama3:8b: Downloads the Llama3 8B parameter model. This will increase the Docker image size.
npm install: Installs Node.js dependencies for our bridge service.
ollama serve & npm start: Starts Ollama in the background and then our Node.js bridge service.
Bridge-Service
This Node.js microservice will act as a bridge, receiving HTTP requests and forwarding them to the Copilot Chat API within the code-server environment using vscode-jsonrpc.

package.json

JSON

{
  "name": "copilot-bridge",
  "version": "1.0.0",
  "description": "Bridges HTTP requests to VS Code Copilot Chat API",
  "main": "index.js",
  "scripts": {
    "start": "node index.js"
  },
  "dependencies": {
    "express": "^4.19.2",
    "node-fetch": "^3.3.2",
    "ws": "^8.17.0"
  }
}
index.js

JavaScript

const express = require('express');
const WebSocket = require('ws');
const { v4: uuidv4 } = require('uuid');
const { TextDecoder, TextEncoder } = require('util');

const app = express();
const port = process.env.PORT || 8080;

app.use(express.json());

// In a real-world scenario, you would need to securely obtain and manage this token.
// For this cookbook, we'll assume it's passed via an environment variable.
const COPILOT_TOKEN = process.env.COPILOT_TOKEN;
if (!COPILOT_TOKEN) {
  console.error("COPILOT_TOKEN environment variable is not set. Copilot Chat will not function.");
  process.exit(1);
}

// Function to interact with Copilot Chat via WebSocket
async function callCopilotChat(prompt) {
    return new Promise((resolve, reject) => {
        // code-server typically runs on port 8080 or 8443 by default.
        // If code-server is running within the same container,
        // it might not expose a direct WebSocket for Copilot.
        // This is a conceptual bridge. A more robust solution would involve
        // a VS Code extension that exposes an endpoint, or directly interacting
        // with the Copilot VS Code extension's internal APIs (which is complex and unsupported).
        // For the purpose of this cookbook, we're simulating a direct interaction
        // with a hypothetical Copilot Chat exposed endpoint.
        // In a real VS Code extension scenario, you'd use VS Code's extension API.

        // THIS IS A SIMPLIFIED MOCK. DIRECTLY ACCESSING COPILOT CHAT API VIA WEBSOCKET
        // FROM OUTSIDE VS CODE IS NOT SUPPORTED WITHOUT A CUSTOM VS CODE EXTENSION EXPOSING IT.
        // A robust solution would involve writing a VS Code extension that exposes
        // a custom command or API endpoint that the bridge service can call
        // using `vscode-jsonrpc` over a named pipe or a custom WebSocket server
        // exposed by the extension itself.

        // Placeholder for a conceptual WebSocket connection to a VS Code extension endpoint
        // that is designed to expose Copilot Chat functionality.
        // In reality, you'd need a custom VS Code extension to make this work securely.
        const ws = new WebSocket(`ws://localhost:8080/copilot-chat-api-bridge`); // Hypothetical endpoint

        ws.onopen = () => {
            console.log('Connected to Copilot Chat bridge WebSocket');
            // Simulate sending a request to the hypothetical Copilot Chat bridge
            const requestId = uuidv4();
            const message = {
                jsonrpc: '2.0',
                id: requestId,
                method: 'chat.sendMessage',
                params: {
                    message: prompt,
                    // You might need to pass the COPILOT_TOKEN or it should be handled internally by the extension
                }
            };
            ws.send(JSON.stringify(message));
        };

        ws.onmessage = (event) => {
            const data = JSON.parse(event.data);
            if (data.id === requestId && data.result) {
                resolve(data.result.response); // Assuming 'response' key holds the chat output
                ws.close();
            } else if (data.error) {
                reject(new Error(data.error.message));
                ws.close();
            }
        };

        ws.onerror = (error) => {
            console.error('WebSocket error:', error);
            reject(error);
        };

        ws.onclose = () => {
            console.log('Copilot Chat bridge WebSocket closed');
        };
    });
}

// Endpoint to interact with Copilot Chat
app.post('/copilot-chat', async (req, res) => {
    const { prompt } = req.body;
    if (!prompt) {
        return res.status(400).json({ error: 'Prompt is required.' });
    }

    try {
        const response = await callCopilotChat(prompt);
        res.json({ response });
    } catch (error) {
        console.error('Error calling Copilot Chat:', error);
        res.status(500).json({ error: 'Failed to get response from Copilot Chat.' });
    }
});

// Endpoint to interact with Ollama
app.post('/ollama-chat', async (req, res) => {
    const { prompt, model = 'llama3:8b' } = req.body;
    if (!prompt) {
        return res.status(400).json({ error: 'Prompt is required.' });
    }

    try {
        const ollamaResponse = await fetch(`http://localhost:11434/api/generate`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                model: model,
                prompt: prompt,
                stream: false // For simple request/response
            }),
        });

        if (!ollamaResponse.ok) {
            const errorText = await ollamaResponse.text();
            throw new Error(`Ollama API error: ${ollamaResponse.status} - ${errorText}`);
        }

        const data = await ollamaResponse.json();
        res.json({ response: data.response });
    } catch (error) {
        console.error('Error calling Ollama:', error);
        res.status(500).json({ error: 'Failed to get response from Ollama.' });
    }
});

// Basic health check endpoint
app.get('/healthz', (req, res) => {
    res.status(200).send('OK');
});

app.listen(port, () => {
    console.log(`Bridge service listening at http://localhost:${port}`);
});
Important Considerations for the Bridge Service:

Copilot Chat API Access: Directly accessing GitHub Copilot Chat's internal API from an external Node.js service is not officially supported and is highly complex. The provided callCopilotChat function is a conceptual placeholder. A robust solution would require:
Custom VS Code Extension: Develop a VS Code extension that hosts a local HTTP or WebSocket server. This extension would then use the vscode.commands.executeCommand or vscode.window.createChatAgent APIs to interact with Copilot Chat, and expose the responses to your bridge service.
vscode-jsonrpc: The vscode-jsonrpc library is typically used for communication between VS Code and language servers (or extensions) over a stream (like a named pipe or WebSocket). You'd use this within a VS Code extension to communicate with your external service, or if your extension itself exposes a JSON-RPC endpoint.
Security: Exposing Copilot Chat directly as an HTTP service requires careful consideration of authentication and authorization. The COPILOT_TOKEN should be handled securely.
Ollama API: Interacting with Ollama is straightforward as it provides a standard HTTP API.
Secrets
The GitHub Copilot token (COPILOT_TOKEN) is a sensitive credential and must be managed securely. Google Cloud Secret Manager is the ideal service for this.

Create a Secret in Secret Manager:

Bash

gcloud secrets create COPILOT_TOKEN --replication-policy="automatic"
Add the Secret Value:

Bash

echo "YOUR_GITHUB_COPILOT_TOKEN" | gcloud secrets versions add COPILOT_TOKEN --data-file=-
Replace "YOUR_GITHUB_COPILOT_TOKEN" with your actual Copilot token.

Grant Cloud Run Service Account Access:
Your Cloud Run service account needs permission to access the secret.

Bash

# Get your Cloud Run service account email
PROJECT_ID=$(gcloud config get-value project)
SERVICE_ACCOUNT=$(gcloud run services describe YOUR_SERVICE_NAME --region YOUR_REGION --format='value(spec.template.spec.serviceAccountName)' || echo "service-${PROJECT_ID}@gcp-sa-cloudrun.iam.gserviceaccount.com")

# Grant secret accessor role
gcloud secrets add-iam-policy-binding COPILOT_TOKEN \
  --member="serviceAccount:${SERVICE_ACCOUNT}" \
  --role="roles/secretmanager.secretAccessor"
Replace YOUR_SERVICE_NAME and YOUR_REGION with your Cloud Run service's name and region.

Reference the Secret in Cloud Run Deployment:
When deploying your Cloud Run service, you'll configure it to inject the secret as an environment variable.

Bash

gcloud run deploy YOUR_SERVICE_NAME \
  --image gcr.io/${PROJECT_ID}/ollama-copilot-bridge \
  --platform managed \
  --region YOUR_REGION \
  --allow-unauthenticated \
  --memory 4Gi \
  --cpu 2 \
  --set-env-vars=COPILOT_TOKEN=projects/${PROJECT_ID}/secrets/COPILOT_TOKEN/versions/latest
This command deploys the service, allocates 4GB of memory and 2 CPUs (required for Llama3:8b), and sets the COPILOT_TOKEN environment variable from Secret Manager.

Benchmarks
Benchmarking a combined Ollama and Copilot Chat service on Cloud Run involves considering both the local LLM (Ollama) and the potential overhead of the Copilot bridge. These are estimates and will vary based on prompt complexity and actual usage.

Assumptions for Cloud Run (e2-medium, 2 vCPU, 4GB RAM):

Ollama (Llama3:8b):
RAM: Llama3:8b typically requires around 4.7 GB of RAM for inference with default settings (or less if quantized). Running ollama serve and loading the model will consume a significant portion of the allocated 4GB. This is why 4GB is recommended as the minimum for the Cloud Run instance.
Tokens/s: On a 2 vCPU environment, you might expect anywhere from 10-30 tokens/second for Llama3:8b, depending on the specific CPU architecture and I/O.
Copilot Chat Bridge:
RAM: Minimal (Node.js microservice footprint, few hundred MB).
Tokens/s: Dependent on GitHub Copilot's backend performance, not directly measurable from your container as it's an external API call. The latency would be dominated by the Copilot API response time.
Overall Cost (e2-medium, 2 vCPU, 4GB RAM on Cloud Run):
CPU: $0.06 - $0.12 per vCPU-hour (variable pricing based on usage).
Memory: $0.006 - $0.012 per GB-hour (variable pricing based on usage).
Invocations: First 2 million invocations per month are free.
Networking: Standard Cloud Run egress costs.
Benchmark Table (Estimated for e2-medium, 2 vCPU, 4GB RAM):

Metric	Ollama (Llama3:8b)	Copilot Chat (via Bridge)	Combined Service (Idle)
Tokens/s (approx.)	10-30 (for Llama3:8b generation)	N/A (external service)	N/A
RAM Usage	~4.7 GB (for Llama3:8b model load)	&lt; 500 MB (Node.js runtime)	~5.2 GB (Peak)
Cost (per hour)	~$0.06 - $0.12 (CPU) + ~$0.04 (RAM)	Minimal (invocation cost only)	~$0.10 - $0.16
Latency	Dependent on prompt length	Dependent on Copilot API response	Sum of both

Eksportuj do Arkuszy
Note on RAM: The 4GB RAM limit on Cloud Run for e2-medium instances will be a tight fit for Llama3:8b. You might experience out-of-memory errors if other processes consume too much memory or if the model itself requires slightly more. Consider increasing the memory allocation on Cloud Run to 8GB (e2-highmem-4) for more stability, which will increase the cost.

n8n Flow
This n8n workflow demonstrates how to trigger our deployed service using a webhook, send a prompt, and then respond to the webhook.

JSON

{
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "copilot-ollama-bridge",
        "options": {}
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "json": true,
      "notesInMarkdown": false,
      "clipboardData": {
        "notesInMarkdown": false
      }
    },
    {
      "parameters": {
        "url": "YOUR_CLOUD_RUN_SERVICE_URL/copilot-chat",
        "method": "POST",
        "jsonBody": true,
        "bodyParameters": [
          {
            "name": "prompt",
            "value": "={{$json.body.prompt}}"
          }
        ],
        "options": {}
      },
      "name": "HTTP Request (Copilot Chat)",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 1,
      "notesInMarkdown": false,
      "clipboardData": {
        "notesInMarkdown": false
      }
    },
    {
      "parameters": {
        "url": "YOUR_CLOUD_RUN_SERVICE_URL/ollama-chat",
        "method": "POST",
        "jsonBody": true,
        "bodyParameters": [
          {
            "name": "prompt",
            "value": "={{$json.body.prompt}}"
          }
        ],
        "options": {}
      },
      "name": "HTTP Request (Ollama)",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 1,
      "notesInMarkdown": false,
      "clipboardData": {
        "notesInMarkdown": false
      }
    },
    {
      "parameters": {
        "responseMode": "lastNode",
        "options": {}
      },
      "name": "Respond to Webhook (Copilot)",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1,
      "notesInMarkdown": false,
      "clipboardData": {
        "notesInMarkdown": false
      }
    },
    {
      "parameters": {
        "responseMode": "lastNode",
        "options": {}
      },
      "name": "Respond to Webhook (Ollama)",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1,
      "notesInMarkdown": false,
      "clipboardData": {
        "notesInMarkdown": false
      }
    }
  ],
  "connections": {
    "Webhook": [
      [
        "HTTP Request (Copilot Chat)",
        "HTTP Request (Ollama)"
      ]
    ],
    "HTTP Request (Copilot Chat)": [
      [
        "Respond to Webhook (Copilot)"
      ]
    ],
    "HTTP Request (Ollama)": [
      [
        "Respond to Webhook (Ollama)"
      ]
    ]
  ]
}
How to use this n8n Flow:

Import: In your n8n instance, go to "Workflows" and click "New". Then, click the three dots in the top right and select "Import from JSON". Paste the above JSON.
Configure Webhook: Activate the Webhook node. Copy the generated webhook URL.
Configure HTTP Request Nodes: Replace YOUR_CLOUD_RUN_SERVICE_URL with the actual URL of your deployed Cloud Run service.
Test: Send a POST request to your n8n webhook URL with a JSON body like:
JSON

{
  "prompt": "Explain DevOps in one sentence."
}
You can then check the execution results in n8n to see the responses from either Copilot Chat or Ollama.
Next Steps
Refine Copilot Chat Integration: As highlighted, the direct integration with Copilot Chat in the bridge service is a simplification. The most robust and supported approach involves developing a custom VS Code extension that exposes the Copilot Chat functionality via a local API that your Node.js service can consume securely.
Authentication/Authorization: Implement proper authentication and authorization for your Cloud Run service to prevent unauthorized access. This could involve API keys, OAuth2, or Google-managed identity.
Error Handling and Logging: Enhance the Node.js bridge service with more comprehensive error handling and structured logging for better observability.
Persistent Storage (for Ollama models): If you anticipate frequent updates or different Ollama models, consider using a persistent volume (e.g., Cloud Storage FUSE) with Cloud Run to store models, avoiding repeated downloads during container startup. However, this adds complexity and might impact cold start times. For a single, static model like Llama3:8b, embedding it in the Docker image is simpler.
Monitoring and Alerting: Set up Cloud Monitoring and Cloud Logging for your Cloud Run service to monitor performance, resource usage, and receive alerts on potential issues.
Cost Optimization: Monitor your Cloud Run costs closely. If the service is idle for long periods, consider adjusting the minimum instances to zero or using a more granular scaling strategy. If Llama3:8b proves too resource-intensive, explore smaller or more optimized models.
Citations:

Cloud Run Pricing: https://cloud.google.com/run/pricing (Accessed 2025-06-18)
Ollama GitHub Repository: https://github.com/ollama/ollama (Accessed 2025-06-18)
code-server Documentation: https://code.visualstudio.com/docs/remote/codespaces#_connect-to-a-codespace-from-your-local-machine (Accessed 2025-06-18)
Google Cloud Secret Manager: https://cloud.google.com/secret-manager (Accessed 2025-06-18)
n8n Documentation: https://docs.n8n.io/ (Accessed 2025-06-18)

 Źródła
