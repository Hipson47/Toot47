<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

# VS Code AI Coding Assistants: Definitive Guide (June 2025)

## 1. Extension APIs for External Calls

### Copilot Chat

- VS Code extension API enables Copilot Chat to communicate via Language Model API for AI-powered features [^1_1][^1_2] - 5
- Copilot Chat uses WebSocket connections for real-time communication with GitHub's backend services [^1_2] - 4
- Authentication tokens stored securely using VS Code's SecretStorage API for persistent sessions [^1_2][^1_3] - 5
- Official documentation: https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-chat-in-your-ide [^1_2] - 5


### Continue

- Continue.dev uses REST API endpoints to communicate with local LLM servers like Ollama [^1_4][^1_5] - 4
- Server facilitates communication between IDE and GUI through standardized API calls [^1_4] - 4
- Steps can be recursively composed into complex workflows via the SDK [^1_4] - 5
- Official documentation: https://continue.dev/docs/how-continue-works [^1_4] - 5


### Codeium

- Codeium extension connects to backend via REST API with configurable endpoint settings [^1_6] - 3
- Authentication handled through access token stored in credentials manager [^1_6][^1_3] - 4
- Extension provides real-time code suggestions through WebSocket connections [^1_6] - 3
- Official documentation: https://www.restack.io/p/ai-enhanced-ides-codeium-answer-vscode-integration-cat-ai [^1_6] - 4


## 2. Steps to Run Local LLM in VS Code

### Installation

- Install Ollama with `curl https://ollama.ai/install.sh | sh` or download from ollama.ai [^1_5][^1_7] - 5
- Start Ollama server with `ollama serve` command to expose port 11434 [^1_5][^1_7] - 5
- Install VS Code extension like Continue.dev, VSCode Ollama, or Llama Coder [^1_5][^1_8] - 5
- Official documentation: https://ollama.ai [^1_5][^1_7] - 5


### Model Management

- List available models with `ollama list` or via Python API `requests.get("http://localhost:11434/api/tags")` [^1_9][^1_10] - 5
- Pull models with `ollama pull <model-name>` (e.g., `ollama pull llama3:8b` or `ollama pull phi3-mini:4k`) [^1_5][^1_7] - 5
- Configure model parameters in extension settings or via Modelfile for custom models [^1_5][^1_7] - 4
- Official documentation: https://github.com/ollama/ollama/blob/main/docs/api.md [^1_5][^1_9] - 5


### RAM Requirements

- Llama-3 8B requires approximately 6GB VRAM with 4-bit quantization [^1_11][^1_12] - 5
- Phi-3 Mini requires approximately 2GB VRAM with 4-bit quantization [^1_11][^1_13] - 5
- Context length significantly impacts memory usage; 30K context with Phi-3 Mini uses ~17GB combined RAM+VRAM [^1_12] - 4
- Official benchmarks: https://huggingface.co/Mozilla/LocalScore [^1_11] - 4


## 3. Security

### Keytar Storage

- VS Code 1.80+ replaced deprecated keytar with Electron's safeStorage API for secrets [^1_14] - 5
- SecretStorage API stores tokens in OS-specific secure storage (Windows Credential Manager, macOS Keychain, Linux keyring) [^1_3][^1_14] - 5
- Security vulnerability exists where malicious extensions can access other extensions' tokens [^1_3][^1_15] - 5
- Official documentation: https://github.com/microsoft/vscode/issues/185677 [^1_16] - 4


### GCP Secret Manager Integration

- Cloud Code extension provides direct integration with GCP Secret Manager [^1_17][^1_18] - 5
- Create, view, update secrets directly in VS Code without storing in codebase [^1_17][^1_18] - 5
- Access secrets programmatically in your code with proper authentication [^1_17][^1_18] - 5
- Official documentation: https://cloud.google.com/code/docs/vscode/secret-manager [^1_17] - 5


### Best Practices

- Validate extension permissions before installation to prevent token theft [^1_3][^1_19] - 5
- Use environment variables for sensitive data instead of hardcoding [^1_19][^1_20] - 4
- Implement proper authentication and authorization mechanisms in custom extensions [^1_19] - 4
- Official security guidelines: https://code.visualstudio.com/docs/devcontainers/create-dev-container [^1_21] - 3


