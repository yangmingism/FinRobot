<div align="center">
<img align="center" width="30%" alt="image" src="https://github.com/AI4Finance-Foundation/FinGPT/assets/31713746/e0371951-1ce1-488e-aa25-0992dafcc139">
</div>

# FinRobot：一个基于大型语言模型的开源金融应用AI代理平台
[![下载量](https://static.pepy.tech/badge/finrobot)]([https://pepy.tech/project/finrobot](https://pepy.tech/project/finrobot))
[![每周下载量](https://static.pepy.tech/badge/finrobot/week)](https://pepy.tech/project/finrobot)
[![Python 3.8](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![PyPI](https://img.shields.io/pypi/v/finrobot.svg)](https://pypi.org/project/finrobot/)
![许可证](https://img.shields.io/github/license/AI4Finance-Foundation/finrobot.svg?color=brightgreen)
![](https://img.shields.io/github/issues-raw/AI4Finance-Foundation/finrobot?label=问题)
![](https://img.shields.io/github/issues-closed-raw/AI4Finance-Foundation/finrobot?label=已关闭的问题)
![](https://img.shields.io/github/issues-pr-raw/AI4Finance-Foundation/finrobot?label=开放的PR)
![](https://img.shields.io/github/issues-pr-closed-raw/AI4Finance-Foundation/finrobot?label=已关闭的PR)




<div align="center">
<img align="center" src=figs/logo_white_background.jpg width="40%"/>
</div>

**FinRobot** 是一个超越 FinGPT 范围的 AI 代理平台，它是一个为金融应用精心设计的综合解决方案。它集成了**各种各样的 AI 技术**，不仅仅局限于语言模型。这种扩展的愿景突出了该平台的多功能性和适应性，能够满足金融行业的各种需求。

**AI 代理的概念**: AI 代理是一种智能实体，它使用大型语言模型作为其大脑来感知其环境、做出决策并执行操作。与传统的 AI 不同，AI 代理能够独立思考并利用工具逐步实现既定目标。

[FinRobot 白皮书](https://arxiv.org/abs/2405.14767)

[![](https://dcbadge.vercel.app/api/server/trsr8SXpW5)](https://discord.gg/trsr8SXpW5)

![访问量](https://api.visitorbadge.io/api/VisitorHit?user=AI4Finance-Foundation&repo=FinRobot&countColor=%23B17A)


## FinRobot 生态系统
<div align="center">
<img align="center" src="https://github.com/AI4Finance-Foundation/FinRobot/assets/31713746/6b30d9c1-35e5-4d36-a138-7e2769718f62" width="90%"/>
</div>

### FinRobot 的整体框架分为四个不同的层级，每个层级都旨在解决金融 AI 处理和应用的特定方面：
1. **金融 AI 代理层**: 金融 AI 代理层现在包括金融思维链 (CoT) 提示，增强了复杂分析和决策能力。市场预测代理、文档分析代理和交易策略代理利用 CoT 将金融挑战分解成逻辑步骤，将其先进的算法和领域专业知识与不断变化的金融市场动态相结合，以获得精确、可操作的见解。
2. **金融 LLM 算法层**: 金融 LLM 算法层配置和使用专门针对特定领域和全球市场分析定制的模型。
3. **LLMOps 和 DataOps 层**: LLMOps 层实施多源集成策略，为特定的金融任务选择最合适的 LLM，利用一系列最先进的模型。
4. **多源 LLM 基础模型层**: 此基础层支持各种通用和专业 LLM 的即插即用功能。


## FinRobot：代理工作流程
<div align="center">
<img align="center" src="https://github.com/AI4Finance-Foundation/FinRobot/assets/31713746/ff8033be-2326-424a-ac11-17e2c9c4983d" width="60%"/>
</div>

1. **感知**: 此模块使用复杂的技巧来捕获和解释来自市场数据馈送、新闻和经济指标的多模态金融数据，将数据结构化以进行彻底的分析。

2. **大脑**: 充当核心处理单元，此模块使用 LLM 感知来自感知模块的数据，并利用金融思维链 (CoT) 流程生成结构化指令。

3. **行动**: 此模块执行来自大脑模块的指令，应用工具将分析见解转化为可操作的结果。行动包括交易、投资组合调整、生成报告或发送警报，从而积极影响金融环境。

## FinRobot：智能调度器
<div align="center">
<img align="center" src="https://github.com/AI4Finance-Foundation/FinRobot/assets/31713746/06fa0b78-ac53-48d3-8a6e-98d15386327e" width="60%"/>
</div>

智能调度器对于确保模型多样性以及优化最合适的 LLM 的集成和选择至关重要。
* **主管代理**: 此组件协调任务分配过程，确保根据代理的性能指标和对特定任务的适用性将任务分配给代理。
* **代理注册**: 管理代理在系统中的注册和跟踪可用性，促进高效的任务分配流程。
* **代理适配器**: 将代理功能调整为特定任务，增强其在整个系统中的性能和集成。
* **任务管理器**: 管理和存储针对各种金融任务量身定制的不同通用和微调的基于 LLM 的代理，并定期更新以确保相关性和有效性。

## 文件结构

主文件夹 **finrobot** 有三个子文件夹 **agents、data_source、functional**。

```
FinRobot
├── finrobot (主文件夹)
│   ├── agents
│   	├── agent_library.py
│   	└── workflow.py
│   ├── data_source
│   	├── finnhub_utils.py
│   	├── finnlp_utils.py
│   	├── fmp_utils.py
│   	├── sec_utils.py
│   	└── yfinance_utils.py
│   ├── functional
│   	├── analyzer.py
│   	├── charting.py
│   	├── coding.py
│   	├── quantitative.py
│   	├── reportlab.py
│   	└── text.py
│   ├── toolkits.py
│   └── utils.py
│
├── configs
├── experiments
├── tutorials_beginner (上手教程)
│   ├── agent_fingpt_forecaster.ipynb
│   └── agent_annual_report.ipynb 
├── tutorials_advanced (潜在 FinRobot 开发人员的高级教程)
│   ├── agent_trade_strategist.ipynb
│   ├── agent_fingpt_forecaster.ipynb
│   ├── agent_annual_report.ipynb 
│   ├── lmm_agent_mplfinance.ipynb
│   └── lmm_agent_opt_smacross.ipynb
├── setup.py
├── OAI_CONFIG_LIST_sample
├── config_api_keys_sample
├── requirements.txt
└── README.md
```

## 安装：

**1.（推荐）创建一个新的虚拟环境**
```shell
conda create --name finrobot python=3.10
conda activate finrobot
```
**2. 使用终端下载 FinRobot 存储库或手动下载**
```shell
git clone https://github.com/AI4Finance-Foundation/FinRobot.git
cd FinRobot
```
**3. 从源代码或 pypi 安装 finrobot 和依赖项**

从 pypi 获取我们的最新版本
```bash
pip install -U finrobot
```
或直接从此存储库安装
```
pip install -e .
```
**4. 修改 OAI_CONFIG_LIST_sample 文件**
```shell
1) 将 OAI_CONFIG_LIST_sample 重命名为 OAI_CONFIG_LIST
2) 删除 OAI_CONFIG_LIST 文件中的四行注释
3) 添加您自己的 OpenAI api-key <您的 OpenAI API 密钥>
```
**5. 修改 config_api_keys_sample 文件**
```shell
1) 将 config_api_keys_sample 重命名为 config_api_keys
2) 删除 config_api_keys 文件中的注释
3) 添加您自己的 finnhub-api “YOUR_FINNHUB_API_KEY”
4) 添加您自己的 financialmodelingprep 和 sec-api 密钥“YOUR_FMP_API_KEY”和“YOUR_SEC_API_KEY”（用于生成财务报告）
```
**6. 开始浏览以下教程或演示：**
```
# 在教程中找到这些笔记本
1) agent_annual_report.ipynb
2) agent_fingpt_forecaster.ipynb
3) agent_trade_strategist.ipynb
4) lmm_agent_mplfinance.ipynb
5) lmm_agent_opt_smacross.ipynb
```

## 演示
### 1. 市场预测代理（预测股票走势方向）
以公司的股票代码、最近的基本财务数据和市场新闻作为输入，并预测其股票走势。

1. 导入
```python
import autogen
from finrobot.utils import get_current_date, register_keys_from_json
from finrobot.agents.workflow import SingleAssistant
```
2. 配置
```python
# 从 JSON 文件读取 OpenAI API 密钥
llm_config = {
    "config_list": autogen.config_list_from_json(
        "../OAI_CONFIG_LIST",
        filter_dict={"model": ["gpt-4-0125-preview"]},
    ),
    "timeout": 120,
    "temperature": 0,
}

# 注册 FINNHUB API 密钥
register_keys_from_json("../config_api_keys")
```
3. 运行
```python
company = "NVDA"

assitant = SingleAssistant(
    "Market_Analyst",
    llm_config,
    # 如果您希望聊天而不是简单地接收预测，则设置为“ALWAYS”
    human_input_mode="NEVER",
)
assitant.chat(
    f"使用所有提供的工具检索在 {get_current_date()} 可用的关于 {company} 的信息。分别用 2-4 个最重要的因素分析 {company} 的积极发展和潜在问题，并使它们简洁明了。大多数因素应从与公司相关的新闻中推断出来。 "
    f"然后对下周 {company} 的股价走势做出粗略的预测（例如，上涨/下跌 2-3%）。提供一份摘要分析来支持您的预测。"
)
```
4. 结果
<div align="center">
<img align="center" src="https://github.com/AI4Finance-Foundation/FinRobot/assets/31713746/812ec23a-9cb3-4fad-b716-78533ddcd9dc" width="40%"/>
<img align="center" src="https://github.com/AI4Finance-Foundation/FinRobot/assets/31713746/9a2f9f48-b0e1-489c-8679-9a4c530f313c" width="41%"/>
</div>

### 2. 用于报告写作的财务分析师代理（股票研究报告）
以公司的 10-k 表格、财务数据和市场数据作为输入，并输出股票研究报告

1. 导入 
```python
import os
import autogen
from textwrap import dedent
from finrobot.utils import register_keys_from_json
from finrobot.agents.workflow import SingleAssistantShadow
```
2. 配置
```python
llm_config = {
    "config_list": autogen.config_list_from_json(
        "../OAI_CONFIG_LIST",
        filter_dict={
            "model": ["gpt-4-0125-preview"],
        },
    ),
    "timeout": 120,
    "temperature": 0.5,
}
register_keys_from_json("../config_api_keys")

# 中间策略模块将保存在此目录中
work_dir = "../report"
os.makedirs(work_dir, exist_ok=True)

assistant = SingleAssistantShadow(
    "Expert_Investor",
    llm_config,
    max_consecutive_auto_reply=None,
    human_input_mode="TERMINATE",
)

```
3. 运行
```python
company = "Microsoft"
fyear = "2023"

message = dedent(
    f"""
    使用您提供的工具，根据 {company} 的 {fyear} 年 10-k 报告编写一份年度报告，并将其格式化为 pdf。
    请注意以下事项：
    - 在开始之前明确解释您的工作计划。
    - 为清楚起见，逐一使用工具，尤其是在寻求指示时。
    - 所有文件操作都应在“{work_dir}”中完成。
    - 生成图像后在聊天中显示。
    - 所有段落应结合 400 到 450 个单词，在明确满足此要求之前不要生成 pdf。
"""
)

assistant.chat(message, use_cache=True, max_turns=50,
               summary_method="last_msg")
```
4. 结果
<div align="center">
<img align="center" src="https://github.com/AI4Finance-Foundation/FinRobot/assets/31713746/d2d999e0-dc0e-4196-aca1-218f5fadcc5b" width="60%"/>
<img align="center" src="https://github.com/AI4Finance-Foundation/FinRobot/assets/31713746/3a21873f-9498-4d73-896b-3740bf6d116d" width="60%"/>
</div>

**金融 CoT**:
1. **收集初步数据**: 10-K 报告、市场数据、财务比率
2. **分析财务报表**: 资产负债表、损益表、现金流量表
3. **公司概况和业绩**: 公司描述、业务亮点、细分分析
4. **风险评估**: 评估风险
5. **财务绩效可视化**: 绘制市盈率和每股收益
6. **将调查结果综合成段落**: 将所有部分组合成一个连贯的摘要
7. **生成 PDF 报告**: 使用工具自动生成 PDF
8. **质量保证**: 检查字数


### 3. 具有多模态功能的交易策略代理


## AI 代理论文

+ [斯坦福大学 + 微软研究院] [代理 AI：调查多模态交互的视野](https://arxiv.org/abs/2401.03568)
+ [斯坦福大学] [生成式代理：人类行为的交互式模拟](https://arxiv.org/abs/2304.03442)
+ [复旦自然语言处理小组] [基于大型语言模型的代理的兴起和潜力：一项调查](https://arxiv.org/abs/2309.07864)
+ [复旦自然语言处理小组] [LLM-Agent-Paper-List](https://github.com/WooooDyy/LLM-Agent-Paper-List)
+ [清华大学] [大型语言模型赋能的基于代理的建模和仿真：调查与展望](https://arxiv.org/abs/2312.11970)
+ [人民大学] [关于基于大型语言模型的自主代理的调查](https://arxiv.org/pdf/2308.11432.pdf)
+ [南洋理工大学] [FinAgent：用于金融交易的多模态基础代理：工具增强、多样化和通才](https://arxiv.org/abs/2402.18485)

## AI 代理博客和视频
+ [Medium] [AI 代理简介](https://medium.com/humansdotai/an-introduction-to-ai-agents-e8c4afd2ee8f)
+ [Medium] [揭开最佳 Character AI 聊天机器人的面纱 | 2024](https://medium.com/@aitrendorbit/unmasking-the-best-character-ai-chatbots-2024-351de43792f4#the-best-character-ai-chatbots)
+ [big-picture] [ChatGPT，下一级：认识 10 个自主 AI 代理](https://blog.big-picture.com/en/chatgpt-next-level-meet-10-autonomous-ai-agents-auto-gpt-babyagi-agentgpt-microsoft-jarvis-chaosgpt-friends/)
+ [TowardsDataScience] [浏览 LLM 代理的世界：初学者指南](https://towardsdatascience.com/navigating-the-world-of-llm-agents-a-beginners-guide-3b8d499db7a9)
+ [YouTube] [介绍 Devin - “第一个” AI 代理软件工程师](https://www.youtube.com/watch?v=iVbN95ica_k)

## Citing FinRobot
```
@inproceedings{
zhou2024finrobot,
title={FinRobot: {AI} Agent for Equity Research and Valuation with Large Language Models},
author={Tianyu Zhou and Pinqiao Wang and Yilin Wu and Hongyang Yang},
booktitle={The 1st Workshop on Large Language Models and Generative AI for Finance},
year={2024}
}

@article{yang2024finrobot,
  title={FinRobot: An Open-Source AI Agent Platform for Financial Applications using Large Language Models},
  author={Yang, Hongyang and Zhang, Boyu and Wang, Neng and Guo, Cheng and Zhang, Xiaoli and Lin, Likun and Wang, Junlin and Zhou, Tianyu and Guan, Mao and Zhang, Runjia and others},
  journal={arXiv preprint arXiv:2405.14767},
  year={2024}
}
```
**Disclaimer**: The codes and documents provided herein are released under the Apache-2.0 license. They should not be construed as financial counsel or recommendations for live trading. It is imperative to exercise caution and consult with qualified financial professionals prior to any trading or investment actions.


## AI 代理开源框架和工具
+ [AutoGPT（163k 星）](https://github.com/Significant-Gravitas/AutoGPT) 是一款供所有人使用的工具，旨在使 AI 民主化，使其能够供所有人使用和构建。
+ [LangChain（87.4k 星）](https://github.com/langchain-ai/langchain) 是一个用于开发由语言模型驱动的上下文感知应用程序的框架，使它们能够连接到上下文源并依靠模型的推理能力来进行响应和操作。
+ [MetaGPT（41k 星）](https://github.com/geekan/MetaGPT) 是一个多代理开源框架，将不同的角色分配给 GPT，形成一个协作软件实体来执行复杂任务。
+ [dify（34.1.7k 星）](https://github.com/langgenius/dify) 是一个 LLM 应用程序开发平台。它集成了后端即服务和 LLMOps 的概念，涵盖了构建生成式 AI 原生应用程序所需的核心技术栈，包括内置的 RAG 引擎
+ [AutoGen（27.4k 星）](https://github.com/microsoft/autogen) 是一个用于开发具有协作解决任务的对话代理的 LLM 应用程序的框架。这些代理是可定制的，支持人机交互，并以结合 LLM、人工输入和工具的模式运行。
+ [ChatDev（24.1k 星）](https://github.com/OpenBMB/ChatDev) 是一个专注于开发能够进行对话和问答的对话式 AI 代理的框架。它提供了一系列预训练模型和交互式界面，方便用户开发自定义聊天代理。
+ [BabyAGI（19.5k 星）](https://github.com/yoheinakajima/babyagi) 是一个 AI 驱动的任务管理系统，致力于构建具有初步通用智能的 AI 代理。
+ [CrewAI（16k 星）](https://github.com/joaomdmoura/crewAI) 是一个用于协调角色扮演、自主 AI 代理的框架。通过培养协作智能，CrewAI 使代理能够无缝协同工作，解决复杂的任务。
+ [SuperAGI（14.8k 星）](https://github.com/TransformerOptimus/SuperAGI) 是一个面向开发人员的开源自主 AI 代理框架，使开发人员能够构建、管理和运行有用的自主代理。
+ [FastGPT（14.6k 星）](https://github.com/labring/FastGPT) 是一个基于 LLM 构建的知识库平台，提供开箱即用的数据处理和模型调用能力，允许通过流程可视化进行工作流编排。
+ [XAgent（7.8k 星）](https://github.com/OpenBMB/XAgent) 是一种开源实验性大型语言模型 (LLM) 驱动的自主代理，可以自动解决各种任务。
+ [Bisheng（7.8k 星）](https://github.com/dataelement/bisheng) 是一个领先的开发 LLM 应用程序的开源平台。
+ [Voyager（5.3k 星）](https://github.com/OpenBMB/XAgent) 一个具有大型语言模型的开放式具身代理。
+ [CAMEL（4.7k 星）](https://github.com/camel-ai/camel) 是一个提供构建多模态 AI 代理的综合工具和算法集的框架，使它们能够处理各种数据形式，例如文本、图像和语音。
+ [Langfuse（4.3k 星）](https://github.com/langfuse/langfuse) 是一个语言融合框架，可以整合多个 AI 代理的语言能力，使它们能够同时拥有多语言理解和生成能力。

**免责声明**: 本文中提供的代码和文档是在 Apache-2.0 许可下发布的。它们不应被解释为财务建议或实时交易的建议。在进行任何交易或投资行动之前，务必谨慎行事并咨询合格的财务专业人士。


希望以上翻译对您有所帮助！如果您有任何其他问题，请随时提问。 
