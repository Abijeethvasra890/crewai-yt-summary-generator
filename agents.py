from crewai import Agent, LLM
from tools import yt_tool

# Configure the LLM
llm = LLM(
    api_key=None, 
    model="groq/llama3-8b-8192"
)

# Agent for summarizing video content
content_writer = Agent(
    role="Summary Generator",
    goal="Summarize compelling content from the video topic based on the {transcript}.",
    verbose=True,
    memory=True,
    backstory="Specializes in simplifying complex topics into concise summaries.",
   # tools=[yt_tool],
    llm=llm,
    allow_delegation=False,
)
