# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 18:27:23 2019

@author: Janani
"""

#chat bot
import numpy as np
import pandas as pd

user_template="User Message: {}"
bot_template="Bot Message: {}"

#respond function

def respond(message):
    return("I hear you said" + message)

def send(message):
    print(user_template.format(message))
    response=respond(message)
    print(bot_template.format(response))

send("Life is beautiful")