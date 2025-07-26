<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

# n8n-Routed LLM Agents on Vertex AI: Critical Documentation \& Best Practices

## 1. n8n Hosting: Cloud vs Docker on Cloud Run — Price Matrix (2025 Tiers)

- n8n Cloud Starter: €20/month (2,500 executions, 5 active workflows) - https://n8n.io/pricing/ + confidence 5 [^1_1]
- n8n Cloud Pro: €50/month (10,000 executions, 15 active workflows) - https://n8n.io/pricing/ + confidence 5 [^1_2]
- Google Cloud Run Tier 1: \$0.00001800/vCPU-second, \$0.00000200/GiB-second (always-on) - https://cloud.google.com/run/pricing + confidence 5 [^1_3]
- Cloud Run monthly estimate: 1 vCPU, 1GB RAM ~\$52/month continuous - https://hamy.xyz/blog/2025-04_google-cloud-run-pricing + confidence 4 [^1_4]
- n8n self-hosted minimum: 2GB RAM, 2 CPU cores for basic workflows - https://osher.com.au/blog/how-to-self-host-n8n/ + confidence 4 [^1_5]
- n8n recommended specs: 4GB RAM, 4 CPU cores for 100 jobs/day - https://www.devhelp.ai/p/n8n-self-hosted-requirements + confidence 3 [^1_6]
- Cloud Run concurrency: Multiple requests share allocated CPU/memory per instance - https://cloud.google.com/run/pricing + confidence 5 [^1_3]


## 2. Webhook Security: Header-Auth, Basic-Auth, IP-whitelist, Rate-limit Node

- n8n webhook credentials support: Basic Auth, Header Auth, JWT Auth methods - https://docs.n8n.io/integrations/builtin/credentials/webhook/ + confidence 5 [^1_7]
- Header authentication setup: Configure custom header name and value for webhook security - https://docs.n8n.io/integrations/builtin/credentials/webhook/ + confidence 5 [^1_7]
- Basic auth configuration: Username/password authentication for webhook endpoints in n8n - https://docs.n8n.io/integrations/builtin/credentials/webhook/ + confidence 5 [^1_7]
- Bearer token validation: Custom webhook security using Authorization header checks - https://www.xqus.com/how-to-secure-webhooks-in-n8n-with-bearer-token-field-validation/ + confidence 4 [^1_8]
- Rate limiting implementation: Use webhook queuing and retry mechanisms for control - https://www.reddit.com/r/n8n/comments/1du9j7j/extra_security_layer_for_n8n_webhook/ + confidence 3 [^1_9]
- IP whitelisting: **UNKNOWN** - official n8n documentation lacks specific IP filtering guidance + confidence 1


## 3. Secret Management: n8n Encryption + GCP Secret Manager Integration

- n8n credential encryption: Uses N8N_ENCRYPTION_KEY environment variable for database encryption - https://docs.n8n.io/external-secrets/ + confidence 5 [^1_10]
- External secrets availability: Enterprise Self-hosted and Enterprise Cloud plans only - https://docs.n8n.io/external-secrets/ + confidence 5 [^1_10]
- GCP Secret Manager support: Officially supported external secrets provider in n8n Enterprise - https://docs.n8n.io/external-secrets/ + confidence 5 [^1_10]
- Secret naming constraints: Alphanumeric characters and underscores only, no spaces/hyphens - https://docs.n8n.io/external-secrets/ + confidence 5 [^1_10]
- Integration setup: Go to Settings > External Secrets, select GCP provider - https://docs.n8n.io/external-secrets/ + confidence 5 [^1_10]
- Usage syntax: Reference secrets using {{ \$secrets.gcpSecretsManager.secret_name }} expression - https://docs.n8n.io/external-secrets/ + confidence 5 [^1_10]


## 4. REST / CI-CD: API Endpoints for Workflow Create/Update, Git-sync

- n8n REST API availability: Not available during free trial, requires paid plan - https://docs.n8n.io/api/ + confidence 5 [^1_11]
- API authentication: Required for all n8n public API endpoints access - https://docs.n8n.io/api/ + confidence 5 [^1_11]
- Workflow endpoints: Create, update, delete workflows programmatically via REST API - https://docs.n8n.io/api/api-reference/ + confidence 5 [^1_12]
- Source control integration: Git-based environments feature for Enterprise plans - https://docs.n8n.io/hosting/ + confidence 4 [^1_13]
- API playground: Available for self-hosted instances at /rest/api/v1/docs - https://docs.n8n.io/api/using-api-playground/ + confidence 5 [^1_14]
- Cloud Build integration: **UNKNOWN** - no official n8n documentation for Cloud Build pipelines + confidence 1


