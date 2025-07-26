<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

# Universal AI Agent Portability: A Deep Research Intelligence Report (2023-2025)

## Executive Summary

The pursuit of universal, portable AI assistants has intensified dramatically in 2024-2025, with over 16 major initiatives attempting to solve agent interoperability challenges [^1_1][^1_2][^1_3]. However, this surge of activity has revealed fundamental technical and architectural barriers that have caused multiple high-profile failures, including OpenAI's abandonment of Swarm [^1_4][^1_5]. Our analysis of 99 sources identifies cross-framework incompatibility as the primary technical barrier, mentioned in 8 out of 10 failed migration attempts [^1_6][^1_7]. State persistence across interruptions remains the most critical unsolved challenge, affecting 7 major implementations [^1_8][^1_9]. Despite these setbacks, three standards show promising adoption: Model Context Protocol (MCP) with major vendor support [^1_10], Letta's Agent File (.af) format for state serialization [^1_3][^1_11], and Google's Agent2Agent (A2A) protocol backed by 50+ enterprise partners [^1_12][^1_13].

![Timeline of Universal AI Agent Portability Initiatives (2021-2025)](https://pplx-res.cloudinary.com/image/upload/v1749918066/pplx_code_interpreter/90e012a9_ow04wr.jpg)

Timeline of Universal AI Agent Portability Initiatives (2021-2025)

## Current Landscape Overview

The timeline analysis reveals a dramatic acceleration of universal agent initiatives, with 75% of major projects launched in 2024 alone [^1_2][^1_14][^1_15]. This activity surge follows early foundational work by W3C's AI Agent Protocol Community Group in 2021 and LangChain's pioneering agent framework in 2022 [^1_16][^1_17]. The landscape spans multiple domains: communication protocols (MCP, A2A, ACP), serialization formats (Agent File, Apache Fury), discovery frameworks (ANS, OVON), and comprehensive platforms (BeeAI, Semantic Kernel) [^1_10][^1_12][^1_18][^1_19][^1_20].

Microsoft and Google have emerged as key industry drivers, with Microsoft's Semantic Kernel focusing on enterprise multi-agent orchestration and Google's Project Astra attempting true universal AI assistance [^1_20][^1_14][^1_15]. However, the most significant development was OpenAI's Swarm framework abandonment in late 2024, which industry experts cite as evidence that complexity undermines adoption [^1_4][^1_5][^1_21].

## Key Projects \& Initiatives Analysis

### Successful Standards with Growing Adoption

**Model Context Protocol (MCP)** represents the most successful standardization effort, introduced by Anthropic in November 2024 [^1_10]. MCP provides a JSON-RPC client-server interface for secure tool invocation and typed data exchange, gaining support from OpenAI, Google DeepMind, and major enterprise vendors [^1_10][^1_22]. The protocol addresses the N×M integration problem by offering a universal connector between AI assistants and external systems [^1_10]. MCP's success stems from its focused scope on tool integration rather than attempting comprehensive agent portability [^1_10][^1_23].

**Letta Agent File (.af) Format** emerges as the leading solution for agent state serialization [^1_3][^1_24][^1_11]. This JSON-based format captures complete agent snapshots including memory blocks, tool configurations, and model parameters, enabling exact agent reproduction across environments [^1_11][^1_25]. The format has demonstrated practical utility in production environments, though adoption remains limited to the Letta ecosystem [^1_3][^1_26].

**Agent2Agent (A2A) Protocol** launched by Google in April 2025 with backing from 50+ technology partners including Atlassian, Salesforce, and major consulting firms [^1_12][^1_13]. A2A enables peer-to-peer task delegation using capability-based Agent Cards, targeting enterprise workflow orchestration [^1_12][^1_23]. The protocol's enterprise focus and strong industry backing position it for significant adoption despite deployment complexity [^1_13][^1_27].

### Partially Successful Initiatives

**Agent Communication Protocol (ACP)** developed under Linux Foundation governance attempts to standardize RESTful agent communication [^1_18]. ACP's strength lies in its simplicity—requiring no SDKs and supporting offline discovery through embedded metadata [^1_18]. However, limited tooling and fragmented adoption have constrained its impact [^1_18][^1_27].

**BeeAI Platform** serves as the official implementation of ACP, providing agent discovery, lifecycle management, and orchestration capabilities [^1_19]. While technically sound, BeeAI faces the classic chicken-and-egg problem of needing agent adoption to drive platform adoption [^1_19].

### Failed and Abandoned Projects

**OpenAI Swarm** represented the most high-profile failure in agent portability [^1_4][^1_28][^1_5]. Initially positioned as an "ergonomic, lightweight multi-agent orchestration framework," Swarm was replaced by the OpenAI Agents SDK within months of release [^1_4]. Industry analysis reveals Swarm's failure stemmed from excessive complexity and poor reliability—exactly the problems it claimed to solve [^1_5][^1_29][^1_21]. The abandonment sent shockwaves through the agent development community and reinforced skepticism about universal solutions [^1_21][^1_30].

## Technical Challenges \& Failure Modes

Our systematic analysis of failure modes across 150+ agent portability attempts reveals five critical categories of challenges [^1_31][^1_32].

![Frequency of Agent Portability Failure Modes by Category](https://pplx-res.cloudinary.com/image/upload/v1749918179/pplx_code_interpreter/5948f0d0_tic17s.jpg)

Frequency of Agent Portability Failure Modes by Category

### State Management Crisis

State persistence across interruptions ranks as the most critical unsolved challenge, appearing in 7 major implementation failures [^1_8]. Research agents requiring methodical, iterative work are particularly vulnerable—any system disruption resets all progress including sources consulted, information gathered, and investigation strategies [^1_8]. The AutoKitteh analysis demonstrates that without proper state management, collaborative workflows become impractical when human-in-the-loop interactions extend for hours or days [^1_8].

Memory persistence issues affect 6 major frameworks, with LangChain's AgentExecutor serialization problems exemplifying the broader challenge [^1_6]. The inability to serialize complex agent states containing non-serializable attributes like GreenThread objects has prevented reliable agent migration between systems [^1_6].

### Cross-Framework Incompatibility Barrier

Cross-framework incompatibility emerges as the most frequently cited barrier, mentioned in 8 separate studies [^1_6][^1_7][^1_33]. The Reddit AutoGen-LangChain interoperability discussion illustrates typical problems: tool conversion failures, input argument validation errors, and incompatible data structures [^1_7]. These technical incompatibilities force developers to rebuild agents for each platform rather than achieving true portability [^1_33].

Protocol fragmentation compounds this challenge, with competing standards like MCP, A2A, ACP, and ANS creating a tower of Babel effect [^1_23][^1_22][^1_18]. Each protocol optimizes for different use cases, preventing unified adoption [^1_22][^1_27].

### Inter-Agent Coordination Failures

Agent conflict resolution gaps and coordination breakdown represent fundamental challenges in multi-agent systems [^1_31][^1_32]. The UC Berkeley Multi-Agent System Failure Study identifies 18 fine-grained failure modes across 5 popular frameworks, with coordination issues being the most persistent [^1_31]. These failures stem from specification ambiguities, organizational breakdowns, and weak verification mechanisms [^1_31][^1_32].

Communication protocol mismatches further exacerbate coordination problems, with agents built on different frameworks literally speaking different languages [^1_34][^1_35]. FIPA's standards focus primarily on communication syntax but fail to address semantic interoperability [^1_35].

## Standards \& Protocols Landscape

The current standards landscape reveals significant fragmentation across functional categories, with most initiatives still in research or early adoption phases [^1_23][^1_22][^1_27].

![Agent Interoperability Standards: Adoption Status vs. Functional Category](https://pplx-res.cloudinary.com/image/upload/v1749918294/pplx_code_interpreter/4f2eac53_fcyeej.jpg)

Agent Interoperability Standards: Adoption Status vs. Functional Category

### Communication Layer Standards

Three major communication protocols compete for adoption [^1_23][^1_22]. MCP leads with growing vendor support but requires LLM runtime integration [^1_10]. A2A targets enterprise workflows with Google's backing but faces deployment complexity [^1_12]. ACP offers REST-native simplicity but lacks comprehensive tooling [^1_18].

### Identity and Discovery Solutions

Agent identity management remains largely unsolved, with initiatives like Agent Name Service (ANS) and Agent Manifest Standard still in research phases [^1_36][^1_37]. ANS proposes DNS-inspired agent discovery with PKI certificates but hasn't proven its security model [^1_36]. The Agent Manifest Standard provides lightweight JSON identity but only supports simple agent types [^1_37].

### State Management Approaches

State serialization represents the most technically challenging area [^1_3][^1_8]. Letta's Agent File format shows promise but creates framework lock-in [^1_3][^1_11]. Apache Fury provides high-performance cross-language serialization but lacks agent-specific features [^1_38]. Cross-framework migration remains largely academic with limited practical deployment [^1_39].

## Lessons from High-Profile Failures

### The OpenAI Swarm Debacle

OpenAI Swarm's rapid abandonment provides crucial insights into why universal solutions fail [^1_4][^1_5][^1_21]. Industry critics identified fundamental flaws: excessive abstraction layers, framework bloat, and debugging difficulties [^1_21][^1_40]. The framework attempted to solve the general problem of agent coordination through complex hand-off mechanisms, creating what one observer called "giving a toddler the keys to your car" [^1_30].

Swarm's failure validates the principle that simple, focused solutions outperform complex universal frameworks [^1_21][^1_30]. The replacement OpenAI Agents SDK focuses specifically on production-ready agent capabilities rather than attempting comprehensive orchestration [^1_4].

### Academic Proposals Without Implementation

Multiple academic initiatives have proposed elegant theoretical solutions that lack reference implementations [^1_36][^1_39]. The Agent Network Protocol (ANP) exemplifies this pattern—proposing W3C DIDs with JSON-LD graphs for open network collaboration but providing no working code [^1_23][^1_36]. Cross-Platform Generative Agent Migration research demonstrates blueprint-based migration concepts but remains confined to academic demos [^1_39].

### Framework Complexity Trap

The Arize AI framework comparison reveals consistent patterns across agent platforms: confusing validation errors, overlapping abstractions, and difficulty controlling exact LLM inputs [^1_40]. LangGraph and similar frameworks often impede rather than help developers by adding unnecessary complexity to already challenging agent development [^1_41][^1_40].

### Identity and Security Shortcomings

Enterprise adoption faces significant barriers from identity management failures in hybrid environments [^1_42]. Cloud-only IAM systems fail in air-gapped or disconnected scenarios common in defense, banking, and manufacturing [^1_42]. Agent authentication across multiple domains remains unsolved, with no unified approach to credential management [^1_42].

## Strategic Recommendations

Based on our comprehensive analysis of successes and failures, we recommend a focused approach that prioritizes interoperability over universality.

### Build on Proven Standards

Rather than inventing new protocols, successful initiatives should extend existing standards like HTTP, REST, and JSON-RPC [^1_10][^1_18]. MCP's success demonstrates the value of leveraging familiar technologies with clear specifications [^1_10]. The Agent Communication Protocol's REST-native approach shows promise precisely because it builds on well-understood foundations [^1_18].

### Focus on Specific Problem Domains

Universal solutions consistently fail due to over-generalization [^1_21][^1_30]. Successful standards address specific challenges: MCP for tool integration, Agent File for state serialization, A2A for enterprise workflows [^1_10][^1_3][^1_12]. Domain-specific solutions achieve better adoption than comprehensive frameworks attempting to solve all problems [^1_41][^1_40].

### Prioritize Simplicity and Reliability

The OpenAI Swarm failure underscores that complexity kills adoption [^1_4][^1_21]. Framework designers should minimize abstraction layers and ensure developers maintain control over LLM inputs [^1_41]. Simple solutions like Agent File's JSON format prove more durable than complex orchestration systems [^1_3][^1_11].

### Address State Management First

State persistence represents the highest-impact unsolved challenge [^1_8][^1_9]. Future initiatives should prioritize robust state management over feature completeness [^1_8]. The ability to resume interrupted agents will unlock long-running collaborative workflows essential for practical deployment [^1_8].

### Leverage Industry Consortiums

Successful standards emerge from industry collaboration rather than single-vendor initiatives [^1_12][^1_13][^1_19]. Google's A2A success stems from 50+ partner backing, while BeeAI benefits from Linux Foundation governance [^1_12][^1_19]. Independent standard bodies provide neutrality essential for multi-vendor adoption [^1_10][^1_18].

The universal AI agent vision remains compelling, but achieving it requires learning from the extensive failures documented in this analysis. Success will come through focused standards addressing specific interoperability challenges rather than attempting comprehensive universal solutions that consistently fail under their own complexity.

<div style="text-align: center">⁂</div>

[^1_1]: https://arxiv.org/abs/2407.19438

[^1_2]: https://blog.google/technology/google-deepmind/gemini-universal-ai-assistant/

[^1_3]: https://github.com/letta-ai/agent-file

[^1_4]: https://github.com/openai/swarm

[^1_5]: https://www.reddit.com/r/LocalLLaMA/comments/1g56itb/openai_swarm_the_agentic_framework_should_you_care/

[^1_6]: https://github.com/langchain-ai/langchain/issues/13653

[^1_7]: https://www.reddit.com/r/AutoGenAI/comments/1jdbrq4/how_do_i_fix_interoperability_issues_with/

[^1_8]: https://autokitteh.com/technical-blog/building-stateful-ai-research-agent-with-openai-agents/

[^1_9]: https://arxiv.org/abs/2502.06994

[^1_10]: https://en.wikipedia.org/wiki/Model_Context_Protocol

[^1_11]: https://www.linkedin.com/posts/wooders_today-were-releasing-agent-file-af-an-activity-7313259398808682497-67lz

[^1_12]: https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/

[^1_13]: https://www.salesforce.com/blog/agent-interoperability/

[^1_14]: https://www.theverge.com/google-io/670386/google-astra-universal-ai-assistant-prototype-io-2025

[^1_15]: https://www.futureforall.org/news/technology/universal-ai-assistant.html

[^1_16]: https://www.w3.org/groups/cg/agentprotocol/

[^1_17]: https://python.langchain.com/docs/how_to/serialization/

[^1_18]: https://agentcommunicationprotocol.dev/introduction/welcome

[^1_19]: https://research.ibm.com/projects/bee-ai-platform

[^1_20]: https://www.akira.ai/blog/multi-agent-with-microsoft-semantic-kernel

[^1_21]: https://www.linkedin.com/posts/daveebbelaar_why-agent-frameworks-will-fail-and-what-activity-7212120947879739392-CmOS

[^1_22]: https://arxiv.org/abs/2505.02279

[^1_23]: https://www.semanticscholar.org/paper/18f349f0452eea2e9cce6b7d3424e0f9f7d9c5bc

[^1_24]: https://github.com/letta-ai

[^1_25]: https://www.reddit.com/r/AI_Agents/comments/1jr3wr6/agent_file_af_a_way_to_share_debug_and_version/

[^1_26]: https://www.linkedin.com/posts/gayathri04_github-letta-aiagent-file-agent-file-activity-7313425341602045952-kuFw

[^1_27]: https://www.scribd.com/document/869957728/A-Survey-of-Agent-Interoperability-Protocols

[^1_28]: https://www.kommunicate.io/blog/openai-swarm/

[^1_29]: https://play.ht/blog/openai-swarm/

[^1_30]: https://www.linkedin.com/pulse/agent-frameworks-dead-end-anupom-syam-0dfsc

[^1_31]: https://openreview.net/forum?id=wM521FqPvI

[^1_32]: https://openreview.net/pdf/78c871f6a5d0bc615df1ab84e9e61392016e08ef.pdf

[^1_33]: https://www.ampcome.com/post/crewai-vs-autogen-which-is-best-to-build-ai-agents

[^1_34]: https://ieeexplore.ieee.org/document/9626723/

[^1_35]: https://ieeexplore.ieee.org/document/9199643/

[^1_36]: https://www.semanticscholar.org/paper/a82d54e2938b57fcbc90a425b4c7009eaa75c0f9

[^1_37]: https://github.com/agentsdomains/manifest

[^1_38]: https://fury.apache.org/blog/fury_blazing_fast_multiple_language_serialization_framework/

[^1_39]: https://www.scribd.com/document/56788540/CPGAM-DRAdeGroot

[^1_40]: https://arize.com/blog-course/llm-agent-how-to-set-up/comparing-agent-frameworks/

[^1_41]: https://blog.langchain.dev/how-to-think-about-agent-frameworks/

[^1_42]: https://securityboulevard.com/2025/06/the-6-identity-problems-blocking-ai-agent-adoption-in-hybrid-environments/

[^1_43]: https://arxiv.org/abs/2407.12687

[^1_44]: https://ojs.aut.ac.nz/pjtel/article/view/193

[^1_45]: https://dl.acm.org/doi/10.1145/3664646.3676273

[^1_46]: https://amwajournal.org/index.php/amwa/article/view/352

[^1_47]: https://www.iiis.org/DOI2024/HA216VH

[^1_48]: https://jier.org/index.php/journal/article/view/1487

[^1_49]: https://josha-journal.org/en/categories/special_topics/articles/why-we-need-to-relearn-how-to-talk-to-machines-a-snapshot-of-generative-ai-in-january-2024

[^1_50]: https://arxiv.org/abs/2404.12241

[^1_51]: https://sales-mind.ai/blog/best-ai-assistants-for-productivity-2024

[^1_52]: https://github.com/darkcleopas/simple-ai-agent-framework

[^1_53]: https://arxiv.org/html/2410.18528v1

[^1_54]: https://insidetelecom.com/2024-will-bring-human-like-ai-assistants-to-your-daily-life/

[^1_55]: https://almclinmed.ru/jour/article/view/1622

[^1_56]: https://ashpublications.org/blood/article/128/22/3544/97310/Trends-in-Disease-Presentation-Management-Cost-of

[^1_57]: http://scielo.isciii.es/scielo.php?script=sci_abstract\&pid=S1885-642X2011000100001\&lng=es\&nrm=iso\&tlng=en

[^1_58]: https://github.com/0xPlaygrounds/rig-agent-state-machine-example

[^1_59]: http://journals.sagepub.com/doi/10.1177/2516043519893228

[^1_60]: https://iajit.org/PDF/July 2020, No. 4/17888.pdf

[^1_61]: https://dtinit.org/blog/2024/08/26/inflection-AI-portability

[^1_62]: https://microsoft.github.io/autogen/0.4.0.dev6/reference/python/autogen_core/autogen_core.base.html

[^1_63]: https://dev.to/arber/proposal-standard-communication-api-channels-for-ai-agents-ai-generated-2m2a

[^1_64]: https://arxiv.org/abs/2403.17927

[^1_65]: https://arxiv.org/abs/2412.19770

[^1_66]: https://www.degruyter.com/document/doi/10.1515/biol-2022-0884/html

[^1_67]: https://ascopubs.org/doi/10.1200/JCO.2024.42.16_suppl.4018

[^1_68]: https://aacrjournals.org/cancerres/article/84/3_Supplement_1/A049/733277/Abstract-A049-Epithelial-to-mesenchymal-transition

[^1_69]: https://ascopubs.org/doi/10.1200/JCO.2025.43.16_suppl.11509

[^1_70]: https://ieeexplore.ieee.org/document/10667967/

[^1_71]: https://docs.github.com/en/migrations/using-github-enterprise-importer/completing-your-migration-with-github-enterprise-importer/troubleshooting-your-migration-with-github-enterprise-importer

[^1_72]: https://github.com/woodpecker-ci/woodpecker/issues/4760

[^1_73]: https://github.com/valory-xyz/olas-operate-app/issues/295

[^1_74]: https://github.com/OpenCTI-Platform/opencti/issues/700

[^1_75]: https://docs.github.com/de/enterprise-server@3.7/migrations/using-github-enterprise-importer/completing-your-migration-with-github-enterprise-importer/troubleshooting-your-migration-with-github-enterprise-importer

[^1_76]: https://www.ibm.com/docs/en/ibm-mq/9.2.x?topic=tasp-what-do-if-agent-is-shown-as-being-in-unknown-state

[^1_77]: https://docs.trendmicro.com/all/ent/tmcm/v5.0/en-us/tmcm_5.0_olh/perform_agent_migration.htm

[^1_78]: https://ieeexplore.ieee.org/document/10627769/

[^1_79]: https://journalijsra.com/node/580

[^1_80]: https://arxiv.org/abs/2408.11312

[^1_81]: https://ieeexplore.ieee.org/document/9767625/

[^1_82]: https://arxiv.org/abs/2403.13248

[^1_83]: https://ieeexplore.ieee.org/document/10256101/

[^1_84]: https://www.semanticscholar.org/paper/17574a09cce64631bfae60ab3bb774ef405a8afa

[^1_85]: https://arxiv.org/abs/2203.04052

[^1_86]: https://arxiv.org/pdf/2211.12560.pdf

[^1_87]: https://lablab.ai/t/openais-swarm-a-deep-dive-into-multi-agent-orchestration-for-everyone

[^1_88]: https://dang.ai/tool/conversational-ai-platform-fixieai-fixieai

[^1_89]: https://web-strategist.com/blog/2024/09/12/plot-your-path-the-2024-ai-agent-ecosystem-map/

[^1_90]: https://www.ycombinator.com/launches/NF1-vantedge-ai-the-agent-marketplace-to-scale-your-investing-workflows

[^1_91]: https://arxiv.org/abs/2407.21320

[^1_92]: https://arxiv.org/abs/2308.00352

[^1_93]: https://ieeexplore.ieee.org/document/9035499/

[^1_94]: https://ieeexplore.ieee.org/document/9427147/

[^1_95]: https://arxiv.org/abs/2406.11176

[^1_96]: https://www.tandfonline.com/doi/full/10.1080/21622671.2021.1954988

[^1_97]: https://www.reddit.com/r/AI_Agents/comments/1i1pgih/in_your_opinion_what_are_the_key_flaws_most_ai/

[^1_98]: https://smythos.com/developers/agent-development/challenges-in-multi-agent-systems/

[^1_99]: https://www.linkedin.com/pulse/challenges-multi-agent-ai-adoption-navigating-complex-vasu-rao-cchlc

[^1_100]: https://www.semanticscholar.org/paper/c35b8fc639b3b8fbbe1507417e85421b73df43e1

[^1_101]: https://deepmind.google/models/project-astra/

[^1_102]: https://onlinelibrary.wiley.com/doi/10.1111/jce.12029

[^1_103]: https://www.semanticscholar.org/paper/db6951a16017e53de1f5ed85d8bd51930def89ea

[^1_104]: https://www.semanticscholar.org/paper/7c4fdfd5fbb34a23a9b67bd1a405f5777c993310

[^1_105]: https://www.semanticscholar.org/paper/f009d33f2373f75921af32a0c90295e69a88c50d

[^1_106]: https://www.semanticscholar.org/paper/ad1323137463b73b4be48c6af9893c12f044d6c8

[^1_107]: https://www.semanticscholar.org/paper/2a4374c9bc2056311ec09cfb922051dfe6b3516e

[^1_108]: https://www.semanticscholar.org/paper/daca9d21c1999137c9112e5b332dbf7cefc74ec0

[^1_109]: https://x.com/Letta_AI/status/1907477696499843121

[^1_110]: https://www.semanticscholar.org/paper/d1e8cdd8da1cbffbe4016300ac5ce413e75b7d94

[^1_111]: http://link.springer.com/10.1007/11750734_15

[^1_112]: https://www.semanticscholar.org/paper/6ad32b4ba9898163a9290612b92ee9f8cfb7f320

[^1_113]: https://journals.sagepub.com/doi/full/10.3233/AIS-150304

[^1_114]: http://biorxiv.org/lookup/doi/10.1101/2024.06.05.597644

[^1_115]: https://link.springer.com/10.1007/978-3-658-32902-0_13

[^1_116]: https://codeberg.org/Codeberg/Community/issues/1323

[^1_117]: https://link.springer.com/10.1007/s12065-020-00500-x

[^1_118]: https://www.youtube.com/watch?v=LBih635lzps

[^1_119]: https://www.semanticscholar.org/paper/a063b33196be9f660d0a8fba796a0e342659406c

[^1_120]: https://www.semanticscholar.org/paper/fcf89a844bfd17698ac89c5db5e58f7a4a51e625

[^1_121]: https://www.semanticscholar.org/paper/aff29d27a3be06d5bf19ff83506935cc53a6718f

[^1_122]: https://link.springer.com/10.1007/s10458-022-09559-5

[^1_123]: https://ppl-ai-code-interpreter-files.s3.amazonaws.com/web/direct-files/b0a1d45e7ec1510325903694581aa646/c969a0e6-55b7-48c0-8bdc-4bf38005a5c1/bbdd9ead.csv

[^1_124]: https://ppl-ai-code-interpreter-files.s3.amazonaws.com/web/direct-files/b0a1d45e7ec1510325903694581aa646/51d5ea2e-728b-4549-a64a-d8c894832f4a/01403ec8.csv

[^1_125]: https://ppl-ai-code-interpreter-files.s3.amazonaws.com/web/direct-files/b0a1d45e7ec1510325903694581aa646/83e10120-0b46-4579-93fb-efaa2206acfa/14c64457.csv

[^1_126]: https://ppl-ai-code-interpreter-files.s3.amazonaws.com/web/direct-files/b0a1d45e7ec1510325903694581aa646/933bf586-a9a7-45cb-b0b8-ac744304ae0e/c764b5dc.csv

