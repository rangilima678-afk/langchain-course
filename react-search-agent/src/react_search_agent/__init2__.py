from pathlib import Path
from dotenv import load_dotenv

# Path(__file__).resolve() gets the absolute path to this __init__.py file
# .parents[2] steps up 3 levels: react_search_agent -> src -> react-search-agent
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)

from langchain.agents import create_agent
# from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_tavily import TavilySearch
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

# Initialize Tavily search tool
tavily_tool = TavilySearch(max_results=3)

llm = ChatOpenAI(model="gpt-5")
tools = [tavily_tool]
agent = create_agent(model=llm, tools=tools)

def main() -> None:
    print("Hello from react-search-agent!")
    result = agent.invoke({
        "messages": HumanMessage(
            content="search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details"
        )
    })
    print(result)

if __name__ == "__main__":
    main()