## 5. Content-Policy Blueprints: OpenAI Policy 2025, DALL-E 3 Safety, Anthropic Constitution

- OpenAI Usage Policies: Updated 2025-01-29, clarifies prohibited activities and compliance - https://openai.com/policies/usage-policies/ + confidence 5 [^1_15]
- DALL-E 3 System Card: October 2023 release, details safety measures and training filtering - https://dalle-3.pages.dev + confidence 5 [^1_16]
- DALL-E 3 content filtering: Graphic sexual/violent content and hate symbols removed from training - https://dalle-3.pages.dev + confidence 5 [^1_16]
- Anthropic Constitutional AI: Framework published May 2023, establishes AI behavior principles - https://venturebeat.com/ai/anthropic-releases-ai-constitution-to-promote-ethical-behavior-and-development/ + confidence 4 [^1_17]
- Claude constitution principles: Discourages torture, slavery, cruelty, respects non-western cultures - https://www.businesstoday.in/technology/news/story/ai-with-morals-google-backed-anthropic-reveals-the-set-of-values-that-guide-its-ai-380756-2023-05-10 + confidence 4 [^1_18]
- Constitutional AI approach: Values learning, generalization, and law-governed AI behavior - https://claudeai.uk/anthropic-aims-to-create-a-better-constitution-for-ai/ + confidence 3 [^1_19]


## 6. Long-term Memory Architectures: MemGPT, LangChain + Vector-store

- MemGPT framework: Enables LLMs to manage hierarchical memory tiers like operating systems - https://sky.cs.berkeley.edu/project/memgpt/ + confidence 5 [^1_20]
- MemGPT evolution: Now called Letta, open-source stateful agents framework - https://github.com/letta-ai/letta + confidence 5 [^1_21]
- LangChain vector stores: Supports Chroma, FAISS, Pinecone, Weaviate, Milvus databases - https://dev.to/jamesli/detailed-explanation-of-langchains-vector-storage-and-retrieval-technology-1jfh + confidence 4 [^1_22]
- RAG retrieval heuristic: Similarity search with configurable k parameter for top results - https://dev.to/priyaselvaraj11/rag-and-langchain-basics-3n0h + confidence 4 [^1_23]
- Memory benchmarks: MemGPT achieves 92.5% accuracy on deep memory retrieval tasks - https://mem0.ai/blog/ai-agent-memory-benchmark/ + confidence 4 [^1_24]
- Vector search formula: k_top parameter determines number of similar chunks retrieved - https://dev.to/priyaselvaraj11/rag-and-langchain-basics-3n0h + confidence 4 [^1_23]


## 7. Evaluation Frameworks: OpenAI Evals, LMSYS Arena Metrics, Audit Checklists

- OpenAI Evals framework: Open-source systematic evaluation for LLMs and LLM-powered systems - https://datanorth.ai/blog/evals-openais-framework-for-evaluating-llms + confidence 4 [^1_25]
- LMSYS Arena scoring: Elo rating system based on crowdsourced human pairwise comparisons - https://www.gabormelli.com/RKB/LMSYS_Arena_Score + confidence 4 [^1_26]
- Factuality evaluation: Categories A-E classification system for output-reference consistency - https://www.promptfoo.dev/docs/guides/factuality-eval/ + confidence 4 [^1_27]
- Evaluation types: Basic ground-truth evals and model-graded evals for different use cases - https://datanorth.ai/blog/evals-openais-framework-for-evaluating-llms + confidence 4 [^1_25]
- Arena score interpretation: Higher scores indicate better performance, small differences may be insignificant - https://www.gabormelli.com/RKB/LMSYS_Arena_Score + confidence 4 [^1_26]
- Prompt audit methodology: **UNKNOWN** - specific factuality/policy-risk checklists not found in official sources + confidence 1

<div style="text-align: center">⁂</div>

[^1_1]: https://n8n.io/pricing/

[^1_2]: https://affmaven.com/n8n-pricing/

[^1_3]: https://cloud.google.com/run/pricing

[^1_4]: https://hamy.xyz/blog/2025-04_google-cloud-run-pricing

[^1_5]: https://osher.com.au/blog/how-to-self-host-n8n/

[^1_6]: https://www.devhelp.ai/p/n8n-self-hosted-requirements

[^1_7]: https://docs.n8n.io/integrations/builtin/credentials/webhook/

[^1_8]: https://www.xqus.com/how-to-secure-webhooks-in-n8n-with-bearer-token-field-validation/

[^1_9]: https://www.reddit.com/r/n8n/comments/1du9j7j/extra_security_layer_for_n8n_webhook/

[^1_10]: https://docs.n8n.io/external-secrets/

[^1_11]: https://docs.n8n.io/api/

[^1_12]: https://docs.n8n.io/api/api-reference/

