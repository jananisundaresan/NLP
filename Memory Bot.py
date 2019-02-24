# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 10:22:55 2019

@author: Janani
"""

#check  chatbot memory

import re
import random

rules= {'I want (.*)': ['What would it mean if you got {0}',
  'Why do you want {0}',
  "What's stopping you from getting {0}"],
 'do you remember (.*)': ['Did you think I would forget {0}',
  "Why haven't you been able to forget {0}",
  'What about {0}',
  'Yes .. and?'],
 'do you think (.*)': ['if {0}? Absolutely.', 'No chance'],
 'if (.*)': ["Do you really think it's likely that {0}",
  'Do you wish that {0}',
  'What do you think about {0}',
  'Really--if {0}']}
 
def match_msg(rules,message):
    response,phrase="default",None
    
    for pattern,response in rules.items():
        match=re.search(pattern,message)
        if match is not None:
            responses=random.choice(response)
            if '{0}' in response:
                phrase=match.group(1)
#                phrase=phrase.lower()
#                if 'me' in phrase:
#                    # Replace 'me' with 'you'
#                    return re.sub('me', 'you', phrase)
#                if 'my' in phrase:
#                    # Replace 'my' with 'your'
#                    return re.sub('my', 'your', phrase)
#                if 'your' in phrase:
#                    # Replace 'your' with 'my'
#                    return re.sub('your', 'my', phrase)
#                if 'you' in phrase:
#                    # Replace 'you' with 'me'
#                    return re.sub('you', 'me', phrase)
    return responses.format(phrase)
    
    
    


match_msg(rules,"do you remember jessy?")