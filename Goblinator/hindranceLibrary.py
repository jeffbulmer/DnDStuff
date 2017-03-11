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
        self.length = len(self.hindrances)
        
    def selectAtRandom(self):
        return self.hindrances[randint(0,len(self.hindrances)-1)]

    def selectWithName(self, name):
        for i in self.hindrances:
            if i.getName() == name:
                return i
        print("Hindrance Not Found")
        return 0
        
    def populate(self):
        self.hindrances = [Hindrance.Hindrance("All Thumbs",{1:["level", "", "at least", 0]}, "This character doesn't really 'get' machinery. Suffer a -2 to repair, and on a roll of 1, the device malfunctions", {1:["skill", "repair", "minus", 2]}, "Minor"),
                           Hindrance.Hindrance("Anemic",{1:["level","","at least", 0]}, "Ferrous Bueller took a day off. This character suffers from low blood iron content, and gets fatigued easily as a result. -2 to Fatigue tests", {1:["pace", 0, "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Arrogant",{1:["level","","at least",0]}, "This character thinks a little more highly of him/herself than is probably wise. The character must humiliate opponents, and when meeting an enemy force, the character must challenge the leader", {1:["pace", 0, "plus", 0]}, "Major"),
                           Hindrance.Hindrance("Bad Eyes (Near-Sighted)",{1:["level", "", "at least", 0]}, "This character can't see very well without glasses. -2 to Notice and shoot rolls if the object is more than 5 feet away", {1:["skill","notice", "minus", 2]}, "Minor"),
                           Hindrance.Hindrance("Kind of Bad Stuff",{1:["level", "", "at least", 0]}, "Minor Bad Stuff", {1:["pace", 0, "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Kind of Bad Stuff",{1:["level", "", "at least", 0]}, "Minor Bad Stuff", {1:["pace", 0, "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Kind of Bad Stuff",{1:["level", "", "at least", 0]}, "Minor Bad Stuff", {1:["pace", 0, "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Kind of Bad Stuff",{1:["level", "", "at least", 0]}, "Minor Bad Stuff", {1:["pace", 0, "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Kind of Bad Stuff",{1:["level", "", "at least", 0]}, "Minor Bad Stuff", {1:["pace", 0, "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Kind of Bad Stuff",{1:["level", "", "at least", 0]}, "Minor Bad Stuff", {1:["pace", 0, "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Kind of Bad Stuff",{1:["level", "", "at least", 0]}, "Minor Bad Stuff", {1:["pace", 0, "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Kind of Bad Stuff",{1:["level", "", "at least", 0]}, "Minor Bad Stuff", {1:["pace", 0, "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Kind of Bad Stuff",{1:["level", "", "at least", 0]}, "Minor Bad Stuff", {1:["pace", 0, "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Kind of Bad Stuff",{1:["level", "", "at least", 0]}, "Minor Bad Stuff", {1:["pace", 0, "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Kind of Bad Stuff",{1:["level", "", "at least", 0]}, "Minor Bad Stuff", {1:["pace", 0, "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Kind of Bad Stuff",{1:["level", "", "at least", 0]}, "Minor Bad Stuff", {1:["pace", 0, "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Kind of Bad Stuff",{1:["level", "", "at least", 0]}, "Minor Bad Stuff", {1:["pace", 0, "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Kind of Bad Stuff",{1:["level", "", "at least", 0]}, "Minor Bad Stuff", {1:["pace", 0, "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Kind of Bad Stuff",{1:["level", "", "at least", 0]}, "Minor Bad Stuff", {1:["pace", 0, "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Kind of Bad Stuff",{1:["level", "", "at least", 0]}, "Minor Bad Stuff", {1:["pace", 0, "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Kind of Bad Stuff",{1:["level", "", "at least", 0]}, "Minor Bad Stuff", {1:["pace", 0, "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Kind of Bad Stuff",{1:["level", "", "at least", 0]}, "Minor Bad Stuff", {1:["pace", 0, "plus", 0]}, "Minor"),
                          ]
