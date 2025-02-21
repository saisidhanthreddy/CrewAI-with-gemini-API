from crewai import Agent, LLM
from tools import tool
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get the Google API key
google_api_key = os.getenv("GEMINI_API_KEY")

# Ensure the API key is set in the environment for LiteLLM (optional redundancy)
os.environ["GEMINI_API_KEY"] = google_api_key

# Define the LLM using CrewAI's LLM class
llm = LLM(
    model="gemini/gemini-1.5-flash",  # Use the exact model from CrewAI docs
    api_key=google_api_key,                 # Pass the API key directly
    temperature=0.5                         # Set your desired temperature
)

# Creating a senior researcher agent with memory and verbose mode
news_researcher = Agent(
    role="Senior Researcher",
    goal='Uncover groundbreaking technologies in {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of "
        "innovation, eager to explore and share knowledge that could change "
        "the world."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

# Creating a writer agent with custom tools responsible for writing news blog
news_writer = Agent(
    role='Writer',
    goal='Narrate compelling tech stories about {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft "
        "engaging narratives that captivate and educate, bringing new "
        "discoveries to light in an accessible manner."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)