## 4. Headless VS Code (code-server / web) + AI Plugins

### Deployment Options

- VS Code Server provides headless service accessible through browser or local client [^1_22][^1_23] - 5
- code-server enables browser-based access to VS Code with extension support [^1_23][^1_24] - 5
- GitHub Copilot and other AI extensions work in headless mode with proper authentication [^1_25][^1_26] - 4
- Official documentation: https://code.visualstudio.com/docs/remote/vscode-server [^1_22] - 5


### AI Plugin Compatibility

- GitHub Copilot Chat works in code-server with official VS Code Server binary [^1_25] - 4
- Continue.dev supports headless mode for asynchronous workflows [^1_4] - 3
- AI extensions requiring local GPU access may need special configuration in headless mode [^1_27][^1_28] - 3
- Official documentation: https://code.visualstudio.com/docs/copilot/copilot-extensibility-overview [^1_27] - 4


### Cloud Run Costs

- Cloud Run pricing based on vCPU, memory usage, and request count [^1_29] - 5
- 1 vCPU/512MB instance handling 10M requests/month costs approximately \$3.20 after free tier [^1_29] - 5
- AI-enhanced workloads require more resources: 2 vCPU/4GB recommended at ~\$33.32/month [^1_29] - 4
- Official pricing: https://cloud.google.com/run/pricing [^1_29] - 5


## 5. Devcontainer / Dockerfile to Pre-install Extensions + Ollama

### Dockerfile Configuration

- Create Dockerfile based on debian/ubuntu with `curl https://ollama.ai/install.sh | sh` to install Ollama [^1_30][^1_31] - 5
- Pre-pull models with `RUN ollama pull <model-name>` after starting Ollama service [^1_30][^1_31] - 4
- Expose port 11434 with `EXPOSE 11434` for Ollama API access [^1_30][^1_32] - 5
- Example repository: https://github.com/MandalAutomations/Ollama-Devcontainer [^1_31] - 4


### Devcontainer.json Setup

- Configure `devcontainer.json` with `"features": { "ghcr.io/prulloac/devcontainer-features/ollama:1": {} }` [^1_33] - 5
- Add `"postStartCommand": "ollama serve"` to automatically start Ollama service [^1_34][^1_33] - 5
- Include VS Code extensions like `"extensions": ["ms-toolsai.ai-tools", "10nates.ollama-autocoder"]` [^1_33] - 4
- Official documentation: https://code.visualstudio.com/docs/devcontainers/create-dev-container [^1_21] - 5


### Network Configuration

- Use `"forwardPorts": [^1_11434]` to expose Ollama API port to host [^1_35] - 5
- For Docker Compose, configure network settings to allow inter-container communication [^1_31][^1_35] - 4
- Access Ollama from host with `http://host.docker.internal:11434` in Windows/macOS environments [^1_35] - 5
- Docker Hub image: https://hub.docker.com/r/ollama/ollama [^1_32] - 5


## 6. Resource Benchmarks: Llama-3 8B vs Phi-3 Mini

### Performance (tokens/s)

- Llama-3 8B achieves ~12-15 tokens/second on consumer GPUs, ~5-8 tokens/second on CPU [^1_36][^1_11] - 4
- Phi-3 Mini delivers ~20-25 tokens/second on GPUs, ~12 tokens/second on CPU [^1_36][^1_13] - 4
- Phi-3 Mini produces over 1100 tokens/second on specialized AI hardware (SambaNova SN40L) [^1_37] - 5
- Official benchmarks: https://myscale.com/blog/llama-3-vs-phi-3-mini-showdown-comparison/ [^1_38] - 3


### Memory Usage

- Llama-3 8B requires ~11GB combined RAM+VRAM at 30K context window [^1_12] - 5
- Phi-3 Mini requires ~17GB combined RAM+VRAM at 30K context window [^1_12] - 5
- Phi-3 Mini can run on smartphones with 4-bit quantization using only ~1.8GB memory [^1_13] - 5
- Memory calculator: https://blog.spheron.network/how-much-gpu-memory-is-required-to-run-a-large-language-model-find-out-here [^1_39] - 4


### Model Capabilities

