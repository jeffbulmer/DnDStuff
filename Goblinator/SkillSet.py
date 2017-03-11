# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 15:44:47 2017

@author: jeff
"""

from random import randint
import math

class SkillSet:
    
    def __init__(self, possibleSkills):
        self.skills = {}
        self.populateSkills(possibleSkills)
        print(self.skills)
        
    def populateSkills(self, possibleSkills):
        for i in possibleSkills:
            self.skills[i] = [possibleSkills[i], 0]
            
    def getSkills(self):
        return self.skills
            
    def assignSkills(self, points, init, attr):
         panic = 0
         while points > 0:
            #select skill to modify            
            addAttr = randint(0,len(self.skills)-1)
            skill = self.skills[self.skills.keys()[addAttr]]
            maxV = attr[skill[0]]
            
            #determine modifier
            mod = randint(1,5)            
            
            #determine incentive 
            #skill assignment incentivizes putting points into 
            #useful skills that correspond to attributes
            #which the goblin possesses.
            incentive = math.floor(maxV/2);
            if(maxV > 1):
                if init:
                    incentive += 1
                else:
                    incentive -= 1
            else:
                incentive -= 2
            if(skill[1] > maxV):
                incentive -= 1
            elif(skill[1] < maxV):
                incentive += 1
            if(skill[0].lower == 'smarts' or skill[0].lower == 'agility'):
                incentive += 1
            incentive += maxV - (mod+skill[1]-1)
            
            #modify skill
            check = randint(0,maxV)
            
            #print("Skill: " + str(self.skills.keys()[addAttr]))
            #print("Incentive = " + str(incentive))
            #print("Check = " + str(check))
            #print("Mod = " + str(mod))
            if incentive >= check or panic >= 5:
                if panic == 5:
                    panic = 0;                
                cost = 0;
                for i in range(0,mod):
                    currV = skill[1]
                    currCost = 0
                    if (currV + 1) > 5:
                        break;
                    if (currV >= maxV) or (currV == 0 and not init):
                        currCost = 2
                    else:
                        currCost = 1
                        
                    cost += currCost
                    if points - cost < 0:
                        break;
                    skill[1] += 1
                
                points -= cost
            else:
                panic += 1