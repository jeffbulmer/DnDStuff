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
                           Hindrance.Hindrance("Bad Eyes",{1:["hindrance", "Blind", "has not", 0]}, "This character can't see very well without glasses. -2 to Notice and shoot rolls if the object is more than 5 feet away", {1:["skill","notice", "minus", 2], 2:["skill","shooting","minus", 2]}, "Minor"),
                           Hindrance.Hindrance("Bad Luck",{1:["level", "", "at least", 0]}, "Fun fact: Murphy wanted to name his law after this character, but he couldn't remember the name. Just this character's luck, eh? This Character gets one fewer Benny per session", {1:["pace", 0, "plus", 0]}, "Major"),
                           Hindrance.Hindrance("Big Mouth",{1:["level", "", "at least", 0]}, "Can you keep a secret? Than that's one skill you have that this character doesn't.", {1:["pace", 0, "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Blind",{1:["hindrance", "Bad Eyes", "has not", 0]}, "This character cannot see. -6 on all rolls that require vision, -2 to all social rolls. This character may take an additional edge.", {1:["edge", 0, "plus", 1], 2:["skill", "fighting", "minus", 6], 3:["skill","shooting","minus", 6], 4:["skill","notice","minus",6], 5:["skill","driving","minus",6], 6:["skill","riding","minus",6], 7:["skill","boating","minus",6], 8:["skill","persuasion","minus",2]}, "Major"),
                           Hindrance.Hindrance("Bloodthirsty",{1:["level", "", "at least", 0]}, "This character never takes prisoners", {1:["charisma", 0, "minus", 4]}, "Major"),
                           Hindrance.Hindrance("Cautious",{1:["level", "", "at least", 0]}, "This character is overly careful.", {1:["pace", 0, "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Clueless",{1:["level", "", "at least", 0]}, "Do you know why the sky is blue? If you answered 'Wait, the sky is blue?', you might be as clueless as this character. -2 on most common knowledge rolls", {1:["skill", "common knowledge", "minus", 2]}, "Major"),
                           Hindrance.Hindrance("Code of Honour",{1:["level", "", "at least", 0]}, "This character is very honourable. S/he always keeps his/her word, and behaves well.", {1:["pace", 0, "plus", 0]}, "Major"),
                           Hindrance.Hindrance("Curious",{1:["level", "", "at least", 0]}, "Curiosity killed the cat. This character would be wise to ensure s/he doesn't suffer the same fate...", {1:["pace", 0, "plus", 0]}, "Major"),
                           Hindrance.Hindrance("Death Wish (Minor)",{1:["hindrance", "Death Wish (Major)", "has not", 0]}, "This character dreams of a good death... a death directly following some particular event.", {1:["pace", 0, "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Death Wish (Major)",{1:["hindrance", "Death Wish (Minor)", "has not", 0]}, "This character fantasizes of a glorious death. Of course, his/her definition of 'glorious' is a bit broader than most...", {1:["pace", 0, "plus", 0]}, "Major"),
                           Hindrance.Hindrance("Delusional (Minor)",{1:["hindrance", "Delusional (Major)", "has not", 0]}, "The world is run by a secret society! This character believes something about the world that most would brush off as nonsense.", {1:["pace", 0, "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Delusional (Major)",{1:["hindrance", "Delusional (Minor)", "has not", 0]}, "No one ever dies! It's all false flags, but the government wants to kill me! This character steadfastly believes in something most in the world would brush off as nonsense, and will go to lengths to defend those beliefs", {1:["pace", 0, "plus", 0]}, "Major"),
                           Hindrance.Hindrance("Doubting Thomas",{1:["edge", "Arcane Background", "has not", 0]}, "This character doesn't believe in magic or the supernatural.", {1:["pace", 0, "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Enemy (Minor)",{1:["level", "", "at least", 0]}, "This character has a rival", {1:["pace", 0, "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Enemy (Major)",{1:["level", "", "at least", 0]}, "This character has a nemesis", {1:["pace", 0, "plus", 0]}, "Major"),
                           Hindrance.Hindrance("Greedy (Minor)",{1:["hindrance", "Greedy (Major)", "has not", 0]}, "This character wants to have more stuff.", {1:["pace", 0, "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Greedy (Major)",{1:["hindrance", "Greedy (Minor)", "has not", 0]}, "This character is obsessed with wealth", {1:["pace", 0, "plus", 0]}, "Major"),
                           Hindrance.Hindrance("Habit (Minor)",{1:["hindrance", "Habit (Major)", "has not", 0]}, "This character has an annoying quirk.", {1:["pace", 0, "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Habit (Major)",{1:["hindrance", "Habit (Minor)", "has not", 0]}, "This character has an annoying obsession", {1:["pace", 0, "plus", 0]}, "Major"),
                           Hindrance.Hindrance("Hard of Hearing (Minor)",{1:["hindrance", "Hard of Hearing (Major)", "has not", 0]}, "This character has trouble hearing.", {1:["skill", "notice", "minus", 2]}, "Minor"),
                           Hindrance.Hindrance("Hard of Hearing (Major)",{1:["hindrance", "Hard of Hearing (Minor)", "has not", 0]}, "This character is deaf. Automatic failure on hearing based rolls.", {1:["skill", "notice", "minus", 10]}, "Major"),
                           Hindrance.Hindrance("Heroic",{1:["level", "", "at least", 0]}, "Ever valiant, this character is sworn to help those in need.", {1:["pace", 0, "plus", 0]}, "Major"),
                           Hindrance.Hindrance("Illiterate",{1:["level", "", "at least", 0]}, "Tihs carhatcer cnot reed", {1:["pace", 0, "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Lame",{1:["level", "", "at least", 0]}, "This character has trouble walking, and is a bit slower than usual as a result. Running die is a d4.", {1:["pace", 0, "minus", 2]}, "Major"),
                           Hindrance.Hindrance("Loyal",{1:["level", "", "at least", 0]}, "This hero will never betray his/her friends.", {1:["pace", 0, "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Mean",{1:["level", "", "at least", 0]}, "People don't like being around this character. For good reason.", {1:["charisma", 0, "minus", 2]}, "Minor"),
                           Hindrance.Hindrance("Obese",{1:["level", "", "at least", 0]}, "Call it what you want, this character is realy just big-boned. Rolls a d4 running die.", {1:["pace", 0, "minus", 1], 2:["toughness",0,"plus",1]}, "Minor"),
                           Hindrance.Hindrance("One Arm",{1:["level", "", "at least", 0]}, "This character is never fully 'armed'. -4 to any task requiring 2 arms.", {1:["pace", 0, "plus", 0]}, "Major"),
                           Hindrance.Hindrance("One Eye",{1:["level", "", "at least", 0]}, "This character is missing an eye. -2 to any roll requiring depth perception.", {1:["charisma", 0, "minus", 1],2:["skill","shooting","minus",2]}, "Major"),
                           Hindrance.Hindrance("One Leg",{1:["level", "", "at least", 0]}, "Almost everyone in the world has a leg up on this character. Rolls a d4 running die, -2 to any roll requiring two legs.", {1:["pace", 0, "minus", 2],2:["skill","swimming","minus",2]}, "Major"),
                           Hindrance.Hindrance("Outsider",{1:["level", "", "at least", 0]}, "This character never really fits in with society.", {1:["charisma", 0, "minus", 2]}, "Minor"),
                           Hindrance.Hindrance("Overconfident",{1:["level", "", "at least", 0]}, "As a child, this character was told 'You can do anything you set your mind to'. S/he promptly set his/her mind to doing anything.", {1:["pace", 0, "plus", 0]}, "Major"),
                           Hindrance.Hindrance("Pacifist (Minor)",{1:["hindrance","Pacifist (Major)","has not",0]}, "This character is combat-averse", {1:["pace", 0, "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Pacifist (Major)",{1:["hindrance", "Pacifist (Minor)", "has not", 0]}, "This character refuses to fight.", {1:["pace", 0, "plus", 0]}, "Major"),
                           Hindrance.Hindrance("Phobia (Minor)",{1:["hindrance", "Phobia (Major)", "has not", 0]}, "This character has an irrational fear", {1:["pace", 0, "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Phobia (Major)",{1:["hindrance", "Phobia (Minor)", "has not", 0]}, "This character has a crippling irrational fear.", {1:["pace", 0, "plus", 0]}, "Major"),
                           Hindrance.Hindrance("Poverty",{1:["level", "", "at least", 0]}, "This character is really bad with money. It's ok though, s/he's never had all that much anyway...", {1:["pace", 0, "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Quirk",{1:["level", "", "at least", 0]}, "This character has a kooky quirk.", {1:["pace", 0, "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Small",{1:["level", "", "at least", 0]}, "This character is smaller than average", {1:["toughness", 0, "minus", 1]}, "Major"),
                           Hindrance.Hindrance("Stubborn",{1:["level", "", "at least", 0]}, "This character always gets his way... because s/he won't cooperate otherwise....", {1:["pace", 0, "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Ugly",{1:["level", "", "at least", 0]}, "This character has a face only a mother could love... well, let's not overplay how attractive s/he is...", {1:["charisma", 0, "minus", 2]}, "Minor"),
                           Hindrance.Hindrance("Vengeful (Minor)",{1:["hindrance", "Vengeance (Major)", "has not", 0]}, "This character holds grudges.", {1:["pace", 0, "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Vengeful (Major)",{1:["hindrance", "Vengeful (Minor)", "has not", 0]}, "Get on this character's bad side, and s/he'll never forget it... at least not until you're dead.", {1:["pace", 0, "plus", 0]}, "Major"),
                           Hindrance.Hindrance("Vow (Minor)",{1:["hindrance", "Vow (Major)", "has not", 0]}, "This character has made a pledge to a group, deity or religion.", {1:["pace", 0, "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Vow (Major)",{1:["hindrance", "Vow (Minor)", "has not", 0]}, "This character has made a serious pledge to a group, deity or religion.", {1:["pace", 0, "plus", 0]}, "Major"),
                           Hindrance.Hindrance("Wanted (Minor)",{1:["hindrance", "Wanted (Major)", "has not", 0]}, "This character is wanted for some crime.", {1:["pace", 0, "plus", 0]}, "Minor"),
                           Hindrance.Hindrance("Wanted (Major)",{1:["hindrance", "Wanted (Minor)", "has not", 0]}, "This character is wanted for some crime.", {1:["pace", 0, "plus", 0]}, "Major"),
                           Hindrance.Hindrance("Yellow",{1:["level", "", "at least", 0]}, "This character is unusually cowardly, and suffers -2 to fear checks.", {1:["pace", 0, "plus", 0]}, "Major")
                          ]