- Phi-3 Mini (3.8B parameters) outperforms Llama-3 8B on most benchmarks despite smaller size [^1_40][^1_41] - 5
- Llama-3 8B handles longer context more efficiently due to better architecture (GQA) [^1_12] - 4
- Phi-3 Mini excels at structured output generation with fewer errors [^1_42] - 4
- Technical comparison: https://www.linkedin.com/posts/junlinghu_phi-3-mini-outperforms-llama-3-8b-very-impressive-activity-7188624710463623169-Lkev [^1_40] - 3


## 7. Example Workflow: HTTP call from n8n → VS Code → returns generated code or PR diff

### n8n Webhook Setup

- Configure n8n Webhook node to receive HTTP requests with parameters [^1_43][^1_44] - 5
- Set webhook to return custom response with generated content [^1_45][^1_46] - 4
- Use production webhook URL for stable integration after testing [^1_47][^1_48] - 5
- Official documentation: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/ [^1_47] - 5


### VS Code API Integration

- Implement VS Code extension with REST API endpoints using custom handlers [^1_49][^1_50] - 4
- Use `vscode-diff` package to generate PR diffs programmatically [^1_51][^1_52] - 4
- Access GitHub PR data with custom Accept header: `application/vnd.github.v3.diff` [^1_53][^1_54] - 5
- Example extension: https://marketplace.visualstudio.com/items?itemName=mkloubert.vs-rest-api [^1_49] - 4


### Code Generation Workflow

- n8n HTTP Request node sends prompt to VS Code extension endpoint [^1_46][^1_55] - 4
- VS Code extension processes request, generates code using Language Model API [^1_56][^1_57] - 3
- Extension returns generated code or PR diff as HTTP response [^1_49][^1_58] - 3
- Workflow example: **UNKNOWN** - No complete end-to-end example available in current sources - 0

<div style="text-align: center">⁂</div>

[^1_1]: https://code.visualstudio.com/api/references/vscode-api

[^1_2]: https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-chat-in-your-ide

[^1_3]: https://cycode.com/blog/exposing-vscode-secrets/

[^1_4]: https://continue.dev/docs/how-continue-works

[^1_5]: https://gist.github.com/othyn/42e67d7b6116d88d6c9c83e7d84b20c0

[^1_6]: https://www.restack.io/p/ai-enhanced-ides-codeium-answer-vscode-integration-cat-ai

[^1_7]: https://hacktobeer.eu/posts/local-llms/

[^1_8]: https://marketplace.visualstudio.com/items?itemName=warm3snow.vscode-ollama

[^1_9]: https://stackoverflow.com/questions/79372940/how-to-get-a-list-of-models-available-in-ollama-using-langchain

[^1_10]: https://www.cohorte.co/blog/using-ollama-with-python-step-by-step-guide

[^1_11]: https://huggingface.co/Mozilla/LocalScore

[^1_12]: https://www.reddit.com/r/LocalLLaMA/comments/1ei9pz4/phi3_mini_context_takes_too_much_ram_why_to_use_it/

[^1_13]: https://the-decoder.com/microsofts-small-and-efficient-llm-phi-3-beats-metas-llama-3-and-free-chatgpt-in-benchmarks/

[^1_14]: https://stackoverflow.com/questions/76863788/where-are-vs-code-extension-secrets-stored

[^1_15]: https://www.varutra.com/ctp/threatpost/postDetails/Code-Flaw-in-Microsoft-Visual-Studio-Lets-Extensions-to-Collect-Credentials/TXdzeDI3bjc1eVB3d3l6N2w1cTF4Zz09

[^1_16]: https://github.com/microsoft/vscode/issues/185677

[^1_17]: https://cloud.google.com/code/docs/vscode/secret-manager

[^1_18]: https://cloud.google.com/code/docs/vscode/manage-secrets

[^1_19]: https://app.studyraid.com/en/read/8400/231902/security-considerations

[^1_20]: https://blog.gitguardian.com/visual-studio-code-extension/

[^1_21]: https://code.visualstudio.com/docs/devcontainers/create-dev-container

[^1_22]: https://code.visualstudio.com/docs/remote/vscode-server

[^1_23]: https://github.com/cdr/code-server/issues/2105

