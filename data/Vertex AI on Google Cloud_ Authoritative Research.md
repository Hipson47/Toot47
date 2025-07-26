<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

# Vertex AI on Google Cloud: Authoritative Research Findings

## Free \$300 Credit Terms \& Limits

- (5) New customers get \$300 in free credits valid for 90 days—no billing until paid account activation. [https://cloud.google.com/free](https://cloud.google.com/free) [^1_1]
- (5) Credit applies to all Google Cloud resources including Vertex AI; separate Always Free tier available. [https://cloud.google.com/free/docs/free-cloud-features](https://cloud.google.com/free/docs/free-cloud-features) [^1_2]
- (4) Trial restrictions include max 8 concurrent cores, no GPUs on VMs, no quota increases. [https://cloudkul.com/blog/google-cloud-platform-free-tier/](https://cloudkul.com/blog/google-cloud-platform-free-tier/) [^1_3]
- (4) Free Tier offers 20+ products with monthly limits not charged against \$300 credit. [https://cloud.google.com/free](https://cloud.google.com/free) [^1_1]


## Supported Generative Models

- (5) Current models: Gemini 2.5 Pro/Flash, Gemini 2.0 Flash/Flash-Lite with multimodal capabilities. [https://cloud.google.com/vertex-ai/generative-ai/docs/model-garden/available-models](https://cloud.google.com/vertex-ai/generative-ai/docs/model-garden/available-models) [^1_4]
- (5) Imagen 4.0 for image generation, Chirp 2 for speech, plus 200+ foundation models. [https://cloud.google.com/vertex-ai/generative-ai/docs/model-garden/available-models](https://cloud.google.com/vertex-ai/generative-ai/docs/model-garden/available-models) [^1_4]
- (5) text-bison and chat-bison models retire April 21, 2025—migrate to Gemini alternatives. [https://cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versions](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versions) [^1_5]
- (4) Partner models include Claude Opus 4, Llama 4 Scout, Mistral Large available via managed APIs. [https://cloud.google.com/vertex-ai/generative-ai/docs/model-garden/available-models](https://cloud.google.com/vertex-ai/generative-ai/docs/model-garden/available-models) [^1_4]


## Pricing After Credit Expires

- (5) Gemini 2.0 Flash: \$0.15/\$0.60 per 1M tokens (input/output); batch API 50% discount. [https://cloud.google.com/vertex-ai/generative-ai/pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing) [^1_6]
- (5) Partner models range from \$0.20 (Jamba Mini) to \$75 (Claude Opus 4) per 1M output tokens. [https://cloud.google.com/vertex-ai/generative-ai/pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing) [^1_6]
- (4) AutoML training starts at \$1.375/node hour; custom training varies by machine type. [https://cloud.google.com/vertex-ai/pricing](https://cloud.google.com/vertex-ai/pricing) [^1_7]
- (4) Imagen 4 costs \$0.04/image; Imagen 4 Ultra \$0.06/image for generation tasks. [https://cloud.google.com/vertex-ai/generative-ai/pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing) [^1_6]


## Best-Practice Workflow for Small-Budget Prototyping

- (4) Start with Vertex AI Workbench instances (~\$0.12/hour) for small datasets and experimentation. [https://www.datacamp.com/tutorial/vertex-ai-tutorial](https://www.datacamp.com/tutorial/vertex-ai-tutorial) [^1_8]
- (4) Use 10-minute idle shutdown and e2-micro instances to minimize costs during development. [https://cloud.google.com/architecture/ml-on-gcp-best-practices](https://cloud.google.com/architecture/ml-on-gcp-best-practices) [^1_9]
- (4) Training within Workbench sufficient for small datasets; use training service for larger ones. [https://cloud.google.com/architecture/ml-on-gcp-best-practices](https://cloud.google.com/architecture/ml-on-gcp-best-practices) [^1_9]
- (3) Enable only required APIs and choose appropriate regions to optimize costs effectively. [https://www.restack.io/p/vertex-ai-solutions-answer-ai-pricing-model-strategies-cat-ai](https://www.restack.io/p/vertex-ai-solutions-answer-ai-pricing-model-strategies-cat-ai) [^1_10]


## API Authentication via Service Account JSON

- (5) Use Application Default Credentials with GOOGLE_APPLICATION_CREDENTIALS environment variable pointing to JSON key. [https://cloud.google.com/vertex-ai/docs/authentication](https://cloud.google.com/vertex-ai/docs/authentication) [^1_11]
- (5) Create service account via IAM Console, assign Vertex AI roles, download JSON key file. [https://cloud.google.com/vertex-ai/docs/general/custom-service-account](https://cloud.google.com/vertex-ai/docs/general/custom-service-account) [^1_12]
- (4) ADC searches credentials in order: env variable, gcloud auth, attached service account metadata. [https://github.com/svetamorag/VertexAI_Authentication](https://github.com/svetamorag/VertexAI_Authentication) [^1_13]
- (4) Custom service accounts provide fine-grained access control for different jobs and resources. [https://cloud.google.com/vertex-ai/docs/general/custom-service-account](https://cloud.google.com/vertex-ai/docs/general/custom-service-account) [^1_12]


## Rate Limits and Regional Endpoints

- (5) Standard quotas: 30,000 online prediction requests/minute, 600 resource management requests/minute per region. [https://cloud.google.com/vertex-ai/docs/quotas](https://cloud.google.com/vertex-ai/docs/quotas) [^1_14]
- (5) Regional endpoints format: https://REGION-aiplatform.googleapis.com (e.g., us-central1, europe-west4). [https://cloud.google.com/vertex-ai/docs/general/locations](https://cloud.google.com/vertex-ai/docs/general/locations) [^1_15]
- (4) Gemini API default quota: 100 RPM per project; model-specific limits apply. [https://www.genspark.ai/spark/understanding-rate-limits-in-vertex-ai-gemini/2dce3c7f-5724-4472-8a06-d27eaaba0c09](https://www.genspark.ai/spark/understanding-rate-limits-in-vertex-ai-gemini/2dce3c7f-5724-4472-8a06-d27eaaba0c09) [^1_16]
- (5) Partner models available in 7+ US regions; global endpoint available for some models. [https://cloud.google.com/vertex-ai/generative-ai/docs/learn/locations](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/locations) [^1_17]

<div style="text-align: center">⁂</div>

[^1_1]: https://cloud.google.com/free

[^1_2]: https://cloud.google.com/free/docs/free-cloud-features

[^1_3]: https://cloudkul.com/blog/google-cloud-platform-free-tier/

[^1_4]: https://cloud.google.com/vertex-ai/generative-ai/docs/model-garden/available-models

[^1_5]: https://cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versions

[^1_6]: https://cloud.google.com/vertex-ai/generative-ai/pricing

[^1_7]: https://cloud.google.com/vertex-ai/pricing

[^1_8]: https://www.datacamp.com/tutorial/vertex-ai-tutorial

[^1_9]: https://cloud.google.com/architecture/ml-on-gcp-best-practices

[^1_10]: https://www.restack.io/p/vertex-ai-solutions-answer-ai-pricing-model-strategies-cat-ai

[^1_11]: https://cloud.google.com/vertex-ai/docs/authentication

[^1_12]: https://cloud.google.com/vertex-ai/docs/general/custom-service-account

[^1_13]: https://github.com/svetamorag/VertexAI_Authentication

[^1_14]: https://cloud.google.com/vertex-ai/docs/quotas

[^1_15]: https://cloud.google.com/vertex-ai/docs/general/locations

[^1_16]: https://www.genspark.ai/spark/understanding-rate-limits-in-vertex-ai-gemini/2dce3c7f-5724-4472-8a06-d27eaaba0c09

[^1_17]: https://cloud.google.com/vertex-ai/generative-ai/docs/learn/locations

[^1_18]: https://nsojournals.onlinelibrary.wiley.com/doi/10.1111/ecog.07385

[^1_19]: https://informatics.bmj.com/lookup/doi/10.14236/jhi.v24i4.885

[^1_20]: https://www.mdpi.com/2073-445X/13/11/1950

[^1_21]: https://www.mdpi.com/2073-4395/15/4/873

[^1_22]: https://acnsci.org/journal/index.php/cte/article/view/205

[^1_23]: https://isprs-archives.copernicus.org/articles/XLII-1-W1/627/2017/

[^1_24]: https://www.googlecloudcommunity.com/gc/Community-Hub/Understand-GCP-free-300-Utilization/m-p/545702

[^1_25]: https://www.reddit.com/r/Firebase/comments/1d8ipon/question_about_the_300_free_trial_for_google/

[^1_26]: https://cloud.google.com/free?hl=tr

[^1_27]: https://tekpon.com/software/google-cloud-vertex-ai/pricing/

[^1_28]: https://www.clickittech.com/news/google-cloud-platform-free-tier/

[^1_29]: https://www.prowebtips.com/how-to-get-google-cloud-subscriptions-for-free/

[^1_30]: https://www.newittrendzzz.com/post/is-vertex-ai-free-to-use-exploring-your-options

[^1_31]: https://www.mdpi.com/2076-3417/14/22/10748

[^1_32]: https://ejurnal.seminar-id.com/index.php/bits/article/view/6040

[^1_33]: https://www.researchprotocols.org/2024/1/e58149

[^1_34]: https://www.ssrn.com/abstract=4714998

[^1_35]: https://academic.oup.com/hropen/article/doi/10.1093/hropen/hoae070/7906496

[^1_36]: http://medrxiv.org/lookup/doi/10.1101/2024.09.13.24313606

[^1_37]: https://cloud.google.com/vertex-ai/docs/supported-frameworks-list

[^1_38]: https://firebase.google.com/docs/vertex-ai/gemini-models

[^1_39]: https://cloud.google.com/vertex-ai/docs/release-notes

[^1_40]: https://dev.to/dataninsight/building-ai-powered-image-apps-with-gemini-and-imagen-on-vertex-ai-5d7f

[^1_41]: https://www.youtube.com/watch?v=16DmffaT7ew

[^1_42]: https://sg.news.yahoo.com/google-brings-gemini-pro-vertex-150032343.html

[^1_43]: https://cloud.google.com/vertex-ai/generative-ai/docs/release-notes

[^1_44]: https://journal-isi.org/index.php/isi/article/view/773

[^1_45]: https://www.frontiersin.org/articles/10.3389/fdgth.2024.1484503/full

[^1_46]: https://wjarr.com/content/machine-learning-financial-forecasting-us-review-exploring-advancements-challenges-and

[^1_47]: https://link.springer.com/10.1007/s40271-024-00720-8

[^1_48]: https://www.ewadirect.com/proceedings/ace/article/view/16996

[^1_49]: https://link.aps.org/doi/10.1103/PhysRevD.110.032015

[^1_50]: https://taxcloud.com/blog/avalara-vs-vertex-comparison/

[^1_51]: https://discuss.ai.google.dev/t/using-pay-as-you-go-before-may-30-2024/2031

[^1_52]: https://jaiinfoway.com/google-vertex-ai-pricing/

[^1_53]: https://cloud.google.com/generative-ai-app-builder/pricing

[^1_54]: https://cloud.google.com/ai-platform/pricing

[^1_55]: https://www.g2.com/products/calk-ai/pricing

[^1_56]: https://ieeexplore.ieee.org/document/10616506/

[^1_57]: https://ijitce.org/index.php/ijitce/article/view/1042

[^1_58]: https://dl.acm.org/doi/10.1145/3649158.3657043

[^1_59]: https://arxiv.org/abs/2207.10811

[^1_60]: https://www.granthaalayahpublication.org/ijetmr-ojms/ijetmr/article/view/1598

[^1_61]: https://dl.acm.org/doi/10.1145/3687272.3690890

[^1_62]: https://docs.vectorize.io/how-to/google-vertex-ai/create-a-gcp-service-account-for-google-vertex-ai/

[^1_63]: https://www.cloudskillsboost.google/course_templates/892/video/425580?locale=pl

[^1_64]: https://help.qlik.com/talend/en-US/components/8.0/google-drive/how-to-access-google-drive-using-service-account-json-file-a-google

[^1_65]: https://www.youtube.com/watch?v=gjAVd784WqE

[^1_66]: https://ijsrem.com/download/enterprise-ai-transformation-with-google-vertex-ai-best-practices-strategies/

[^1_67]: https://ojs.aaai.org/index.php/AAAI/article/view/30347

[^1_68]: https://fepbl.com/index.php/ijmer/article/view/1206

[^1_69]: https://onepetro.org/SPEMEOS/proceedings/23MEOS/23MEOS/D031S114R007/517265

[^1_70]: https://journals.uran.ua/tarp/article/view/285749

[^1_71]: https://journals.bilpubgroup.com/index.php/jaeser/article/view/5362

[^1_72]: https://www.reddit.com/r/googlecloud/comments/1fzna0y/does_anyone_have_tips_on_cost_efficient_ways_of/

[^1_73]: https://cloud.google.com/vertex-ai

[^1_74]: https://topqlearn.com/google-vertex-ai-tutorial-and-overview

[^1_75]: https://codelabs.developers.google.com/vertex-p2p-training

[^1_76]: https://www.tandfonline.com/doi/full/10.1080/03736245.2024.2341660

[^1_77]: https://www.mdpi.com/2072-4292/14/22/5672

[^1_78]: https://journal.hmjournals.com/index.php/JCFMBS/article/view/896

[^1_79]: https://ieeexplore.ieee.org/document/10112056/

[^1_80]: https://www.semanticscholar.org/paper/f8f91872cbf23d72a4111a4659cfdc9300408c61

[^1_81]: https://www.semanticscholar.org/paper/d0e9c7ea3817210c3a009c65b243e4dd0b0cfdbb

[^1_82]: https://journal.stemfellowship.org/doi/10.17975/sfj-2024-004

[^1_83]: https://www.semanticscholar.org/paper/f8e1c1602a6f95d431e1c5662d68029e7358f912

[^1_84]: https://console.cloud.google.com/vertex-ai/publishers/meta/model-garden/llama3_1?inv=1\&invt=Abi2vg

[^1_85]: https://ai-rockstars.com/google-gemini-vertex-ai/

[^1_86]: https://www.ssrn.com/abstract=4998534

[^1_87]: https://ijsser.org/2024files/ijsser_09__287.pdf

[^1_88]: https://www.ewadirect.com/proceedings/tns/article/view/16426

[^1_89]: https://www.googlecloudcommunity.com/gc/AI-ML/Confused-about-pricing-differences-between-Vertex-AI-and-Google/m-p/886021

[^1_90]: https://www.semanticscholar.org/paper/7d53b2e231b52d7729bb47f790ff2da4c25edabb

[^1_91]: https://ieeexplore.ieee.org/document/9761287/

[^1_92]: https://ieeexplore.ieee.org/document/10198237/

[^1_93]: https://www.sciendo.com/article/10.2478/cait-2025-0004

[^1_94]: https://www.googlecloudcommunity.com/gc/AI-ML/Accessing-Anthropic-vertex-ai-using-service-account/m-p/890908/highlight/true

[^1_95]: https://journals.bilpubgroup.com/index.php/jaeser/article/view/5408

[^1_96]: https://www.degruyterbrill.com/document/doi/10.1515/9783110337419-017/html

[^1_97]: https://ieeexplore.ieee.org/document/11011960/

[^1_98]: https://www.tandfonline.com/doi/full/10.1080/10402381.2018.1514549

[^1_99]: https://www.googlecloudcommunity.com/gc/AI-ML/Need-to-Stop-VertexAI-Services/m-p/786568

