from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from config import config
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.tools.retriever import create_retriever_tool
from langchain import hub
from langchain.agents import create_openai_tools_agent
from langchain.agents.agent import AgentExecutor
import os


os.environ["OPENAI_API_KEY"] = config["api_key"]
llm = ChatOpenAI(temperature=0.0)


def get_full_web_text(link: str) -> str:
    loader = WebBaseLoader(link)
    doc = loader.load()
    text = doc[0].page_content
    while "\n\n\n" in text:
        text = text.replace("\n\n\n", "\n\n")
    return text


def get_chunks(text: str):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=50,
        length_function=len,
        is_separator_regex=False,
    )

    texts = text_splitter.create_documents([text])
    return texts


def create_bd(texts, save=False, search_type="similarity"):
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(texts, embeddings)
    if save:
        db.save_local("faiss_index")
    retriever = db.as_retriever(
        search_type=search_type,
    )
    return retriever


def create_agent(retriever, link_prompt=r"hwchase17/openai-tools-agent"):
    tool = create_retriever_tool(
        retriever,
        "search_web",
        "Searches and returns data from page"
    )
    tools = [tool]
    prompt = hub.pull(link_prompt)
    agent = create_openai_tools_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools)
    return agent_executor
