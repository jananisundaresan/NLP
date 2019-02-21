# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 18:27:23 2019

@author: Janani
"""


import random

User_template="User: {}"
Bot_template="Bot: {}"

weather=["sunny","windy","rainy","cloudy"]
Q_A={"What is your name?":["Hi, How can I be of help today","Hi!, This is Elsa. What can I help you with today?","My name is Elsa. I am your virtual Assistant.","I am Elsa. I am here to address your query","Elsa here. Kindly let me know what you want today."],
     "Not able to login":["I am sorry to hear that. Please give your ID","Give me your ID. I will lookinto what the issue is","Sorry for the trouble.It will be resolved soon"],
     "The server is down?":["Yes. Maintenance is going on","The network has issue"],
     "What is the weather today?":"it is {}".format(weather)}

def respond(message):
    if message in Q_A:
        return random.choice(Q_A[message])
    else:
        return "I am sorry. I do not understand your question"

def send(message):
    print(User_template.format(message))
    response=respond(message)
    print(Bot_template.format(response))
    
    
send("The server is down?")
send("How you doin?")
send("What is your name?")

    