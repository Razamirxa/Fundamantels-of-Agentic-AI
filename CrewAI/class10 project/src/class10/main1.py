from  crewai.flow.flow import Flow, start,listen
from litellm import completion
import time
import os

API_KEY ="AIzaSyBsNFkNa4T4ljaRin1KKz3XGXeljfUCHzg"
class CityFunFact(Flow):

    @start()
    def genrate_rondom_city(self):
        result = completion(
            model="gemini/gemini-1.5-pro",
            api_key=API_KEY,
            messages= [{"content":"Give me a random city name from pakistan","role":"user"}]
        )
        city= result['choices'][0]['message']['content']
        print(city)
        return city

    @listen(genrate_rondom_city)
    def genrate_fun_fact(self,city_name):
        result = completion(
            model="gemini/gemini-1.5-pro",
            api_key=API_KEY,
            messages= [{"content":f"Write some fun fact about{city_name}","role":"user"}]
        )
        fun_fact =result['choices'][0]['message']['content']
        print(fun_fact)
        self.state['fun_fact']=fun_fact

    @listen(genrate_fun_fact)
    def save_fun_fact(self):
            with open("Fun_fact.md", "w") as file:
                file.write(self.state['fun_fact'])
                return self.state['fun_fact']
        



def kickoff():
    obj = CityFunFact()
    result = obj.kickoff()
    print(result)