from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


@CrewBase
class DevCrew:
    """DEV Crew"""


    @agent
    def junior_python_developer(self) -> Agent:
        return Agent(
            role="junior python developer",
            goal="write python code without type hints that meets project requirements'{problem}'",
            backstory="You have python web development experience and are looking to expand your skills in a new environment"
        )
    
    @agent
    def senior_python_developer(self) -> Agent:
        return Agent(
            role="Senior python developer",
            goal="""rewiew the python code written by junior developers and provide feedback for this problem '{problem}'apply type hints to the code and refactor it to meet project requirements apply pydocs write 3 pytest test for the code""",
            backstory=""""You have 10 years of experience in python web development and are looking to mentor junior developers"""
            
        )


    @task
    def write_code(self) -> Task:
        return Task(
            description="you have to write a python code without type hints that meets project requirements for this problem '{problem}'",
            expected_output="return python code only",
            agent=self.junior_python_developer()
            
        )
    
    @task
    def rewiew_code(self) -> Task:
        return Task(
            description="""you have to rewiew the python code written by junior developers and provide feedback for this problem '{problem}'
            apply type hints to the code and refactor it to meet project requirements
            apply pydocs
            write 3 pytest test for the code""",
            expected_output="return python code only",
            agent=self.senior_python_developer()
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Research Crew"""


        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
