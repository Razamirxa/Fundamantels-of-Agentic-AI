from crewai.flow.flow import Flow, listen, start, router
import random

class RouterFlow(Flow):

    @start()  # Add parentheses here
    def greeting(self):
        print("Asslam o Alaikum")

    @router(greeting)
    def select_city(self):
        cities = ["karachi", "lahore", "islamabad"]
        selected_city = random.choice(cities)
        print(f"Selected City: {selected_city}")
        return selected_city  # Return the selected city name
    
    @listen(select_city)  # Listen for the output of select_city
    def city_fun_fact(self, city):
        print(f"Write some fun fact about the {city}")

def kickoff():
    obj = RouterFlow()
    obj.kickoff()

def plot():
    obj = RouterFlow()
    obj.plot()
