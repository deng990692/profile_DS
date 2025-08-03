import streamlit as st

# --- 设置页面配置 ---
st.set_page_config(page_title="DS - 个人简历", page_icon="👋")

# --- 样式调整 (可选，让页面更美观) ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f2f6; /* 轻微的背景色 */
        color: #333333; /* 主要文字颜色 */
    }
    .st-emotion-cache-zt5ig8 { /* 调整主内容区域宽度 */
        max-width: 800px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    h1 {
        color: #004d40; /* 标题颜色 */
        font-size: 3em;
        margin-bottom: 0.5em;
    }
    h2 {
        color: #00796b; /* 副标题颜色 */
        font-size: 2em;
        border-bottom: 2px solid #00796b;
        padding-bottom: 0.3em;
        margin-top: 1.5em;
        margin-bottom: 1em;
    }
    h3 {
        color: #009688; /* 小标题颜色 */
        font-size: 1.5em;
        margin-top: 1.2em;
        margin-bottom: 0.8em;
    }
    p {
        line-height: 1.6;
        margin-bottom: 0.5em;
    }
    ul {
        margin-top: 0.5em;
        margin-bottom: 1em;
        padding-left: 20px;
    }
    ul li {
        margin-bottom: 0.3em;
    }
    .job-title {
        font-weight: bold;
        color: #00796b;
    }
    .project-title {
        font-weight: bold;
        color: #009688;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- 头部信息 ---
st.title("DS")
st.write("---")
st.markdown(f"""
    **出生日期:** 2000-01-02  |  **电话:** 135-xxxx-4994  |  **邮箱:** dengsh134@126.com
    **学历:** 本科 - 数据科学与大数据专业
    **求职意向:** AI应用工程师 / LLM工程化开发
""")
st.write("---")

# --- 技术技能 ---
st.header("技术技能")

st.subheader("AI工程化")
st.markdown("""
* **大模型应用:** Ollama本地部署 / Prompt / MCP / Dify工作流开发 / RAG优化 / LangChain
* **数据处理:** Python数据清洗 / ETL设计 / ECharts可视化 / 爬虫开发
""")

st.subheader("后端开发")
st.markdown("""
* **Java技术栈:** Spring Boot / MyBatis / MySQL / Oracle / Spring Cloud
* **架构能力:** RESTful API设计 / 高并发优化 / 数据库性能调优
* **其他:** Linux服务部署 / Crontab定时任务 / Docker基础
""")

st.write("---")

# --- 工作经历 ---
st.header("工作经历")
st.markdown("""
### XXXXX | 软件工程师 （2023.02 - 2025.03）
* 使用Spring Boot + MyBatis开发公司核心业务系统模块，负责需求分析、接口设计与数据库表结构设计，保障代码可维护性。
* 优化现有业务逻辑，解决慢查询问题，提升系统整体运行效率。
* 设计并实现符合规范的RESTful API，支持多终端数据交互需求。
* 主导历史项目的功能迭代与Bug修复，确保系统稳定运行。
""")
st.write("---")

# --- 项目经历 ---
st.header("项目经历")

st.markdown("""
### 1. AI智能数据分析助手
* **技术组合:** Dify + Ollama + DeepSeek + RAG + ECharts
* **突破性设计:**
    * 创新性融合知识库中表结构动态生成SQL与NLP意图识别，实现自然语言→SQL的精准转换。
    * 部署数据库查询本地MCP，并可将获取数据以图表形式统计展示。
    * 多轮上下文对话记忆，可实现对话式提问查询数据与展现统计图表。
* **成果:** 降低非技术团队数据查询门槛，实现业务人员自助式多轮提问式数据分析。
    <br> (项目地址占位，请在此处替换为实际链接或描述)
""")

st.markdown("""
### 2. 晨报自动化系统
* **技术组合:** Dify + Qwen + Python爬虫 + Notion
* **技术亮点:**
    * 多源爬虫(Python) + 大模型摘要(Llama3-8B) + TTS语音合成。
    * 通过Notion API实现文字和语音版双通道发布，实现在线访问。
    * 基于Linux Crontab实现无人值守运行。
    * 设置失败重试机制（最大3次），异常自动邮件通知。
* **成果:** 实现100%自动化日报生成，单次处理时间缩短至1分钟内。
    <br> (项目地址占位，请在此处替换为实际链接或描述)
""")
st.write("---")

# --- 自我评价 ---
st.header("自我评价")
st.markdown("""
* **扎实的后端开发能力**，熟悉企业级应用开发全流程，具备良好的技术迁移能力。
* 具备**主动学习意识**，热爱AI技术，持续研究AI应用方向技术与框架并进行实践与尝试。
* **良好的团队协作能力**，能高效对接产品、测试与前端团队，推动项目落地。
""")

st.write("---")
st.caption("祝您求职顺利！")
