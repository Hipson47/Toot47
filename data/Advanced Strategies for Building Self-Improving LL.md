<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

# Advanced Strategies for Building Self-Improving LLM Reasoning Systems: A 2024-2025 Analysis

Based on analysis of 90+ research papers, open-source repositories, and industry implementations, this report examines the most advanced strategies for building and evolving reasoning logic in Large Language Models (LLMs) and AI assistants [^1_1][^1_2][^1_3].

## Revolutionary Framework Breakthroughs in 2024-2025

### Open-Source Reasoning Frameworks

The landscape of LLM reasoning has been transformed by several breakthrough frameworks that enable sophisticated self-improvement capabilities [^1_1][^1_4][^1_5]. **OpenR** represents the first open-source framework that successfully replicates OpenAI's O1-style reasoning with reinforcement learning, integrating test-time compute, process supervision, and advanced reasoning capabilities beyond traditional autoregressive methods [^1_4][^1_1]. This framework demonstrates substantial gains on mathematical reasoning tasks through reinforcement learning with process reward models [^1_4][^1_5].

**DAPO (Decoupled Clip and Dynamic Sampling Policy Optimization)** emerged as a state-of-the-art large-scale reinforcement learning system, achieving 50 points on AIME 2024 using Qwen2.5-32B as the base model [^1_5][^1_6]. The system introduces four key algorithmic innovations that enable successful large-scale LLM reinforcement learning, with full open-source implementation available through the verl framework [^1_5][^1_6].

### Self-Feedback and Evaluation Systems

**RLAIF-V** introduces a novel framework for aligning multimodal language models using fully open-source paradigms [^1_7][^1_2]. The system reduces object hallucination by 80.7% and overall hallucination by 33.7%, demonstrating that RLAIF-V 12B can achieve super GPT-4V trustworthiness through self-alignment mechanisms [^1_7][^1_2]. This framework maximally explores open-source MLLMs from two perspectives: high-quality feedback data generation for preference learning and self-feedback guidance for inference-time scaling [^1_7][^1_2].

**EQUATOR (Evaluation of Question Answering Thoroughness in Open-ended Reasoning)** provides a deterministic framework that combines deterministic scoring with factual accuracy assessment [^1_2][^1_3]. This system pairs open-ended questions with human-evaluated answers using vector databases, enabling more precise and scalable evaluations while significantly reducing reliance on human evaluators [^1_2][^1_3].

