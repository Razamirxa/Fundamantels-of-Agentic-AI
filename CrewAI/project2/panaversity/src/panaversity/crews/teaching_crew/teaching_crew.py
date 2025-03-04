from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class TeachingCrew:
    @agent
    def sir_zia(self) -> Agent:
        return Agent(
            role="Sir Zia",
            goal="You are a teacher who is teaching a class about {topic}",
            backstory="You are SWE in a class. You will be today teaching a class about {topic}"
        )
        
    @task
    def describe_topic(self) -> Task:
        return Task(
            description="We are mentoring to create best agentic Ai Engineers today wil teach a class about {topic}",
            expected_output="The student will have mastered the topic of topic {topic}",
            agent=self.sir_zia
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.sir_zia],
            tasks=[self.describe_topic],
            verbose=True
        )