# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from random import randint
import math
import Edge
import edgeLibrary

class Goblin:    
    
    def __init__(self, lvl, armour, paceMod, parryMod):
        self.verbose = True
        self.library = edgeLibrary.edgeLibrary()
        self.name = self.generateName()      
        self.level = 0
        self.attrLock = False        
        self.attr = {"agility": 1,
                "smarts": 1,
                "spirit": 1,
                "strength": 1,
                "vigor": 1
                }
        self.assignAttr()
        self.skills = {"boating": ["agility", 0],
                       "climbing": ["strength", 0],
                       "fighting": ["agility", 0],
                       "healing": ["smarts", 0],
                       "intimidate": ["spirit",0],
                       "lockpicking": ["agility",0],
                       "notice": ["smarts", 0],
                       "persuasion": ["spirit",0],
                       "repair": ["smarts", 0],
                       "shooting": ["agility", 0],
                       "stealth": ["agility", 0],
                       "survival":["smarts", 0],
                       "swimming": ["agility", 0],
                       "throwing": ["agility", 0],
                       "tracking": ["smarts", 0],
                       "taunt": ["smarts", 0],
                       "use magic item": ["smarts", 0]}
        self.assignSkills(15)
        self.edges = {}
        self.effects = {}        
        self.base_toughness = 2+ (self.attr["vigor"]+1)
        self.toughness = self.base_toughness + armour
        self.base_parry = 2 + (self.skills["fighting"][1]+1)
        self.parry = self.base_parry
        self.pace = 6 + paceMod
        self.charisma = 0

        while self.level < lvl:
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
            if self.attr.keys()[addAttr] is "smarts" and ptA%2 is 0:
                while ptA > 0 and (self.attr[self.attr.keys()[addAttr]] + 1) < 6:                
                    self.attr[self.attr.keys()[addAttr]] += 1
                    ptA -= 2
                    points -=2
            else:
                while ptA > 0 and (self.attr[self.attr.keys()[addAttr]] + 1) < 6:
                    self.attr[self.attr.keys()[addAttr]] += 1
                    ptA -= 1
                    points -= 1
            
            
    def assignSkills(self, points):
         panic = 0
         while points > 0:
            #select skill to modify            
            addAttr = randint(0,len(self.skills)-1)
            skill = self.skills[self.skills.keys()[addAttr]]
            maxV = self.attr[skill[0]]
            
            #determine modifier
            mod = randint(1,5)            
            
            #determine incentive 
            #skill assignment incentivizes putting points into 
            #useful skills that correspond to attributes
            #which the goblin possesses.
            incentive = math.floor(maxV/2);
            if(maxV > 1):
                incentive += 1
            else:
                incentive -= 2
            if(skill[1] > maxV):
                incentive -= 1
            elif(skill[1] < maxV):
                incentive += 1
            if(skill[0] == 'smarts' or skill[0] == 'agility'):
                incentive += 1
            incentive += maxV - (mod+skill[1]-1)
            
            #modify skill
            check = randint(0,maxV)
            
            #print("Skill: " + str(self.skills.keys()[addAttr]))
            #print("Incentive = " + str(incentive))
            #print("Check = " + str(check))
            #print("Mod = " + str(mod))
            if incentive >= check or panic is 5:
                if panic == 5:
                    panic = 0;                
                cost = 0;
                for i in range(0,mod):
                    currV = skill[1]
                    if (currV + 1) > 5:
                        break;
                    if currV < maxV:
                        cost += 1
                    else:
                        cost += 2                    
                        
                    if points - cost < 0:
                        break;
                    skill[1] += 1
                
                points -= cost
            else:
                panic += 1
    
    
    ######################### Effects format #############################
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
        #effects = {1:[type("attr","skill","toughness", or "parry"), 
        #----                  "nameOfAttr",
        #----                  operator("plus","minus", "multiply", "divide"), 
        #----                  value], ...}
    
    def addEdge(self):
        addEdge = self.library.selectAtRandom()
        names = {};
        for i in self.edges:
            names[i] = self.edges[i].name
        while (addEdge.isCompatible(self.attr, self.skills, self.edges, self.level)) == False:
           addEdge = self.library.selectAtRandom()
        self.evaluateEdge(addEdge, self.verbose)
        self.edges[len(self.edges)] = addEdge;
            
    
    def evaluateEdge(self, edge, verbose):
        effects = edge.getEffects()
        for i in effects:
            if verbose:
                self.doEffectsVerbose(effects[i], edge.getName())
            else:
                self.doEffectsCompact(effects[i], edge.getName())
            #print(edge.name + " effects done")
            
    def doEffectsVerbose(self, effect, edgeName):
        mod = effect[0]
        name = effect[1]
        operator = effect[2]
        value = effect[3]
        if mod is ("attr" or "skill"):
            self.effects[len(self.effects)] = name + " " + operator + str(value) + " due to " + edgeName
        elif mod is "toughness":
            self.effects[len(self.effects)] = mod + " " + operator + str(value) + " due to " + edgeName
            self.toughness = self.operate(operator, self.toughness, value)
        elif mod is "parry":
            self.effects[len(self.effects)] = mod + " " + operator + str(value) + " due to " + edgeName
            self.parry = self.operate(operator, self.parry, value)
        elif mod is "pace":
            self.effects[len(self.effects)] = mod + " " + operator + str(value) + " due to " + edgeName
            self.pace = self.operate(operator, self.pace, value)
        elif mod is "charisma":
            self.effects[len(self.effects)] = mod + " " + operator + str(value) + " due to " + edgeName
            self.charisma = self.operate(operator, self.charisma, value)
    
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
                     lvlStr += addAttr + " raised by 1"
            if mod is 2:
                self.assignSkills(2)
                lvlStr += " skills raised "
                valid = True
            if mod is 3:
                self.addEdge()
                lvlStr += " edge added "
                valid = True
        print(lvlStr)
    
    ############################### Name Generation ###########################
        #---- Handles random name generation for a goblin.
        #---- first, an array of vowels and an array of constants are created.
        #---- each array is then weighted, and a while loop then creates a name
        #---- based on an algorithm which has been found to generate usually
        #---- reasonable names (the rules are essentially arbitrary)
        #---- letters are added based on an incentive function that awards 
        #---- incentive for following the predefined rules. 
        #----------------------------------------------------------------------
        #---- The helper function assignWeights expands an array of keys and weights
        #---- which is given as a dictionary, by creating an array containing
        #---- a number of each key given by that key's weight.
    
    def generateName(self):
        vowels = self.assignWeights({"a": 7, "e": 12, "i": 11, "o": 29, "u":9, "y":3})       
        consonants = self.assignWeights({'b':3,'c':2,'d':6,'f':1,'g':16,'h':5,'j':1,'k':10,'l':15,'m':9,'n':12,'p':2, 'q':0,'r':14,'s':6,'t':6,'v':5,'w':4,'x':3,'y':3,'z':1})        
        name = ""
        lastletter = ""
        length = randint(4, 8)
        vir = 0;
        cir = 0;
        while len(name) < length:
            iniVal = randint(0,1)
            if len(name) == 0:
                if iniVal is 0:
                    addletter = vowels[randint(0,len(vowels)-1)]
                    lastletter = addletter
                    name += addletter
                    vir += 2
                    cir = 0
                else:
                    addletter = consonants[randint(0,len(consonants)-1)]
                    lastletter = addletter                    
                    name += addletter
                    vir = 0
                    cir += 1
            else:
                mod = randint(0,max(vir+1, cir+1))
                if (vir > cir and iniVal == mod) or (cir > vir and iniVal != mod):
                    addletter = vowels[randint(0,len(vowels)-1)]
                    if (addletter == lastletter and randint(0,4) == 1) or addletter != lastletter:
                        name += addletter 
                        lastletter = addletter
                        vir += 2
                        cir = 0
                else:
                    addletter = consonants[randint(0,len(consonants)-1)]
                    if (addletter == lastletter and randint(0,7) == 1) or addletter != lastletter:
                        if(lastletter == 'g' or lastletter == 'k' or lastletter == 'c' or lastletter == 'j') and randint(0,5) == 1:  
                            continue;
                        name += addletter
                        lastletter = addletter
                        cir += 1
                        vir = 0
        return name
        
    def assignWeights(self,dictionary):
        array = []
        for k in dictionary:
            v = int(dictionary[k])
            for m in range(0,v):
                array.append(k)
        return array
                
            
    ############################### toString Method ###########################
            #---- This method takes all the elements of the character, and
            #---- generates a basic character sheet.
    def toString(self):
        dieTypes = {'1': 'd4', '2': 'd6', '3': 'd8', '4': 'd10', '5': 'd12', '6': 'd12 +2'}
        attStr = 'Attributes: '
        skillStr = 'Skills: '
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

        # for i, hind in self.hindrances:
        #     if i == len(self.hindrances) - 1:
        #         hindStr += str(hind) + '}'
        #     else:
        #         hindStr += str(hind) + ', '

        skillStr = skillStr[0:(len(skillStr)-2)] + ''

        returnStr = attStr + '\n' + paceStr + '\n' + toughStr + '\n' + skillStr + '\n' + edgeStr + '\n' + hindStr
        print(returnStr)       

goblin = Goblin(32,0,0,0)
print(goblin.name)
print("Level: " + str(goblin.level))
print(goblin.toString())