[^1_13]: https://docs.n8n.io/hosting/

[^1_14]: https://docs.n8n.io/api/using-api-playground/

[^1_15]: https://openai.com/policies/usage-policies/

[^1_16]: https://dalle-3.pages.dev

[^1_17]: https://venturebeat.com/ai/anthropic-releases-ai-constitution-to-promote-ethical-behavior-and-development/

[^1_18]: https://www.businesstoday.in/technology/news/story/ai-with-morals-google-backed-anthropic-reveals-the-set-of-values-that-guide-its-ai-380756-2023-05-10

[^1_19]: https://claudeai.uk/anthropic-aims-to-create-a-better-constitution-for-ai/

[^1_20]: https://sky.cs.berkeley.edu/project/memgpt/

[^1_21]: https://github.com/letta-ai/letta

[^1_22]: https://dev.to/jamesli/detailed-explanation-of-langchains-vector-storage-and-retrieval-technology-1jfh

[^1_23]: https://dev.to/priyaselvaraj11/rag-and-langchain-basics-3n0h

[^1_24]: https://mem0.ai/blog/ai-agent-memory-benchmark/

[^1_25]: https://datanorth.ai/blog/evals-openais-framework-for-evaluating-llms

[^1_26]: https://www.gabormelli.com/RKB/LMSYS_Arena_Score

[^1_27]: https://www.promptfoo.dev/docs/guides/factuality-eval/

[^1_28]: https://papers.academic-conferences.org/index.php/ictr/article/view/3440

[^1_29]: https://www.semanticscholar.org/paper/d6fc2acc7d2ed6b7f9800adfd677a377c0e8bd97

[^1_30]: https://currentprotocols.onlinelibrary.wiley.com/doi/10.1002/cpz1.70095

[^1_31]: https://iopn.library.illinois.edu/journals/aliseacp/article/view/1759

[^1_32]: https://iwaponline.com/ws/article/8/2/189/26412/Hydroeconomic-analysis-of-water-supply-for-the

[^1_33]: http://ascelibrary.org/doi/10.1061/40976(316)190

[^1_34]: https://autogpt.net/n8-review/

[^1_35]: https://vinahost.vn/en/hosting-n8n/

[^1_36]: https://github.com/Codexship/N8N-free-plan-pricing/

[^1_37]: https://github.com/tooltec/N8N-Free-Plan/

[^1_38]: https://github.com/luke-lewandowski/n8n-cloudrun-example

[^1_39]: https://www.01net.com/en/web-hosting/n8n/

[^1_40]: https://thedigitalprojectmanager.com/reviews/n8n-pricing/

[^1_41]: https://dx.plos.org/10.1371/journal.pcbi.1012050

[^1_42]: https://eajournals.org/ijliss/vol11-issue-1-2025/google-tools-at-the-disposal-of-librarians-and-skills-for-the-enhancement-of-library-services-a-conceptual-review/

[^1_43]: https://www.nepjol.info/index.php/JACEM/article/view/26673

[^1_44]: https://journals.ku.edu/kjm/article/view/18617

[^1_45]: https://zenodo.org/record/3743493

[^1_46]: https://docs.n8n.io/hosting/installation/server-setups/digital-ocean/

[^1_47]: https://docs.n8n.io/hosting/installation/server-setups/google-cloud/

[^1_48]: https://docs.n8n.io/hosting/configuration/user-management-self-hosted/

[^1_49]: https://opensource-heroes.com/r/n8n-io/n8n-docs

[^1_50]: https://www.youtube.com/watch?v=f3qQ9oOrVSw

[^1_51]: https://docs.n8n.io/hosting/configuration/environment-variables/endpoints/

[^1_52]: https://support.account.wrk.com/en/articles/10806464-perform-an-api-call-in-n8n

[^1_53]: https://docs.n8n.io/hosting/installation/server-setups/aws/

[^1_54]: https://arxiv.org/pdf/1901.07309.pdf

[^1_55]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9147194/

[^1_56]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7924604/

[^1_57]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8575280/

[^1_58]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7070978/

[^1_59]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8963074/

[^1_60]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10459229/

[^1_61]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3264488/

[^1_62]: https://community.n8n.io/t/webhook-authentication/4566

[^1_63]: https://brickscoach.com/how-to-send-a-webhook-to-n8n-with-header-authentication-with-bricks-forge-pro-forms/

[^1_64]: https://deepwiki.com/n8n-io/n8n-docs/5-security-and-access-control

[^1_65]: https://n8npro.in/development/uilding-a-custom-api-endpoint-with-n8n/

[^1_66]: https://community.n8n.io/t/external-secrets-credentials-detection-for-google-cloud-platform-backend/123111

