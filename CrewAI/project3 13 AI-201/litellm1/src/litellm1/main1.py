from crewai.flow import Flow ,start ,listen
from litellm import completion

class LitellmFlow(Flow):

    @start()
    def start_funtion(self):
        output = completion(
            model="gemini/gemini-1.5-flash",
            messages=[
            {
                'role':'user',
                'content':'who is the founder of pakistan',
            }
        ])
        return output ['choices'][0]['message']['content']

def run_litellm_flow():
    flow = LitellmFlow()
    result= flow.kickoff()
    print(result)