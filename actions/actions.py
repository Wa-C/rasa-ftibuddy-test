# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import csv

class ActionEmmaCheckFitness(Action):
     def name(self) -> Text:
         return "action_emma_check_fitness"


     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="Sure, Emma! Let me check your fitness progress. Give me a moment.")
         dispatcher.utter_message(text="Your Fitness level is fine. Keep going. Dont forget to drink water ")
         

         return []
     
class ActionEmmaCreateWorkoutPlan(Action):
     def name(self) -> Text:
         return "action_emma_create_workout_plan"


     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="How about these: Yoga and Jogging ")
         
         

         return []   
       
class ActionRajCheckFitness(Action):
     def name(self) -> Text:
         return "action_raj_check_fitness"


     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="Sure, Raj! Let me check your fitness progress. Give me a moment.")
         dispatcher.utter_message(text="Your Fitness level is fine. Keep going. Dont forget to drink water ")
         

         return []     

class ActionRajCreateWorkoutPlan(Action):
     def name(self) -> Text:
         return "action_raj_create_workout_plan"


     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="How about these: Jogging and Gym ")
        
         return []

class ActionRajFindGymsNearMe(Action):
     def name(self) -> Text:
         return "action_raj_find_gyms_near_me"


     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="How about this one? FitBuddy Gym. 500 meter from your loaction ")
        
         return []   
     
class ActionLinaCheckFitness(Action):
     def name(self) -> Text:
         return "action_lina_check_fitness"


     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="Lina, I'm on it! Checking your workout results now.")
         dispatcher.utter_message(text="Your Fitness level is fine. Keep going. Dont forget to drink water ")
         

         return []   
     
class ActionLinaCreateWorkoutPlan(Action):
     def name(self) -> Text:
         return "action_lina_create_workout_plan"


     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="How about these: Jogging, Gym and Yoga? ")
        
         return []           
     
class ActionLinaFindGymsNearMe(Action):
     def name(self) -> Text:
         return "action_lina_find_gyms_near_me"


     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="How about this one? FitBuddy Gym. 700 meter from your loaction ")
        
         return []      
     
class ActionEmmaGeneralInquery(Action):
     def name(self) -> Text:
         return "action_emma_general_inquiry"


     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("emma_general_inquiry")
         
        try:
            with open(r'C:\Users\wassi\OneDrive\Desktop\Winter Semester 23-24\Assistance System\WS23\Health_Fitness_Bot_for_International_students\y\actions\data.csv', 'r') as file: 
                reader = csv.DictReader(file)
                for row in reader:
                    if row ["name"] == name:
                        response_message = f"Found {name} about: {row['about']}"
                        dispatcher.utter_message(text=response_message)
                        return []
        except Exception as e: 
            print(f"Error: {e}")     

         
            dispatcher.utter_message(text=f"sorry couldnt found information in Database for {name}")
         

            return []     
class ActionRajGeneralInquery(Action):
     def name(self) -> Text:
         return "action_raj_general_inquiry"


     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("raj_general_inquiry")
         
        try:
            with open(r'C:\Users\wassi\OneDrive\Desktop\Winter Semester 23-24\Assistance System\WS23\Health_Fitness_Bot_for_International_students\y\actions\data.csv', 'r') as file: 
                reader = csv.DictReader(file)
                for row in reader:
                    if row ["name"] == name:
                        response_message = f"Found {name} about: {row['about']}"
                        dispatcher.utter_message(text=response_message)
                        return []
        except Exception as e: 
            print(f"Error: {e}")     

         
            dispatcher.utter_message(text=f"sorry couldnt found information in Database for {name}")
         

            return []         
class ActionLinaGeneralInquery(Action):
     def name(self) -> Text:
         return "action_lina_general_inquiry"


     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("lina_general_inquiry")
         
        try:
            with open(r'C:\Users\wassi\OneDrive\Desktop\Winter Semester 23-24\Assistance System\WS23\Health_Fitness_Bot_for_International_students\y\actions\data.csv', 'r') as file: 
                reader = csv.DictReader(file)
                for row in reader:
                    if row ["name"] == name:
                        response_message = f"Found {name} about: {row['about']}"
                        dispatcher.utter_message(text=response_message)
                        return []
        except Exception as e: 
            print(f"Error: {e}")     

         
            dispatcher.utter_message(text=f"sorry couldnt found information in Database for {name}")
         

            return []         