[^1_67]: https://brixxs.com/faq/hoe-beveilig-ik-credentials-in-n8n/

[^1_68]: https://arxiv.org/abs/2401.06967

[^1_69]: https://ojs.mahadewa.ac.id/index.php/jmti/article/view/3668

[^1_70]: https://www.mdpi.com/1999-5903/16/12/475

[^1_71]: https://ieeexplore.ieee.org/document/10885140/

[^1_72]: https://www.ijsr.net/archive/v12i8/SR23816170845.pdf

[^1_73]: https://ieeexplore.ieee.org/document/9472812/

[^1_74]: https://ejournal.akprind.ac.id/index.php/snast/article/view/4176

[^1_75]: http://www.scitepress.org/DigitalLibrary/Link.aspx?doi=10.5220/0007754601320143

[^1_76]: https://www.youtube.com/watch?v=Oywj7ammIaw

[^1_77]: https://cloud.google.com/functions/pricing-overview

[^1_78]: https://www.economize.cloud/blog/google-cloud-run-pricing/

[^1_79]: https://www.youtube.com/watch?v=SHi_EOkSAE0

[^1_80]: https://618media.com/en/blog/securing-data-privacy-with-dall-e/

[^1_81]: https://arxiv.org/abs/2305.10250

[^1_82]: https://arxiv.org/abs/2306.07174

[^1_83]: https://link.springer.com/10.3758/s13421-024-01532-9

[^1_84]: https://link.springer.com/10.3758/s13421-023-01514-3

[^1_85]: https://arxiv.org/abs/2402.17753

[^1_86]: https://arxiv.org/pdf/2310.08560.pdf

[^1_87]: https://askai.glarity.app/search/What-is-MemGPT-and-how-does-it-improve-language-models

[^1_88]: https://ai.plainenglish.io/unveiling-memgpt-the-evolution-of-memory-augmented-language-models-ebda3e762bcd?gi=bc42f2632d5d

[^1_89]: https://link.springer.com/10.1007/s10586-023-04237-x

[^1_90]: https://dl.acm.org/doi/10.1145/3715340.3715440

[^1_91]: https://journalwjarr.com/node/1190

[^1_92]: https://dl.acm.org/doi/10.1145/3196398.3196411

[^1_93]: https://www.semanticscholar.org/paper/7f7fabbcd2a92ef4382bc436defb88a07f9f7145

[^1_94]: https://dl.acm.org/doi/10.1145/3698062.3698065

[^1_95]: https://arxiv.org/abs/2501.16945

[^1_96]: https://ieeexplore.ieee.org/document/10589859/

[^1_97]: https://n8n.io/workflows/1750-creating-an-api-endpoint/

[^1_98]: https://docsbot.ai/prompts/business/internal-audit-checklist

[^1_99]: http://biorxiv.org/lookup/doi/10.1101/2025.03.15.641219

[^1_100]: https://journals.sagepub.com/doi/10.1177/002070209905400205

[^1_101]: https://www.semanticscholar.org/paper/61d0fb4d68037847eca25c6400423dec4d710f05

[^1_102]: https://www.semanticscholar.org/paper/ebe7a6a4825c637481b447ff0f40929756145d5f

[^1_103]: https://www.semanticscholar.org/paper/a96be6585e07819fc67bfc81d8c137542714edc0

[^1_104]: https://www.semanticscholar.org/paper/77c2c9dd4c2150a36b35a851f0b08557277d99ea

[^1_105]: https://www.semanticscholar.org/paper/5a376d1608cff1680e958da0d39d56e93ff9e1c6

[^1_106]: https://www.semanticscholar.org/paper/de87ed50c189c54e3b45026565385aa60d699002

[^1_107]: http://ieeexplore.ieee.org/document/6597677/

[^1_108]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11520899/

[^1_109]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10747996/

[^1_110]: https://ieeexplore.ieee.org/document/8885348/

[^1_111]: https://ieeexplore.ieee.org/document/8588304/

[^1_112]: https://www.g2.com/products/google-cloud-run/pricing

[^1_113]: https://direct.mit.edu/neco/article/9/8/1735-1780/6109

[^1_114]: https://link.springer.com/10.3758/s13421-024-01556-1

[^1_115]: https://link.springer.com/10.3758/s13421-024-01566-z

[^1_116]: https://link.springer.com/10.3758/s13421-024-01577-w

[^1_117]: https://link.springer.com/10.3758/s13421-023-01474-8

[^1_118]: https://github.com/madebywild/MemGPT

[^1_119]: https://www.semanticscholar.org/paper/f7e0df4f75dbf981b79cc22bf67570ba6d303532

[^1_120]: https://academic.oup.com/bioinformatics/article/38/12/3302/6584006

[^1_121]: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.n8n/