![Advanced AI Feedback Loop Architecture for LLM Reasoning Improvement](https://pplx-res.cloudinary.com/image/upload/v1749828132/gpt4o_images/azkntdahy5sdnecufrpp.png)

Advanced AI Feedback Loop Architecture for LLM Reasoning Improvement

## Multi-Agent Orchestration and Modular Workflow Design

### Advanced Orchestration Patterns

Modern multi-agent systems implement sophisticated orchestration patterns that enable complex task coordination and self-correction mechanisms [^1_8][^1_9][^1_10]. **Hierarchical Supervision** patterns, implemented through CrewAI, AutoGen, and LangGraph frameworks, provide high scalability for complex project management and enterprise workflows [^1_8][^1_11][^1_10]. These systems employ specialized agents for Refinement, Execution, Evaluation, Modification, and Documentation, leveraging iterative feedback loops powered by LLMs [^1_9][^1_10].

**Heterogeneous Swarms** represents a breakthrough in multi-LLM system optimization, employing directed acyclic graphs (DAGs) with topological message passing for collaborative generation [^1_10][^1_1]. This approach jointly optimizes model roles and weights, outperforming 15 baseline methods by 18.5% on average across 12 tasks [^1_10][^1_1]. The system discovers multi-LLM architectures with heterogeneous model roles and substantial collaborative gains [^1_10][^1_1].

![Multi-Agent Orchestration System for Advanced AI Workflows](https://pplx-res.cloudinary.com/image/upload/v1749828192/gpt4o_images/urd2qq7cjifgqr8zezh7.png)

Multi-Agent Orchestration System for Advanced AI Workflows

### Pipeline Chaining and Event-Driven Systems

**Pipeline Chaining** through LangChain, LlamaIndex, and Haystack frameworks offers low implementation complexity with high scalability for data processing and content generation pipelines [^1_8][^1_12][^1_13]. **Event-Driven Triggers** using Temporal and event systems provide real-time response capabilities with high scalability and low implementation complexity [^1_8][^1_14].

**Memory-Augmented Coordination** systems like Letta and MemGPT enable long-term learning and context preservation, though with high implementation complexity [^1_8][^1_12]. These systems maintain extended context windows and build RAG agents with sophisticated memory management [^1_12][^1_15].

![Multi-Agent Orchestration Patterns: Capability Comparison Across Key Dimensions](https://pplx-res.cloudinary.com/image/upload/v1749827966/pplx_code_interpreter/f5208cf6_riav1z.jpg)

Multi-Agent Orchestration Patterns: Capability Comparison Across Key Dimensions

## Real-World Implementation Examples and Case Studies

### SaaS and Automation Success Stories

**Browser Automation SaaS** represents the fastest-growing segment with 200% growth in 2024, led by companies like Axiom.ai [^1_16][^1_17][^1_18]. Axiom.ai enables no-code browser automation for TikTok scraping, automated uploads, and like/follow automation, saving users significant manual effort [^1_17][^1_19]. The platform allows users to automate website actions through visual interfaces, with integration capabilities to ChatGPT for AI-enhanced automation [^1_19][^1_17].

**TikTok/Shorts Automation** workflows typically employ GPT-4, Claude, or Gemini as core LLMs, with custom Python orchestration and Axiom.ai integration, delivering 300-500% ROI [^1_16][^1_17]. These systems automate video uploads in batches, extract data through web scraping, and automate engagement actions [^1_17][^1_19].

![AI Monetization Strategies: 2024 Growth Rates by Market Maturity](https://pplx-res.cloudinary.com/image/upload/v1749827868/pplx_code_interpreter/80f7f8a5_ljbyyk.jpg)

AI Monetization Strategies: 2024 Growth Rates by Market Maturity

### Enterprise AI Workflow Integration

**Zapier** has revolutionized AI workflow automation through Copilot, an AI-powered assistant for building workflows using natural language [^1_18][^1_20]. The platform includes AI by Zapier, which integrates GPT-4o mini into workflows without requiring API keys, enabling data extraction, content generation, and automated analysis [^1_18][^1_20]. Zapier Agents perform autonomous work across 7,000+ apps, with capabilities including data analysis, email drafting, and report generation [^1_18][^1_20].

**UiPath** demonstrates enterprise-scale automation success across healthcare, finance, and manufacturing sectors [^1_21][^1_22]. Case studies show CCS NHS Trust using "Ada," a digital worker powered by UiPath, to automate pediatric referrals and streamline data input from GP submissions [^1_21][^1_22]. State Street leverages automation to boost reliability and productivity while freeing teams for strategic tasks [^1_21][^1_22].

### Code Review and Development Automation

**Code Review \& Development** implementations using CodeLlama, DeepSeek-Coder, and GPT-4 with GitHub Actions orchestration deliver 400-600% ROI [^1_23][^1_24]. **SWE-RL** introduces the first approach to scale reinforcement learning-based LLM reasoning for real-world software engineering, achieving 41.0% solve rate on SWE-bench Verified [^1_23][^1_24]. This represents the best performance for medium-sized (<100B) LLMs, comparable to leading proprietary models like GPT-4o [^1_23][^1_24].

## Continuous Learning and Adaptive Logic Techniques

### Knowledge Injection and Gap Checking

**Knowledge Injection** techniques focus on modifying or augmenting language models with additional information to bias predictions toward specific knowledge domains [^1_25][^1_26]. Fine-tuning approaches include supervised fine-tuning with instruction tuning, reinforcement learning-based methods like RLHF and DPO, and unsupervised continual pre-training [^1_25][^1_26]. Continual pre-training proves particularly effective for injecting new knowledge, building upon knowledge stored during the pre-training phase [^1_25][^1_26].

**StreamBench** provides pioneering evaluation of continuous improvement for LLM agents over input-feedback sequences [^1_27][^1_28]. The benchmark simulates online learning environments where LLMs receive continuous feedback streams and iteratively enhance performance [^1_27][^1_28]. Critical components for successful streaming strategies include iterative adjustment mechanisms and comprehensive analysis of improvement patterns [^1_27][^1_28].

**Gap Analysis** in AI systems employs automated techniques to identify missing test cases, outdated scenarios, or performance bottlenecks [^1_29][^1_30]. AI-driven gap analysis revolutionizes software testing by providing scalable, accurate, and efficient identification of testing gaps compared to manual approaches [^1_29][^1_30]. These systems process up to 10 million log events daily with sub-300ms query latency [^1_29][^1_30].

### Self-Auditing and Reflection Mechanisms

**Chain-of-Thought (CoT)** analysis enables explicit breakdown of reasoning processes into intermediate steps, serving as a mechanism for agents to track and evaluate decision-making [^1_31][^1_32]. CoT transforms black-box AI models into transparent decision-making systems by emulating human reasoning patterns [^1_31][^1_32]. Implementation requires strategic prompt engineering and effective feedback loop integration [^1_31][^1_32].

**Self-Reflection** creates internal feedback loops where agents actively question their own conclusions, similar to human metacognition [^1_32][^1_14]. Recursive feedback loops enable AI systems to continuously monitor, evaluate, and adjust actions based on both external outcomes and internal states [^1_14][^1_33]. These systems develop forms of self-awareness through continuous self-assessment and iterative adjustment [^1_14][^1_33].

## Browser-Based Automation and Tool Integration Patterns

### No-Code Automation Platforms

**Axiom.ai** leads browser automation with visual web scraping, data entry, and spreadsheet automation capabilities [^1_19][^1_17]. The platform supports automation of any website without code, with connections to Zapier, Integromat, and webhooks [^1_19][^1_17]. Users report saving 63 hours of manual work in the first month, with automation efficiency equivalent to hiring a part-time assistant [^1_19][^1_17].

**Browser Automation** patterns typically implement low complexity with 2-6 week time-to-value, requiring minimal compute resources and automation skills [^1_17][^1_19]. Success metrics include automation coverage, time savings, and error reduction, with frameworks supporting Puppeteer, Selenium Grid, and visual automation tools [^1_17][^1_19].

### API-Less Integration Strategies

**Tool Integration Patterns** leverage Zapier, Model Context Protocol (MCP), and API orchestration for connecting AI systems to external tools [^1_18][^1_15]. The MCP protocol enables standardized tool interactions, while Zapier provides integration across 7,000+ applications [^1_18][^1_15]. These patterns achieve low implementation complexity with 2-6 week time-to-value [^1_18][^1_15].

**VoltAgent** represents an open-source TypeScript framework for building AI agents with modular building blocks [^1_15][^1_11]. The framework supports multi-agent systems coordination, extensible packages for voice interactions, and tooling integrations for external APIs and databases [^1_15][^1_11]. VoltAgent implements the Model Context Protocol for standardized tool interactions [^1_15][^1_11].

## Leading Company Strategies and Monetization Analysis

### Market Leadership and Funding Trends

**Foundation Model Companies** lead with massive funding rounds exceeding \$1B, including OpenAI (\$13B), Anthropic (\$7.3B), and xAI (\$12B) [^1_34][^1_35]. The combined \$81 billion in venture funding represents more than half of the total \$142.45 billion raised by companies on Forbes' AI 50 list [^1_34][^1_35]. Multi-agent frameworks attract Series A/B funding (\$10-100M), while AI workflow automation companies secure growth-stage investments (\$50-200M) [^1_34][^1_35].

**StackAI** exemplifies the agentic AI investment trend, raising \$16 million in Series A funding led by Lobby Capital for their no-code platform enabling companies to build AI agents [^1_36][^1_37]. The startup's agents interact with software like Snowflake and Salesforce, completing back-office tasks including data entry, content aggregation, and information categorization [^1_36][^1_37].

### High-Growth Monetization Strategies

**Prompt Marketplaces** demonstrate exceptional 180% growth in 2024, with platforms like Snack Prompt and PromptBase enabling creators to monetize AI prompts [^1_38][^1_16]. These platforms implement commission-based revenue sharing models, allowing content creators to sell unique prompts directly to followers [^1_38][^1_16]. The prompt marketplace model represents a \$5B+ opportunity by 2026 [^1_16][^1_38].

**AI Marketplaces** achieve 120% growth through transaction fee models, with Hugging Face leading platform development [^1_16][^1_34]. Hugging Face creates ecosystems where developers offer AI solutions to end-users, generating revenue through premium features, enterprise solutions, and commercial usage fees [^1_16][^1_34].

**Hyper-Personalization** strategies deliver 60% growth through subscription and usage-based models, exemplified by Netflix and Amazon implementations [^1_16][^1_39]. These approaches leverage conversational AI for 24/7 personalized support, intelligent search functionalities, and AI-based customer experience optimization [^1_16][^1_39].

### Enterprise Adoption and ROI Analysis

**Enterprise AI Solutions** demonstrate substantial ROI across multiple sectors, with implementations ranging from 200-700% returns depending on use case complexity and integration scope [^1_21][^1_22]. **Morgan Stanley** exemplifies successful enterprise AI adoption, with 98% of wealth advisors using OpenAI technology daily after intensive model evaluations on document translation, report summarization, and output comparison [^1_40][^1_21].

**DoorDash** integrated voice-based AI customer service pilots in two months, validating concepts before scaling further [^1_40][^1_21]. This measured approach follows best practices of starting with focused pilots, establishing clear success metrics, and iterating rapidly based on user feedback [^1_40][^1_21].

## Implementation Roadmap and Strategic Recommendations

### Phased Approach to Advanced AI Workflows

**Phase 1: Foundation (Months 1-3)** focuses on self-evaluation systems and browser automation, requiring medium complexity implementation with 2-4 month time-to-value for evaluation systems [^1_41][^1_42]. Organizations should deploy Chain-of-Thought reasoning, EQUATOR evaluation frameworks, and Axiom.ai or custom Puppeteer integration [^1_41][^1_42].

**Phase 2: Advanced Integration (Months 4-8)** involves multi-agent orchestration and knowledge injection, with high complexity implementations requiring 4-8 months for orchestration systems [^1_10][^1_43]. This phase includes deploying CrewAI or AutoGen frameworks, implementing specialized agent roles, and building RAG systems with vector databases [^1_10][^1_43].

**Phase 3: Optimization (Months 9-16)** encompasses continuous learning integration and advanced reasoning implementation, representing the highest complexity with 8-16 month timelines [^1_44][^1_27]. Organizations should integrate OpenR or DAPO frameworks, implement recursive feedback loops, and deploy reinforcement learning systems [^1_44][^1_27].

### Success Metrics and Risk Mitigation

**Technical Metrics** include feedback quality assessment, accuracy improvement measurement, coordination efficiency evaluation, and learning rate analysis [^1_30][^1_27]. **Business Metrics** encompass revenue growth tracking, operational efficiency measurement, performance optimization analysis, and integration success evaluation [^1_30][^1_27].

**Risk Mitigation** strategies address common pitfalls including overengineering, insufficient evaluation, vendor lock-in, and resource underestimation [^1_45][^1_30]. Security considerations include AI-driven insider risk management, automated anomaly detection, model governance frameworks, and regular compliance audits [^1_45][^1_30].

## Future Outlook and Market Opportunities

The AI workflow automation market represents unprecedented growth opportunities, with AI workflow automation projected to reach \$100B+ by 2030, multi-agent systems targeting \$50B+ by 2028, and browser automation approaching \$20B+ by 2027 [^1_16][^1_46]. Organizations investing in advanced AI workflow capabilities now will establish significant competitive advantages as these technologies mature and become ubiquitous across industries [^1_16][^1_46].

The transition from experimental frameworks to production-ready systems marks 2024-2025 as a pivotal period for AI workflow automation adoption [^1_1][^1_46]. Success requires balanced approaches combining cutting-edge research with practical implementation, supported by robust evaluation and continuous improvement mechanisms [^1_1][^1_46].

<div style="text-align: center">⁂</div>

[^1_1]: https://arxiv.org/abs/2504.19678

[^1_2]: https://arxiv.org/abs/2501.00257

[^1_3]: https://arxiv.org/html/2503.10814v1

[^1_4]: https://arxiv.org/abs/2410.09671

[^1_5]: https://arxiv.org/abs/2503.14476

[^1_6]: https://www.semanticscholar.org/paper/7808483b2a9147318e8bc6078ed9566e12555a2c

[^1_7]: https://www.semanticscholar.org/paper/db54861e0b31b0b341bbc9655f30dca98201ffca

[^1_8]: https://temporal.io/blog/what-are-multi-agent-workflows

[^1_9]: https://arxiv.org/abs/2412.17149

[^1_10]: https://arxiv.org/abs/2502.04510

[^1_11]: https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/

[^1_12]: https://zilliz.com/blog/10-open-source-llm-frameworks-developers-cannot-ignore-in-2025

[^1_13]: https://arxiv.org/abs/2410.01782

[^1_14]: https://www.linkedin.com/pulse/how-recursive-feedback-loops-enable-emergent-ai-gary-ramah-hhbvf

[^1_15]: https://github.com/VoltAgent/voltagent

[^1_16]: https://digicrusader.com/ai-monetization-strategies-turning-innovation-into-revenue/

[^1_17]: https://axiom.ai/automate/tiktok-scraper

[^1_18]: https://zapier.com/blog/best-ai-productivity-tools/

[^1_19]: https://axiom.ai

[^1_20]: https://www.flowforma.com/blog/ai-workflow-automation-guide

[^1_21]: https://www.uipath.com/resources/automation-case-studies

[^1_22]: https://journalajrcos.com/index.php/AJRCOS/article/view/628

[^1_23]: https://arxiv.org/abs/2502.18449

[^1_24]: https://www.semanticscholar.org/paper/f0e77b98ea172c4b7b4448f6c7df49d4831205eb

[^1_25]: https://zilliz.com/blog/knowledge-injection-in-llms-fine-tuning-and-rag

[^1_26]: https://arxiv.org/html/2402.01364v1

[^1_27]: https://arxiv.org/abs/2406.08747

[^1_28]: https://github.com/Wang-ML-Lab/llm-continual-learning-survey

[^1_29]: https://www.opkey.com/blog/how-ai-is-revolutionizing-gap-analysis-in-software-testing-process

[^1_30]: https://www.semanticscholar.org/paper/79479ba82a27067aad2ad01b56c1b4ab1b8f483f

[^1_31]: https://sebastianraschka.com/blog/2025/understanding-reasoning-llms.html

[^1_32]: https://galileo.ai/blog/self-evaluation-ai-agents-performance-reasoning-reflection

[^1_33]: https://fonzi.ai/blog/self-evaluating-ai-feedback

[^1_34]: https://www.forbes.com/lists/ai50/

[^1_35]: https://www.entrans.ai/blog/top-11-ai-development-companies-in-2024

[^1_36]: https://www.businessinsider.com/pitch-deck-ai-agent-startup-stackai-series-a-funding-round-2025-5

[^1_37]: https://explodingtopics.com/blog/ai-startups

[^1_38]: https://snack-prompt.canny.io/feature-requests/p/prompt-marketplace-to-sell-your-prompts-earn-money

[^1_39]: https://devlabs.angelhack.com/blog/what-ai-integrations-are-saas-using-in-2025/

[^1_40]: https://www.linkedin.com/pulse/openai-anthropic-playbooks-practical-guide-enterprise-gleb-markevich-evjse

[^1_41]: https://ieeexplore.ieee.org/document/10663193/

[^1_42]: https://ieeexplore.ieee.org/document/10791207/

[^1_43]: https://arxiv.org/abs/2503.08123

[^1_44]: https://arxiv.org/abs/2312.10003

[^1_45]: https://www.mdpi.com/2813-2203/2/2/20

[^1_46]: https://s-rsa.com/index.php/agi/article/view/14755

[^1_47]: https://ieeexplore.ieee.org/document/11018434/

[^1_48]: https://arxiv.org/abs/2503.00025

[^1_49]: https://aclanthology.org/2024.semeval-1.60

[^1_50]: https://www.semanticscholar.org/paper/79797c601d25b99f5e98f9aa8c618bc9862ff67c

[^1_51]: https://arxiv.org/abs/2408.05141

[^1_52]: https://kili-technology.com/large-language-models-llms/llm-reasoning-guide

[^1_53]: https://www.linkedin.com/pulse/top-5-llms-reasoning-capabilities-2025-andreas-ramos-8uf9c

[^1_54]: https://www.ml-science.com/model-self-improvement

[^1_55]: https://www.byteplus.com/en/topic/380950

[^1_56]: https://appian.com/blog/acp/process-automation/ai-workflow-automation

[^1_57]: https://ijpeds.iaescore.com/index.php/IJPEDS/article/view/23901

[^1_58]: https://www.mdpi.com/1660-4601/15/12/2895

[^1_59]: https://arxiv.org/abs/2305.10142

[^1_60]: https://arxiv.org/abs/2411.09706

[^1_61]: https://www.frontiersin.org/articles/10.3389/feduc.2023.1213444/full

[^1_62]: https://ieeexplore.ieee.org/document/10931931/

[^1_63]: https://www.gigaspaces.com/question/how-do-feedback-loops-enhance-self-reflection-in-ai-agents

[^1_64]: https://irisagent.com/blog/the-power-of-feedback-loops-in-ai-learning-from-mistakes/

[^1_65]: https://aclanthology.org/2024.tacl-1.78.pdf

[^1_66]: https://www.salesforce.com/agentforce/ai-agents/autonomous-agents/

[^1_67]: https://arxiv.org/abs/2401.02954

[^1_68]: https://www.semanticscholar.org/paper/aded5be5cf72cef57dbf8c889791012246bc5731

[^1_69]: https://arxiv.org/abs/2404.02078

[^1_70]: https://arxiv.org/abs/2404.10642

[^1_71]: https://www.semanticscholar.org/paper/463de56fb2c9544069531e6b386139e5086f40fc

[^1_72]: https://github.com/atfortes/Awesome-LLM-Reasoning

[^1_73]: https://github.com/eugeneyan/open-llms

[^1_74]: https://www.aibase.com/repos/topic/llm-reasoning

[^1_75]: https://www.reddit.com/r/LocalLLaMA/comments/1kqekgh/best_nonchinese_open_reasoning_llms_atm/

[^1_76]: https://mlaj-revista.org/index.php/journal/article/view/86

[^1_77]: https://www.spiedigitallibrary.org/conference-proceedings-of-spie/13546/3060513/AI-eXpress--a-new-satellite-as-a-service-concept/10.1117/12.3060513.full

[^1_78]: https://www.jmir.org/2025/1/e69881

[^1_79]: https://aipolicylab.se/2025/03/25/potential-impact-of-the-eu-platform-work-directive-on-ai-labelers/

[^1_80]: https://telehealthandmedicinetoday.com/index.php/journal/article/view/565

[^1_81]: https://onepetro.org/JPT/article/76/05/8/544711/Comments-Grabbing-the-Brass-Ring-To-Power-the

[^1_82]: https://biss.pensoft.net/article/136839/

[^1_83]: https://oceanrep.geomar.de/id/eprint/61170/

[^1_84]: https://ieeexplore.ieee.org/document/11027716/

[^1_85]: https://arxiv.org/abs/2407.09024

[^1_86]: https://www.reddit.com/r/LocalLLaMA/comments/19bgv60/continual_learning_in_llm/

[^1_87]: https://dev.to/nareshnishad/day-42-continual-learning-in-llms-1l4g

[^1_88]: https://aclanthology.org/2025.coling-main.402.pdf

[^1_89]: https://mirascope.com/blog/advanced-prompt-engineering

[^1_90]: https://www.hannes-lehmann.com/en/blog/ai-integration-patterns/

[^1_91]: http://medrxiv.org/lookup/doi/10.1101/2025.06.06.25329104

[^1_92]: https://linkinghub.elsevier.com/retrieve/pii/S1071581924001939

[^1_93]: https://www.surveysensum.com/blog/ai-feedback-loop

[^1_94]: https://arxiv.org/abs/2506.03921

[^1_95]: https://www.instaclustr.com/education/open-source-ai/top-10-open-source-llms-for-2025/

[^1_96]: https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/superagency-in-the-workplace-empowering-people-to-unlock-ais-full-potential-at-work

[^1_97]: https://www.semanticscholar.org/paper/5f6af9085b01843383d524f4acb9935ea05c1f93

[^1_98]: https://arxiv.org/abs/2402.01364

[^1_99]: https://ppl-ai-code-interpreter-files.s3.amazonaws.com/web/direct-files/8ade77001c4aa0348b8f5d6303dc4dbd/c5a9e48f-bfb1-42ed-87ed-83324a7f5305/ccf4e0ab.md

[^1_100]: https://ppl-ai-code-interpreter-files.s3.amazonaws.com/web/direct-files/8ade77001c4aa0348b8f5d6303dc4dbd/4b87b829-175e-413d-a857-90d29932397c/0e567399.csv

[^1_101]: https://ppl-ai-code-interpreter-files.s3.amazonaws.com/web/direct-files/8ade77001c4aa0348b8f5d6303dc4dbd/4b87b829-175e-413d-a857-90d29932397c/e7e0d260.csv

[^1_102]: https://ppl-ai-code-interpreter-files.s3.amazonaws.com/web/direct-files/8ade77001c4aa0348b8f5d6303dc4dbd/4b87b829-175e-413d-a857-90d29932397c/bf943a15.csv

[^1_103]: https://ppl-ai-code-interpreter-files.s3.amazonaws.com/web/direct-files/8ade77001c4aa0348b8f5d6303dc4dbd/4caf540d-0aa8-4f4a-b0c1-bfac964aa6be/6c493245.csv

[^1_104]: https://ppl-ai-code-interpreter-files.s3.amazonaws.com/web/direct-files/8ade77001c4aa0348b8f5d6303dc4dbd/4caf540d-0aa8-4f4a-b0c1-bfac964aa6be/c041dcc8.csv

[^1_105]: https://ppl-ai-code-interpreter-files.s3.amazonaws.com/web/direct-files/8ade77001c4aa0348b8f5d6303dc4dbd/4caf540d-0aa8-4f4a-b0c1-bfac964aa6be/65acb968.csv

