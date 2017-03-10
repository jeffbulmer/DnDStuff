# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 00:02:09 2017

@author: jeff
"""

import Hindrance
from random import randint

class hindranceLibrary:
    
    def __init__(self):
        self.hindrances = {}
        self.populate()
        
    def selectAtRandom(self):
        return self.hindrances[randint(0,len(self.hindrances)-1)]
        
    def populate(self):
        self.hindrances = [Hindrance.Hindrance("Kind of Bad Stuff",{1:["level", "", "at least", 0]}, "Minor Bad Stuff", {1:["pace", 0, "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Pretty Bad Stuff",{1:["level","","at least", 0]}, "Minor Bad Stuff 2", {1:["skill", "boating", "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Really Bad Stuff",{1:["level","","at least",0]}, "Major Bad Stuff", {1:["skill", "boating", "plus", 0]}, "Major"),
                          ]
