from crewai import Agent, LLM
import datetime
from search_tool import SerperDevTool
import os

os.getenv("SERPER_API_KEY")
os.getenv("NVIDIA_NIM_API_KEY")


serper_tool = SerperDevTool(n_results=20)

news_retriever_agent = Agent(
        role = "web information retrieval",
        goal = f"retrieve latest advancements in the field of AI in this week.The current time is {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        backstory = "You are expert in web information retrieval and you have been tasked to retrieve the latest advancements in the field of AI in the week.",
        tools=[serper_tool],
        verbose = True,
        llm = LLM("nvidia_nim/meta/llama-3.3-70b-instruct",temperature=0.1)
)

news_analyzer_agent = Agent(
    goal = "analyze the retrieved news and make sure you utilise only those related to AI latest trends and advancements",
    role = "retrieved news analyzer",
    backstory= "You are expert in news analysis and you have been tasked to analyze the retrieved news and make sure you utilise only those related to AI latest trends and advancements.",
    verbose=True,
    llm = LLM("nvidia_nim/meta/llama-3.3-70b-instruct",temperature=0.1)
)


news_formatter_agent = Agent(
    role = "news formatter",
    goal = "format the news in readable and visually appealing format with icons,images and neat alignment and utilising right font properties to design a newsletter",
    backstory = "You are expert in news formatting and have vast experience in formatting,you have been tasked to format the news in readable and visually appealing format with icons,images and neat alignment and utilising right font properties to design a newsletter.",
    verbose = True,
    llm = LLM("nvidia_nim/meta/llama-3.3-70b-instruct",temperature=0.1)
)
