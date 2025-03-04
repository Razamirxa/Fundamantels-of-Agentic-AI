from  crewai.flow.flow import Flow, start,listen
import time

class SimpleFlow(Flow):
    @start()
    def function1(self):
        print('step 1')
        time.sleep(3)
    @listen(function1)
    def function2(self):
        print('step 2')
        time.sleep(3)
    @listen(function2)
    def function3(self):
        print('step 3')


def kickoff():
    obj = SimpleFlow()
    obj.kickoff()