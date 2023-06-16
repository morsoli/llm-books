## 一些资料汇总
> 原仓库[在这里](https://github.com/DSXiangLi/DecryptPromp)，摘取了其中我看过代码或者试用过的模型，对其他板块感兴趣的可以自行前往原仓库关注。

### 模型和数据

- [Berkley出品大模型排位赛榜有准中文榜单](https://lmsys.org/blog/2023-05-03-arena/): GPT4自然是稳居第一，GPT4>Claude>GPT3.5>Vicuna>others
- [Z-Bench中文真格基金评测](https://github.com/zhenbench/z-bench): 国产中文模型的编程可用性还相对较低，大家水平差不太多，两版ChatGLM提升明显
- [Open LLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard): 在Eleuther AI4个评估集上评估的LLM模型榜单
- [Chain-of-thought评估](https://github.com/FranxYao/chain-of-thought-hub):GSM8k, MATH等复杂问题排行榜

### 国外模型

| 模型链接                                                     | 模型描述                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [Google Bard](https://bard.google.com)                       | 谷歌bard虽迟但到，可以申请waitlist了                         |
| [Claude](https://www.anthropic.com/product)                  | ChatGPT最大竞争对手Claude也开放申请了，slack中无限试用       |
| [Falcon](https://huggingface.co/tiiuae/falcon-40b)           | Falcon由阿联酋技术研究所在超高质量1万亿Token上训练得到1B，7B，40B开源，免费商用！土豪们表示钱什么的格局小了 |
| [LLaMA](https://github.com/facebookresearch/llama)           | Meta开源指令微调LLM，规模70 亿到 650 亿不等                  |
| [MPT](https://huggingface.co/mosaicml/mpt-7b-chat)           | MosaicML开源的预训练+指令微调的新模型，可商用，支持84k tokens超长输入 |
| [RedPajama](https://huggingface.co/togethercomputer/RedPajama-INCITE-Instruct-3B-v1) | RedPajama项目既开源预训练数据后开源3B，7B的预训练+指令微调模型 |
| [ChatLLaMA](https://github.com/nebuly-ai/nebullvm/tree/main/apps/accelerate/chatllama) | 基于RLHF微调了LLaMA                                          |
| [Alpaca](https://github.com/tatsu-lab/stanford_alpaca)       | 斯坦福开源的使用52k数据在7B的LLaMA上微调得到，               |
| [Alpaca-lora](https://github.com/tloen/alpaca-lora)          | LORA微调的LLaMA                                              |
| [Dromedary](https://github.com/IBM/Dromedary)                | IBM self-aligned model with the LLaMA base                   |
| [Vicuna](https://github.com/lm-sys/FastChat)                 | Alpaca前成员等开源以LLama13B为基础使用ShareGPT指令微调的模型，提出了用GPT4来评测模型效果 |
| [koala](https://bair.berkeley.edu/blog/2023/04/03/koala/)    | 使用alpaca，HC3等开源指令集+ ShareGPT等ChatGPT数据微调llama，在榜单上排名较高 |
| [ColossalChat](https://github.com/hpcaitech/ColossalAI)      | HPC-AI Tech开源的Llama+RLHF微调                              |
| [MiniGPT4](https://github.com/Vision-CAIR/MiniGPT-4)         | Vicuna+BLIP2 文本视觉融合                                    |
| [StackLLama](https://huggingface.co/trl-lib/llama-7b-se-rl-peft) | LLama使用Stackexchange数据+SFT+RL                            |
| [Cerebras](https://huggingface.co/cerebras/Cerebras-GPT-13B) | Cerebras开源了1亿到130亿的7个模型，从预训练数据到参数全开源  |
| [PaLM-E](https://palm-e.github.io)                           | 谷歌多模态大模型，540B的PaLM语言模型和22B的ViT视觉模型相结合，得到562B的PaLM-E模型，在机器人应用场景有了新的突破 |
| [Dolly-v2](https://huggingface.co/databricks/dolly-v2-7b)    | 可商用 7b指令微调开源模型在GPT-J-6B上微调                    |
| [OpenChatKit](https://github.com/togethercomputer/OpenChatKit) | openai研究员打造GPT-NoX-20B微调+6B审核模型过滤               |
| [MetaLM](https://github.com/microsoft/unilm)                 | 微软开源的大规模自监督预训练模型                             |
| [Amazon Titan](https://aws.amazon.com/cn/bedrock/titan/)     | 亚马逊在aws上增加自家大模型                                  |
| [OPT-IML](https://link.zhihu.com/?target=https%3A//github.com/facebookresearch/metaseq/tree/main/projects/OPT) | Meta复刻GPT3，up to 175B, 不过效果并不及GPT3                 |
| [Bloom](https://huggingface.co/bigscience/bloom)             | BigScience出品，规模最大176B                                 |
| [BloomZ](https://huggingface.co/bigscience/bloomz)           | BigScience出品, 基于Bloom微调                                |
| [Galacia](https://github.com/paperswithcode/galai)           | 和Bloom相似，更针对科研领域训练的模型                        |
| [T0](https://github.com/bigscience-workshop/t-zero)          | BigScience出品，3B~11B的在T5进行指令微调的模型               |

### 国内模型

| 模型链接                                                     | 模型描述                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [ChatGLM](https://github.com/THUDM/ChatGLM-6B)               | 清华开源的、支持中英双语的对话语言模型，使用了代码训练，指令微调和RLHF。和以下GLM相同大小的130B的模型还在开发中。试用了下超出预期！ |
| [Moss](https://github.com/OpenLMLab/MOSS)                    | 为复旦正名！开源了预训练，指令微调的全部数据和模型。可商用   |
| [Wombat-7B](https://huggingface.co/GanjinZero/wombat-7b-delta) | 达摩院开源无需强化学习使用RRHF对齐的语言模型, alpaca基座     |
| [TigerBot](https://github.com/TigerResearch/TigerBot)        | 虎博开源了7B 180B的模型以及预训练和微调语料                  |
| [Chinese-LLaMA-Alpaca](https://github.com/ymcui/Chinese-LLaMA-Alpaca) | 哈工大中文指令微调的LLaMA                                    |
| [Luotuo](https://github.com/LC1332/Luotuo-Chinese-LLM)       | 中文指令微调的LLaMA，和ChatGLM                               |
| [文心一言](https://yiyan.baidu.com/welcome)                  | 已经拿到邀请码并试用，虽然人格化程度显著低，但效果上并没有很拉胯，国产YYDS！不过商业化霸王条款确实不少 |
| [通义千问](https://tongyi.aliyun.com/)                       | 阿里系LLM开放申请                                            |
| [星火](https://passport.xfyun.cn/login)                      | 科大讯飞星火，数学是真的厉害                                 |
| [Aquila](https://github.com/FlagAI-Open/FlagAI/tree/master/examples/Aquila) | 智源开源7B大模型可商用免费                                   |
| [Baichuan](https://github.com/baichuan-inc/baichuan-7B)      | 百川智能开源7B大模型可商用免费                               |
| [BiLLa](https://github.com/Neutralzz/BiLLa)                  | LLama词表扩充预训练+预训练和任务1比1混合SFT+指令样本SFT三阶段训练 |
| [Phoenix](https://github.com/FreedomIntelligence/LLMZoo)     | 港中文开源凤凰和奇美拉LLM，Bloom基座，40+语言支持            |
| [OpenBuddy](https://github.com/OpenBuddy/OpenBuddy)          | Llama 多语言对话微调模型                                     |
| [Guanaco](https://huggingface.co/KBlueLeaf/guanaco-7B-leh)   | LLama 7B基座，在alpaca52K数据上加入534K多语言指令数据微调    |
| [ziya](https://huggingface.co/IDEA-CCNL/Ziya-LLaMA-7B-Reward) | IDEA研究院在7B/13B llama上继续预训练+SFT+RM+PPO+HFTT+COHFT+RBRS |
| [Chinese Vincuna](https://github.com/Facico/Chinese-Vicuna)  | LLama 7B基座，使用Belle+Guanaco数据训练                      |
| [Linly](https://github.com/CVI-SZU/Linly)                    | Llama 7B基座，使用belle+guanaco+pclue+firefly+CSL+newscommentary等7个指令微调数据集训练 |
| [Firefly](https://github.com/yangjianxin1/Firefly)           | 中文2.6B模型，提升模型中文写作，古文能力，待开源全部训练代码，当前只有模型 |
| [Baize](https://github.com/project-baize/baize-chatbot)      | 使用100k self-chat对话数据微调的LLama                        |
| [BELLE](https://github.com/LianjiaTech/BELLE)                | 使用ChatGPT生成数据对开源模型进行中文优化                    |
| [Chatyuan](https://github.com/search?q=chatyuan&type=repositories) | chatgpt出来后最早的国内开源对话模型，T5架构是下面PromptCLUE的衍生模型 |
| [PromptCLUE](https://github.com/clue-ai/PromptCLUE)          | 多任务Prompt语言模型                                         |
| [PLUG](https://www.alice-mind.com/portal#/)                  | 阿里达摩院发布的大模型，提交申请会给下载链接                 |
| [CPM2.0](https://baai.ac.cn/)                                | 智源发布CPM2.0                                               |
| [GLM](https://github.com/THUDM/GLM-130B)                     | 清华发布的中英双语130B预训练模型                             |

### 垂直领域模型

| 模型链接                                                     | 模型描述                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|
| [ChatDoctor](https://github.com/Kent0n-Li/ChatDoctor)        | 110K真实医患对话样本+5KChatGPT生成数据进行指令微调           |
| [Huatuo](https://github.com/SCIR-HI/Huatuo-Llama-Med-Chinese) [Med-ChatGLM](https://github.com/SCIR-HI/Med-ChatGLM) | 医学知识图谱和chatgpt构建中文医学指令数据集+医学文献和chatgpt构建多轮问答数据 |
| [Chinese-vicuna-med](https://github.com/Facico/Chinese-Vicuna/blob/master/docs/performance-medical.md) | Chinese-vicuna在cMedQA2数据上微调                            |
| [OpenBioMed](https://github.com/BioFM/OpenBioMed)            | 清华AIR开源轻量版BioMedGPT, 知识图谱&20+生物研究领域多模态预训练模型 |
| [DoctorGLM](https://github.com/xionghonglin/DoctorGLM)       | ChatDoctor+MedDialog+CMD 多轮对话+单轮指令样本微调GLM        |
| [MedicalGPT-zh](https://github.com/MediaBrain-SJTU/MedicalGPT-zh) | 自建的医学数据库ChatGPT生成QA+16个情境下SELF构建情景对话     |
| [PMC-LLaMA](https://github.com/chaoyi-wu/PMC-LLaMA)          | 医疗论文微调Llama                                            |
| [ NHS-LLM](https://github.com/CogStack/OpenGPT/tree/main)    | Chatgpt生成的医疗问答，对话，微调模型                        |
| [LawGPT-zh](https://github.com/LiuHC0428/LAW-GPT)            | 利用ChatGPT清洗CrimeKgAssitant数据集得到52k单轮问答+我们根据中华人民共和国法律手册上最核心的9k法律条文，利用ChatGPT联想生成具体的情景问答+知识问答使用ChatGPT基于文本构建QA对 |
| [LawGPT](https://github.com/pengxiao-song/LaWGPT)            | 基于llama+扩充词表二次预训练+基于法律条款构建QA指令微调      |
| [Lawyer Llama](https://github.com/AndrewZhe/lawyer-llama)    | 法律指令微调数据集：咨询+法律考试+对话进行指令微调           |
| [LexiLaw](https://github.com/CSHaitao/LexiLaw)               | 法律指令微调数据集：问答+书籍概念解释，法条内容进行指令微调  |
| [FinChat.io](https://finchat.io/)                            | 使用最新的财务数据，电话会议记录，季度和年度报告，投资书籍等进行训练 |
| [OpenGPT](https://github.com/CogStack/OpenGPT)               | 领域LLM指令样本生成+微调框架                                 |
| [乾元BigBang金融2亿模型](https://github.com/ssymmetry/BBT-FinCUGE-Applications/tree/main) | 金融领域预训练+任务微调                                      |
| [度小满千亿金融大模型](https://huggingface.co/xyz-nlp/XuanYuan2.0) | 在Bloom-176B的基础上进行金融+中文预训练和微调                |                                                    |                                                      |

### 开源数据

| 数据类型       | 数据描述                                                     | 数据链接                                                     |
| -------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 指令微调       | self-instruct，GPT3自动生成&过滤得到指令集                   | https://github.com/yizhongw/self-instruct                    |
| 指令微调       | Standford Alpaca：52K text-davinci-003生成的self-instruct指令数据集 | https://github.com/tatsu-lab/stanford_alpaca                 |
| 指令微调       | GPT4-for-LLM 中文+英文+对比指令                              | https://github.com/Instruction-Tuning-with-GPT-4/GPT-4-LLM   |
| 指令微调       | GPTTeacher更多样的通用指令，角色扮演和代码指令               | https://github.com/teknium1/GPTeacher/tree/main              |
| 指令微调       | 中文翻译Alpaca还有一些其他指令数据集                         | https://github.com/hikariming/alpaca_chinese_dataset https://github.com/carbonz0/alpaca-chinese-dataset |
| 指令微调       | alpaca指令GPT4生成，和以上几版对比显著质量更高，回复更长     | https://github.com/Instruction-Tuning-with-GPT-4/GPT-4-LLM/tree/main |
| 指令微调       | Guanaco数据：对Alphca指令重写后以不同语言生成总共534K，有对话和非对话类型，还有补充的QA生成样本 | https://huggingface.co/datasets/JosephusCheung/GuanacoDataset |
| 指令微调       | OIG中文指令包括翻译alpaca+natural+unnatural，多轮对话，考试，leetcode指令 | https://github.com/BAAI-Zlab/COIG                            |
| 指令微调       | Vicuna训练使用的样本，用API获取了sharegpt上用户和chatgpt对话历史，部分网友整理到了HF | https://github.com/domeccleston/sharegpt https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered/tree/main |
| 指令微调       | HC3指令数据中英文，包括金融，开放QA，百科，DBQA，医学等包含人工回复 | https://huggingface.co/datasets/Hello-SimpleAI/HC3-Chinese/tree/main |
| 指令微调       | MOSS开源的SFT数据包含使用plugin的对话数据                    | https://huggingface.co/datasets/Hello-SimpleAI/HC3-Chinese/tree/main |
| 指令微调       | InstructWild数据：用四处爬取的chatgpt指令作为种子self-instruct扩充生成，中英双语 | https://github.com/XueFuzhao/InstructionWild/tree/main/data  |
| 指令微调       | BELLE100万指令数据，参考Alpaca用ChatGPT生成，有数学，多轮对话，校色对话等等 | https://github.com/LianjiaTech/BELLE                         |
| 指令微调       | PromptCLUE多任务提示数据集：模板构建，只包含标准NLP任务      | https://github.com/CLUEbenchmark/pCLUE                       |
| 指令微调       | TK-Instruct微调用的指令数据集, 全人工标注1600+NLP任务        | https://instructions.apps.allenai.org/                       |
| 指令微调       | T0微调用的指令数据集（P3）                                   | https://huggingface.co/datasets/bigscience/P3                |
| 指令微调       | p3衍生的46种多语言数据集（xmtf）                             | https://github.com/bigscience-workshop/xmtf                  |
| 指令微调       | Unnatural Instruction使用GPT3生成后改写得到240k              | https://github.com/orhonovich/unnatural-instructions         |
| 指令微调       | alpaca COT对多个数据源进行了清理并统一格式放到的了HF, 重点是人工整理的COT数据 | https://github.com/PhoebusSi/Alpaca-CoT                      |
| 指令微调       | 人工编写包含23种常见的中文NLP任务的指令数据，中文写作方向    | https://github.com/yangjianxin1/Firefly                      |
| 指令微调       | Amazon COT指令样本包括各类QA，bigbench，math等               | https://github.com/amazon-science/auto-cot                   |
| 指令微调       | CSL包含 396,209 篇中文核心期刊论文元信息 （标题、摘要、关键词、学科、门类）可做预训练可构建NLP指令任务 | https://github.com/ydli-ai/CSL                               |
| 指令微调       | alpaca code 20K代码指令数据                                  | https://github.com/sahil280114/codealpaca#data-release       |
| 指令微调       | GPT4Tools 71K GPT4指令样本                                   | https://github.com/StevenGrove/GPT4Tools                     |
| 指令微调       | GPT4指令+角色扮演+代码指令                                   | https://github.com/teknium1/GPTeacher                        |
| 数学           | 腾讯人工智能实验室发布网上爬取的数学问题APE210k              | https://github.com/Chenny0808/ape210k                        |
| 数学           | 猿辅导 AI Lab开源小学应用题Math23K                           | https://github.com/SCNU203/Math23k/tree/main                 |
| 数学           | grade school math把OpenAI的高中数学题有改造成指令样本有2-8步推理过程 | https://huggingface.co/datasets/qwedsacf/grade-school-math-instructions |
| 数学           | 数学问答数据集有推理过程和多项选择                           | https://huggingface.co/datasets/math_qa/viewer/default/test?row=2 |
| 数学           | AMC竞赛数学题                                                | https://huggingface.co/datasets/competition_math             |
| 数学           | 线性代数等纯数学计算题                                       | https://huggingface.co/datasets/math_dataset                 |
| 代码           | APPS从不同的开放访问编码网站Codeforces、Kattis 等收集的问题  | https://opendatalab.org.cn/APPS                              |
| 代码           | Lyra代码由带有嵌入式 SQL 的 Python 代码组成，经过仔细注释的数据库操作程序，配有中文评论和英文评论。 | https://opendatalab.org.cn/Lyra                              |
| 代码           | Conala来自StackOverflow问题,手动注释3k，英文                 | https://opendatalab.org.cn/CoNaLa/download                   |
| 代码           | code-alpaca ChatGPT生成20K代码指令样本                       | https://github.com/sahil280114/codealpaca.git                |
| 对话指令       | LAION 策划的开放指令通用数据集中手动选择的组件子集 已开源40M 3万个,100M在路上 | https://github.com/LAION-AI/Open-Instruction-Generalist      |
| 对话指令       | Baize基于Chat GPT构建的self-chat数据                         | https://github.com/project-baize/baize-chatbot/tree/main/data |
| 对话指令       | FaceBook开源BlenderBot训练对话数据~6K                        | https://huggingface.co/datasets/blended_skill_talk           |
| 对话指令       | AllenAI开源38.5万个对话高质量数据集SODA                      | https://realtoxicityprompts.apps.allenai.org/                |
| 对话指令       | InstructDial在单一对话任务类型上进行指令微调                 | https://github.com/prakharguptaz/Instructdial                |
| 对话指令       | Ultra Chat 两个独立的 ChatGPT Turbo API 进行对话，从而生成多轮对话数据 | https://github.com/thunlp/UltraChat                          |
| 对话指令       | Awesome Open-domain Dialogue Models提供多个开放域对话数据    | https://github.com/cingtiye/Awesome-Open-domain-Dialogue-Models#%E4%B8%AD%E6%96%87%E5%BC%80%E6%94%BE%E5%9F%9F%E5%AF%B9%E8%AF%9D%E6%95%B0%E6%8D%AE%E9%9B%86 |
| RLFH           | 北大河狸开源RLHF数据集10K，1M需要申请                        | https://huggingface.co/datasets/PKU-Alignment/PKU-SafeRLHF-10K |
| RLHF           | Anthropic hh-rlhf数据集                                      | https://huggingface.co/datasets/Anthropic/hh-rlhf            |
| RLHF           | Stack-exchange上问题对应多个答案，每个答案有打分             | https://huggingface.co/datasets/HuggingFaceH4/stack-exchange-preferences/tree/main |
| RLHF           | Facebook Bot Adversarial Dialogues数据集5K                   | https://github.com/facebookresearch/ParlAI                   |
| RLHF           | AllenAI Real Toxicity prompts                                | https://github.com/facebookresearch/ParlAI                   |
| RLHF           | OpenAssistant Conversations 160K消息，13500人工生成, 英文为主 | https://huggingface.co/datasets/OpenAssistant/oasst1         |
| 评估集         | BigBench(Beyond the Imitation Game Benchmark)                | https://github.com/google/BIG-bench                          |
| 评估集         | Complex QA：用于ChatGPT的评测指令集                          | https://github.com/tan92hl/Complex-Question-Answering-Evaluation-of-ChatGPT |
| 评估集         | Langchain开源评估数据集                                      | https://huggingface.co/LangChainDatasets                     |
| 评估集         | 2010-2022年全国高考卷的题目                                  | https://github.com/OpenLMLab/GAOKAO-Bench                    |
| 评估集         | 中文通用大模型综合性评测基准SuperCLUE                        | https://github.com/CLUEbenchmark/SuperCLUE                   |
| 预训练         | RedPajama开源的复刻llama的预训练数据集                       | https://github.com/togethercomputer/RedPajama-Data           |
| 预训练         | Pile 22个高质量数据集混合的预训练数据集800G,全量开放下载     | https://pile.eleuther.ai/                                    |
| 预训练         | UER整理CLUECorpusSmall+News Commentary中英                   | https://github.com/dbiir/UER-py/wiki/%E9%A2%84%E8%AE%AD%E7%BB%83%E6%95%B0%E6%8D%AE |
| 预训练         | 智源人工智能开源的wudao 200G预训练数据                       | [https://github.com/BAAI-WuDao/WuDaoMM](https://openi.pcl.ac.cn/BAAI/WuDao-Data) |
| 多源数据集整合 | opendatalab整合了预训练阶段的多个数据源                      | https://opendatalab.org.cn/?industry=9821&source=JUU3JTlGJUE1JUU0JUI5JThF |