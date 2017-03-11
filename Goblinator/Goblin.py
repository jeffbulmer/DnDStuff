# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import Character
import SkillSet
import Name
import edgeLibrary
import hindranceLibrary

class Goblin(Character.Character):    
    
    
    def __init__(self, lvl, armour):
        nameObject = Name.Name("goblin")        
        verbose = True
        allEdges = edgeLibrary.edgeLibrary()
        allHindrances = hindranceLibrary.hindranceLibrary() 
        impair = {'smarts':1}
        skillString = {"boating": "agility", 
                       "climbing": "strength",
                       "fighting": "agility",
                       "healing": "smarts",
                       "intimidate": "spirit",
                       "lockpicking": "agility",
                       "notice": "smarts",
                       "persuasion": "spirit",
                       "repair": "smarts",
                       "shooting": "agility",
                       "stealth": "agility",
                       "survival":"smarts", 
                       "swimming":"agility",
                       "throwing":"agility",
                       "tracking":"smarts",
                       "taunt": "smarts",
                       "use magic item": "smarts"}
        
        super(Goblin, self).__init__(lvl,armour, nameObject, verbose, allEdges, allHindrances, impair, skillString)