from crewai import Crew,Process
from agents import news_retriever_agent,news_analyzer_agent,news_formatter_agent
from tasks import news_retrieve_task,news_analyzer_task,news_formatting_task
import os
from dotenv import load_dotenv

load_dotenv()

crew = Crew(
    tasks=[news_retrieve_task, news_analyzer_task, news_formatting_task],
    agents=[news_retriever_agent, news_analyzer_agent, news_formatter_agent],
    memory = True,
    verbose=True,
)

output = crew.kickoff()