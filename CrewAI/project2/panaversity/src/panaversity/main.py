from crewai.flow.flow import Flow, listen, start
from dotenv import load_dotenv, find_dotenv
from litellm import completion
import os
from crewai import Agent, Task, Crew

_: bool = load_dotenv(find_dotenv())
# API_KEY=os.getenv("GEMINI_API_KEY")


class PanaFlow(Flow):
    @start()
    def generate_topic(self):
        response = completion(
            model="gemini/gemini-1.5-flash",
            # api_key=API_KEY,
            messages=[
                {
                    "role": "user",
                    "content": "Generate a topic for a blog post about the benifits of learing Agentic AI."
                }
            ]
        )
        self.state['topic'] = response["choices"][0]["message"]["content"]
        print(f"Step 1 topic : {self.state['topic']}")

    
    @listen("generate_topic")
    def generate_content(self):
        #1. Create crew
        print("step 2:Generating content for the topic")
        
        # Create an agent
        sir_zia = Agent(
            role="Sir Zia",
            goal=f"You are a teacher who is teaching a class about {self.state['topic']}",
            backstory=f"You are SWE in a class. You will be today teaching a class about {self.state['topic']}"
        )
        
        # Create a task
        describe_topic = Task(
            description=f"We are mentoring to create best agentic Ai Engineers today wil teach a class about {self.state['topic']}",
            expected_output=f"The student will have mastered the topic of topic {self.state['topic']}",
            agent=sir_zia
        )
        
        # Create a crew
        crew = Crew(
            agents=[sir_zia],
            tasks=[describe_topic],
            verbose=True
        )
        
        # Run the crew
        result = crew.kickoff()
        print(result)


def kickoff():
    flow = PanaFlow()
    flow.kickoff()



