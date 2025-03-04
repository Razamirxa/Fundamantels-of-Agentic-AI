from crewai import Agent, Task, Crew, Process, LLM
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource
import os

# Get the GEMINI API key
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# Create a knowledge source
content = "Users name is Raza UL Mustafa. He is 30 years old and lives in Lahore Pakistan."
string_source = StringKnowledgeSource(
    content=content,
)

# Create an LLM with a temperature of 0 to ensure deterministic outputs
gemini_llm = LLM(
    model="gemini/gemini-1.5-flash",
    api_key=GEMINI_API_KEY,
    temperature=0,
)

# Create an agent with the knowledge store
agent = Agent(
    role="About User",
    goal="You know everything about the user.",
    backstory="""You are a master at understanding people and their preferences.""",
    verbose=True,
    allow_delegation=False,
    llm=gemini_llm,
    embedder={
        "provider": "google",
        "config": {
            "model": "models/text-embedding-004",
            "api_key": GEMINI_API_KEY,
        }
    }
)

task = Task(
    description="Answer the following questions about the user: {question}",
    expected_output="An answer to the question.",
    agent=agent,
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=True,
    process=Process.sequential,
    knowledge_sources=[string_source],
    embedder={
        "provider": "google",
        "config": {
            "model": "models/text-embedding-004",
            "api_key": GEMINI_API_KEY,
        }
    }
)
def test_knowledge_rag():
    result = crew.kickoff(inputs={"question": "What city does Raza live in and how old is he?"})
    print(result)
