# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 14:43:44 2017

@author: jeff
"""

from random import randint


class Name:
    
    def __init__(self, nameType):
        self.nameType = nameType.lower()

    def getName(self):
        return str(self.generateName(self.nameType))

        ########################### Name Generation ###########################
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
    
    
    def generateName(self, nameType):
        if nameType == "goblin":
           vowels = self.assignWeights({"a": 7, "e": 12, "i": 11, "o": 29, "u":9, "y":3})       
           consonants = self.assignWeights({'b':3,'c':2,'d':6,'f':1,'g':16,'h':5,'j':1,'k':10,'l':15,'m':9,'n':12,'p':2, 'q':0,'r':14,'s':6,'t':6,'v':5,'w':4,'x':3,'y':3,'z':1})        
           return self.generateNameLetters(vowels, consonants)
           
         
    
    def generateNameLetters(self, vowels, consonants):
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