[^1_24]: https://www.reddit.com/r/vscode/comments/dulsfp/vscode_online_headlessserveronly_environments/

[^1_25]: https://github.com/jordolang/docker-code-server

[^1_26]: https://www.webasha.com/blog/top-visual-studio-code-ai-extensions-to-boost-coding-efficiency

[^1_27]: https://code.visualstudio.com/docs/copilot/copilot-extensibility-overview

[^1_28]: https://javascript.plainenglish.io/ai-powered-frontend-development-vscode-plugins-and-ide-recommendations-984324b076b5?gi=93870ef32a07

[^1_29]: https://cloud.google.com/run/pricing?authuser=4

[^1_30]: https://github.com/jmorganca/ollama/issues/957

[^1_31]: https://github.com/MandalAutomations/Ollama-Devcontainer

[^1_32]: https://hub.docker.com/r/ollama/ollama

[^1_33]: https://www.daytona.io/dotfiles/run-llm-with-ollama-inside-daytona-workspace

[^1_34]: https://www.luisquintanilla.me/posts/install-ollama-vscode-devcontainer

[^1_35]: https://stackoverflow.com/questions/78689283/exposing-11434-port-in-docker-container-to-access-ollama-local-model

[^1_36]: https://arxiv.org/pdf/2411.17712.pdf

[^1_37]: https://arxiv.org/abs/2411.01073

[^1_38]: https://myscale.com/blog/llama-3-vs-phi-3-mini-showdown-comparison/

[^1_39]: https://blog.spheron.network/how-much-gpu-memory-is-required-to-run-a-large-language-model-find-out-here

[^1_40]: https://www.linkedin.com/posts/junlinghu_phi-3-mini-outperforms-llama-3-8b-very-impressive-activity-7188624710463623169-Lkev

[^1_41]: https://mlexplained.blog/2024/04/23/is-phi-3-mini-really-better-than-llama-3-testing-the-limits-of-small-llms-in-real-world-scenarios/

[^1_42]: https://www.reddit.com/r/LocalLLaMA/comments/1cbt78y/how_good_is_phi3mini_for_everyone/

[^1_43]: https://n8n.io/integrations/webhook/

[^1_44]: https://www.youtube.com/watch?v=lK3veuZAg0c

[^1_45]: https://pipedream.com/apps/n8n-io/integrations/http

[^1_46]: https://dev.to/brains_behind_bots/mastering-http-requests-in-n8n-the-key-to-connecting-any-app-automating-anything-gm3

[^1_47]: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/

[^1_48]: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/workflow-development/

[^1_49]: https://marketplace.visualstudio.com/items?itemName=mkloubert.vs-rest-api

[^1_50]: https://marketplace.visualstudio.com/items?itemName=mkloubert.vscode-http-client

[^1_51]: https://www.npmjs.com/package/vscode-diff?activeTab=readme

[^1_52]: https://gist.github.com/coderberry/382a7fad7623214e54da800c73799611

[^1_53]: https://github.com/orgs/community/discussions/24460

[^1_54]: https://github.com/reviewdog/reviewdog/issues/1696

[^1_55]: https://www.youtube.com/watch?v=wEC7cL1vs5s

[^1_56]: https://code.visualstudio.com/api/extension-guides/language-model-tutorial

[^1_57]: https://docs.n8n.io/code/

[^1_58]: https://pipedream.com/apps/http/integrations/n8n-io

[^1_59]: https://doiserbia.nb.rs/Article.aspx?ID=1820-02141700009R

[^1_60]: https://dl.acm.org/doi/10.1145/3731558

[^1_61]: https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ECOOP.2024.6

[^1_62]: https://peerj.com/articles/cs-1677

[^1_63]: https://www.semanticscholar.org/paper/3445a761c6b80249b7959a5162c2eca60ef1d0f6

[^1_64]: https://stackoverflow.com/questions/70096828/make-rest-api-call-from-vs-code-extension

[^1_65]: https://techcommunity.microsoft.com/blog/healthcareandlifesciencesblog/calling-rest-apis-from-the-ide/3145949

[^1_66]: https://marketplace.visualstudio.com/items?itemName=humao.rest-client

