from crewai.flow import Flow, listen, start
from multiple_agents.crews.dev_crew.dev_crew import DevCrew



class DevFlow(Flow):


    @start()
    def run_dev_crew(self):
        output = DevCrew().crew().kickoff(
            inputs={
                "problem":"write python code to get the current date and time",
            }
        )
        return output.raw
    

def kickoff():
    dev_flow = DevFlow()
    result=dev_flow.kickoff()
    print(result)