# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 02:16:23 2017

@author: jeff
"""
from random import randint
import json
import SkillSet

class Character(object):
    
    def __init__(self, lvl, armour, nameObject, verbose, allEdges, allHindrances, impair, skillString):
        self.name = nameObject.getName()
        self.verbose = verbose
        self.allEdges = allEdges
        self.allHindrances = allHindrances
        self.impair = impair
        self.edges = {}
        self.hindrances = {}
        self.effects = {}
        self.base_toughness = self.toughness = 2;
        self.base_parry = self.parry = 2;    
        self.pace = 6
        self.charisma = 0
        self.level = 0
        self.attrLock = False
        self.attr = {"agility": 1,
                "smarts": 1,
                "spirit": 1,
                "strength": 1,
                "vigor": 1
                }                
        self.skillSet = SkillSet.SkillSet(skillString)
        self.skills = self.skillSet.getSkills()
        self.assignAttr()
        self.assignSkills(15, True)
        self.assignHindrances()    
        self.base_toughness = 2+ (self.attr["vigor"]+1)
        self.toughness = self.base_toughness + armour
        self.base_parry = self.parry = 2 + (self.skills["fighting"][1]+1)
        while int(self.level) < int(lvl):
            self.levelUp()        
                
    def assignAttr(self):
        points = 5;
        while points > 0:
            addAttr = randint(0,4)
            ptA = randint(0,points) #points to add
            if ptA >= 5:
                ptA = 4
            if self.attr.keys()[addAttr] == 5:
                continue
            if self.attr.keys()[addAttr] in self.impair:
                if ptA%2 == 0:
                    while ptA > 0 and (self.attr[self.attr.keys()[addAttr]] + 1) < 6:                
                        self.attr[self.attr.keys()[addAttr]] += 1
                        ptA -= 2
                        points -=2
                        #print(self.attr.keys()[addAttr] + " raised. Points remaining: " + str(points))
                        if points == 0:
                            continue
                else:
                    continue
            else:
                while ptA > 0 and (self.attr[self.attr.keys()[addAttr]] + 1) < 6:
                    self.attr[self.attr.keys()[addAttr]] += 1
                    ptA -= 1
                    points -= 1
                    #print(self.attr.keys()[addAttr] + " raised. Points remaining: " + str(points))
                    if points == 0:
                        continue
            
    def assignSkills(self, points, init):
        self.skillSet.assignSkills(points, init, self.attr)
        self.skills = self.skillSet.getSkills()
    
    def assignHindrances(self):
        numHindrances = randint(0,3)
        i = 1
        points = 0
        while i <= numHindrances:
            self.addHindrance('')
            i += 1
        for k in self.hindrances:
            if self.hindrances[k].hindType.lower() == 'major':
                points += 2
            else:
                points += 1
    
    ######################### Edges and Hindrances ############################
        #---- The following methods implement a character's edges.
        #---- The format of Edges is described below in a dedicated class
        #---- Once an edge is chosen, the addEdge() function processes that edge
        #---- applying its effects to the character
        #---- There are two main ways of evaluating an edge: verbose and compact
        #---- The verbose method applies the effects in the form of strings,
        #---- which are added to the effects array, preserving the character's
        #---- original skills and attributes. 
        #---- The compact method changes the characters attributes and skills 
        #---- directly. The player is then left to interpret the resulting
        #---- character sheet.
        #---- By default, verbose is selected.
        #----------------------------------------------------------------------
        #---- Hindrances work similar to edges, but also must account for 
        #---- Hindrance type, which is major or minor. 
        #---- A character may only have one major hindrance, so the add and
        #---- evaluate functions incorporate this extra check.
        #---- additionally, the verify function is different within the 
        #---- hindrance class. Go to that class for more information.    
    def addEdge(self, name):
        names = {};
        for i in self.edges:
            names[i] = self.edges[i].name        
        if name != '':
            addEdge = self.allEdges.selectWithName(name)
        else:
            addEdge = self.allEdges.selectAtRandom()
            count = 1
            while not addEdge.isCompatible(self.attr, self.skills, self.edges, self.level) and int(count) < int(self.allEdges.length):
               addEdge = self.allEdges.selectAtRandom()
        if addEdge != 0:
            self.evaluateEdge(addEdge, self.verbose)
            self.edges[len(self.edges)] = addEdge;
            return True
        else:
            return False
            
    
    def evaluateEdge(self, edge, verbose):
        effects = edge.getEffects()
        for i in effects:
            if verbose:
                self.doEffectsVerbose(effects[i], edge.getName())
            else:
                self.doEffectsCompact(effects[i], edge.getName())
    

    def addHindrance(self, name):
        names = {};
        containsMajor = False
        minors = 0
        for i in self.hindrances:
            names[i] = self.hindrances[i].name
            if self.hindrances[i].hindType.lower == "major":
                containsMajor = True;        
            elif self.hindrances[i].hindType.lower == "minor":
                minors += 1
        if name != '':
            addHindrance = self.allHindrances.selectWithName(name)
        else:
            addHindrance = self.allHindrances.selectAtRandom()
            count = 1
            while (addHindrance.isCompatible(self.attr, self.skills, self.edges, self.hindrances, self.level, containsMajor, minors)) == False and int(count) < int(self.allHindrances.length):
               addHindrance = self.allHindrances.selectAtRandom()
        if addHindrance != 0:
            self.evaluateHindrance(addHindrance, self.verbose)
            self.hindrances[len(self.hindrances)] = addHindrance;
        else:
            return False

    def evaluateHindrance(self, hindrance, verbose):
        effects = hindrance.getEffects()
        for i in effects:
            if verbose:
                self.doEffectsVerbose(effects[i], hindrance.getName())
            else:
                self.doEffectsCompact(effects[i], hindrance.getName())
        
        
    def doEffectsVerbose(self, effect, modName):
        mod = effect[0]
        name = effect[1]
        operator = effect[2]
        value = effect[3]
        if mod is ("attr" or "skill"):
            self.effects[len(self.effects)] = name + " " + operator + str(value) + " due to " + modName
        elif mod is "toughness":
            self.effects[len(self.effects)] = mod + " " + operator + str(value) + " due to " + modName
            self.toughness = self.operate(operator, self.toughness, value)
        elif mod is "parry":
            self.effects[len(self.effects)] = mod + " " + operator + str(value) + " due to " + modName
            self.parry = self.operate(operator, self.parry, value)
        elif mod is "pace":
            self.effects[len(self.effects)] = mod + " " + operator + str(value) + " due to " + modName
            self.pace = self.operate(operator, self.pace, value)
        elif mod is "charisma":
            self.effects[len(self.effects)] = mod + " " + operator + str(value) + " due to " + modName
            self.charisma = self.operate(operator, self.charisma, value)
        elif mod is "edge":
            i = 0;
            while int(i) < int(value):
                self.addEdge()
                i += 1
    
    ####doEffectsCompact is deprecated
    def doEffectsCompact(self, effect):
        mod = effect[0]
        name = effect[1]
        operator = effect[2]
        value = effect[3]
        if mod is "attr":
            newVal = self.operate(operator, self.attr[name], value)
            if(newVal > 5):
                self.attr[name] = 5
                print(name + " Cannot go higher than d12")
            else:
                self.attr[name] += newVal
        elif mod is "skill":
            newVal = self.operate(operator, self.skills[name][1], value)
            if(newVal > 5):
                self.skills[name][1] = 5
                print(name + " Cannot go higher than d12")
            else:
                self.skills[name][1] += newVal
        elif mod is "toughness":
            self.toughness = self.operate(operator, self.toughness, value)
        elif mod is "parry":
            self.parry = self.operate(operator, self.parry, value)
        elif mod is "pace":
            self.pace = self.operate(operator, self.pace, value)
        
    
    def operate(self, operator, firstOperand, secondOperand):
        if operator is "plus":
            return firstOperand + secondOperand
        elif operator is "minus":
            return firstOperand - secondOperand
        elif operator is "multiply":
            return firstOperand * secondOperand
        elif operator is "divide":
            return firstOperand / secondOperand
        else:
            return firstOperand                
            
    def levelUp(self):
        #create a levelUp string. This string will contain
        #information about the level up
        lvlStr = "Level Up: Level " + str(self.level) + " ->  "     
        
        #raise level by 1
        #every 4 levels, an attribute can be raised        
        self.level += 1
        lvlStr += str(self.level)
        if self.level%4 is 0:
            self.attrLock = False
            lvlStr += " Attribute lock disengaged "
        
        #choose what to do on a level up
        #this is chosen at random:
        #on 1, an attribute is raised
        #on 2, skills are raised
        #on 3, an edge is awarded        
        valid = False
        while valid is False:
            mod = randint(1,3)
            if mod is 1 and self.attrLock is False:
                addAttr = self.attr.keys()[randint(0,4)]
                if self.attr[addAttr] < 5:
                     self.attr[addAttr] += 1
                     self.attrLock = True                
                     valid = True
                     lvlStr += " " + addAttr + " raised by 1 "
            if mod is 2:
                self.assignSkills(2, False)
                lvlStr += " skills raised "
                valid = True
            if mod is 3:
                valid = self.addEdge('')
                lvlStr += " edge added "
                
        self.updateImpair()
        print(lvlStr)
        
    def updateImpair(self):
        for k in self.impair:
            if(self.impair[k] == 1):
                self.impair[k] -= 1;
        for k,v in self.impair.items():        
            if(v == 0):
                del self.impair[k]
                
            
    ############################### toString Method ###########################
            #---- This method takes all the elements of the character, and
            #---- generates a basic character sheet.
    def toString(self):
        dieTypes = {'1': 'd4', '2': 'd6', '3': 'd8', '4': 'd10', '5': 'd12', '6': 'd12 +2'}
        attStr = 'Attributes: '
        skillStr = 'Skills: '
        charStr = 'Charisma: ' + str(self.charisma)
        paceStr = 'Pace: ' + str(self.pace)
        toughStr = 'Toughness ' + str(self.toughness)        
        edgeStr = 'Edges: {'
        hindStr = 'Hindrances: {'

        for i, att in enumerate(self.attr):
            if i == len(self.attr) - 1:
                attStr += str(att) + ': ' + str(dieTypes[str(self.attr[att])]) + ''
            else:
                attStr += str(att) + ': ' + str(dieTypes[str(self.attr[att])]) + ', '

        for i, skill in enumerate(self.skills):
            if str(self.skills[skill][1]) != '0':
                skillStr += str(skill) + ': ' + str(dieTypes[str(self.skills[skill][1])]) + ', '
        
        for i in self.edges:
            if i == len(self.edges) - 1:
                 edgeStr += "\n" + self.edges[i].toString() + '}'
            else:
                 edgeStr += "\n" + self.edges[i].toString() + ', '

        for i in self.hindrances:
            if i == len(self.hindrances) - 1:
                 hindStr += "\n" + self.hindrances[i].toString() + '}'
            else:
                 hindStr += "\n" + self.hindrances[i].toString() + ', '
                 
        skillStr = skillStr[0:(len(skillStr)-2)] + ''

        returnStr = self.name + '\nLevel: ' + str(self.level) + '\n' + attStr + '\n' + charStr + '\n' + paceStr + '\n' + toughStr + '\n' + skillStr + '\n' + edgeStr + '\n' + hindStr
        print(returnStr)       
        
    ######################### import/export Methods ###########################
            #---- The following methods allow a character to exported and imported
            #---- which makes it so we can save a character for later. 
            #---- Using this, we can import a character to do things like using
            #---- the levelup function on a preexisting character.        
        
    def export(self):       
            exportDict = {'attr': self.attr,
                          'base_parry': self.base_parry,
                          'base_toughness': self.base_toughness,
                          'charisma': self.charisma,
                          'edges': self.enumerateModifiers(self.edges),
                          'effects': self.effects,
                          'hindrances': self.enumerateModifiers(self.hindrances),
                          'impair': self.impair,
                          'level': self.level,                      
                          'name': self.name,                      
                          'pace': self.pace,
                          'parry': self.parry,
                          'skillString': self.skillString,
                          'skills': self.skills,
                          'toughness': self.toughness,
                          'verbose': self.verbose
                          }
            return json.dumps(exportDict)
        
        
    def enumerateModifiers(self, modifiers):
        returnStr = ""            
        for i in modifiers:
            returnStr += modifiers[i].name + ";"
        return(returnStr)
        
    def processEnumerated(self, modString):
        array = {}
        initArray = modString.split(";")
        count = 0
        for i in initArray:
            if len(i) > 0:
                array[count] = i 
                count += 1
        return array;
            
    def importChar(self, json_string):
            importDict = json.loads(json_string)
            self.attr = importDict["attr"]
            self.base_parry = importDict["base_parry"]
            self.base_toughness = importDict["base_toughness"]
            self.charisma = importDict["charisma"]
            self.effects = importDict["effects"]
            self.impair = importDict["impair"]
            self.level = importDict["level"]
            self.name = importDict["name"]
            self.pace = importDict["pace"]
            self.parry = importDict["parry"]
            self.skills = importDict["skills"]
            self.toughness = importDict["toughness"]
            self.verbose = importDict["verbose"]

            self.skillSet = SkillSet.SkillSet(importDict["skillString"])
            self.edges = {}            
            edgeArray = self.processEnumerated(importDict["edges"])
            for i in edgeArray:
                self.addEdge(edgeArray[i])
            self.hindrances = {}
            hindranceArray = self.processEnumerated(importDict["hindrances"])
            for j in hindranceArray:
                self.addHindrance(hindranceArray[j])            