[^1_67]: https://qiita.com/alokrawat050/items/6e7de9959912ea145091

[^1_68]: https://github.com/jiaweing/copilot-chat-api

[^1_69]: https://www.semanticscholar.org/paper/b6343928a3896eae7f9d77c0cb8709a50ffaaeb4

[^1_70]: https://arxiv.org/abs/2504.06006

[^1_71]: https://ieeexplore.ieee.org/document/10720939/

[^1_72]: https://arxiv.org/abs/2503.20126

[^1_73]: https://www.semanticscholar.org/paper/cc87b786f97a9d28fe407fbf11ae2270d56fdb0f

[^1_74]: https://www.semanticscholar.org/paper/e505bfe85148928e6486c25b8acbbea80ff3f8b7

[^1_75]: https://ieeexplore.ieee.org/document/10887002/

[^1_76]: https://arxiv.org/abs/2403.10082

[^1_77]: https://www.reddit.com/r/ollama/comments/1ii6duy/how_do_i_connect_vs_code_on_a_client_machine_to/

[^1_78]: https://freshbrewed.science/2025/01/28/codellm.html

[^1_79]: https://www.byteplus.com/en/topic/504673

[^1_80]: https://www.reddit.com/r/LocalLLaMA/comments/1k627e8/ollama_memory_usage_higher_than_it_should_be_with/

[^1_81]: https://ieeexplore.ieee.org/document/9584916/

[^1_82]: https://ijaem.net/issue_dcp/A%20Secured%20Blockchain%20Database%20Management%20Model%20for%20Medical%20Based%20Organization.pdf

[^1_83]: https://link.springer.com/10.1007/s41781-021-00071-1

[^1_84]: http://biorxiv.org/lookup/doi/10.1101/2023.06.20.545769

[^1_85]: https://dl.acm.org/doi/10.1145/3399668

[^1_86]: https://github.com/microsoft/vscode/issues/68738

[^1_87]: https://www.linkedin.com/pulse/exploitation-microsofts-vs-code-flaw-using-malicious-kumaradasa

[^1_88]: https://www.ndss-symposium.org/wp-content/uploads/2024-73-paper.pdf

[^1_89]: https://ieeexplore.ieee.org/document/9647189/

[^1_90]: https://dl.acm.org/doi/10.1145/3713081.3731737

[^1_91]: https://system-informatics.ru/ru/article/330

[^1_92]: https://aipublications.com/ijeec/detail/scalable-ai-model-deployment-and-management-on-serverless-cloud-architecture/

[^1_93]: https://journalwjaets.com/node/624

[^1_94]: https://dl.acm.org/doi/10.1145/3689728

[^1_95]: https://onepetro.org/JPT/article/75/04/8/519949/Comments-AI-Language-Tools-Hit-the-Books-and

[^1_96]: https://code.visualstudio.com/docs/remote/tunnels

[^1_97]: https://www.youtube.com/watch?v=ZoxJcPkjirs

[^1_98]: https://blog.chernukha.io/blog/vscode-devcontainers-gpu

[^1_99]: https://github.com/kwame-mintah/vscode-ollama-local-code-copilot

[^1_100]: https://arxiv.org/abs/2411.11055

[^1_101]: https://arxiv.org/abs/2503.09334

[^1_102]: https://ieeexplore.ieee.org/document/10942340/

[^1_103]: https://arxiv.org/abs/2410.21465

[^1_104]: https://arxiv.org/pdf/2411.05966.pdf

[^1_105]: http://arxiv.org/pdf/2404.14219.pdf

[^1_106]: https://www.datacamp.com/tutorial/matmul-free-comparison-experiment

[^1_107]: https://arxiv.org/abs/2408.08982

[^1_108]: https://f1000research.com/articles/13-708/v1

[^1_109]: https://bmcchem.biomedcentral.com/articles/10.1186/1752-153X-6-2

[^1_110]: https://n8n.io/integrations/webhook/and/http-request-tool/

[^1_111]: https://www.youtube.com/watch?v=IvUYJQkf6sA

[^1_112]: https://www.youtube.com/watch?v=pXSCfpnC1hQ

[^1_113]: https://marketplace.visualstudio.com/items?itemName=AutoDev-CLIAgent.autodev-agent

[^1_114]: http://f1000research.com/posters/4-377

[^1_115]: https://dl.acm.org/doi/10.1145/3196398.3196425

[^1_116]: https://arxiv.org/abs/2312.11567

[^1_117]: https://dl.acm.org/doi/10.1145/3129416.3129429

[^1_118]: https://pubs.acs.org/doi/10.1021/acs.jcim.1c00169

[^1_119]: https://stackoverflow.com/questions/51316233/how-can-i-see-git-diff-on-the-visual-studio-code-side-by-side-file

[^1_120]: https://code.visualstudio.com/blogs/2018/09/10/introducing-github-pullrequests

[^1_121]: https://github.com/jasonnutter/vscode-github-pr

[^1_122]: https://marketplace.visualstudio.com/items?itemName=young91.pr-comment-generator

[^1_123]: https://graphite.dev/guides/github-pull-request-extensions-vs-code

[^1_124]: https://www.semanticscholar.org/paper/a0c3c92ff5a24e12ddca99077f09876d254a2ff0

[^1_125]: http://link.springer.com/10.1007/978-3-319-42061-5_13

[^1_126]: https://dl.acm.org/doi/10.1145/2723372.2742797

[^1_127]: http://nsca.allenpress.com/nscaonline/?request=get-abstract\&doi=10.1519%2FR-21366.1

[^1_128]: http://ieeexplore.ieee.org/document/7092950/

[^1_129]: https://www.youtube.com/watch?v=RcxvrhQKv8I

[^1_130]: https://pwvas.org/index.php/pwvas/article/view/1068

[^1_131]: https://arxiv.org/abs/2407.02392

[^1_132]: https://www.exxactcorp.com/blog/deep-learning/run-llms-locally-with-continue-vs-code-extension

[^1_133]: https://jeeit.feit.ukim.edu.mk/index.php/jeeit/article/view/219

[^1_134]: http://link.springer.com/10.1007/978-3-642-00457-5_8

[^1_135]: https://www.semanticscholar.org/paper/0e74cad439bc353cb50066a0a16d3b9109f953f0

[^1_136]: https://www.semanticscholar.org/paper/f9a7f3e2e35aa4230506862b6d217ae71827388a

[^1_137]: https://www.semanticscholar.org/paper/aee1b2c0a605a035f04a80932cb9dd0a1e649526

[^1_138]: https://www.semanticscholar.org/paper/7e38d1164f5eec6dd679054a6aa30940afb06b2b

[^1_139]: https://ieeexplore.ieee.org/document/10350769/

[^1_140]: https://visualstudiomagazine.com/articles/2023/03/08/vs-code-ai-tools.aspx

[^1_141]: http://medrxiv.org/lookup/doi/10.1101/2025.05.05.25326979

[^1_142]: https://arxiv.org/pdf/2409.14887.pdf

[^1_143]: https://x.com/rasbt/status/1782778273895731213

[^1_144]: https://www.semanticscholar.org/paper/34ddc3da70f5b17ae0a73266ad1e4f9ae155811f

[^1_145]: https://www.semanticscholar.org/paper/dfd2e6b57f4dfe6f98585353782c5df7680645f5

[^1_146]: https://www.semanticscholar.org/paper/b09b4ab0d07c08021b5d5372b0167d17c2fc897b

[^1_147]: https://www.semanticscholar.org/paper/4e4e391a2155a63c8d7660fbb1f6c13930b186a4

[^1_148]: https://www.semanticscholar.org/paper/3464bfb4003a1a4b24004eac4f85cb08938bd42f

[^1_149]: http://ieeexplore.ieee.org/document/6165314/

[^1_150]: http://ieeexplore.ieee.org/document/4359473/

[^1_151]: https://www.semanticscholar.org/paper/43c85e782a3cd8182751ab1b2b5647d1bb31d0b9

[^1_152]: https://www.semanticscholar.org/paper/2095acfccc9750d681c78d919e3f884c64818aad

[^1_153]: https://dl.acm.org/doi/10.1145/1869542.1869564

[^1_154]: https://www.semanticscholar.org/paper/ea38f9631c2851c198da759c2a920489cc04cc90

