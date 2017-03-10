# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Modifier(object):
    #Each edge has requirements, a decription, and an effect.
    #requirements: an array describing the attributes or skills required to take this edge
    #description: a String describing the edge
    #effect: an array describing the practical effects of this edge.
    ######################### Requirements format #############################
        #----requirements = {1:[type("attr","skill", or "edge"), 
        #----                  "nameOfAttr",
        #----                  operator("at least","at most", "equal"), 
        #----                  value], ...}
    
    ######################### Effects format #############################
        #----effects = {1:[type("attr","skill","toughness", "parry", or "pace"), 
        #----                  "nameOfAttr",
        #----                  operator("plus","minus", "multiply", "divide"), 
        #----                  value], ...}
    
    def __init__(self, name, requirements, description, effects):
        self.name = name
        self.requirements = requirements
        self.description = description
        self.effects = effects
        
    def getName(self):
        return self.name
    
    def getDescription(self):
        return self.description
        
    def getEffects(self):
        return self.effects
        
   ######################### Requirement Checking ############################
        #----Check whether or not a character is compatible with an edge.
        #----An edge may have multiple requirements, so the isCompatible method
        #----must verify that each requirement is met.         
        #----If at any point a requirement is not fulfilled, it will return false,
        #----and the character is not compatible with the edge.
        #----------------------------------------------------------------------
        #----The verify function checks each requirement to see if it is fulfilled
        #----It does this by parsing through a requirement, and comparing it to 
        #----a character's current attributes, skills and edges.
        #----[Edge requires Edge] compatibility is determined by name only.
        #----[Edge requires Attribute] compatibility and [Edge requires Skills]
        #----compatibility is determined by comparison using ">=", "<=", or "=="
    def isCompatible(self, attr, skills, edges, level):
        check = True;
        #if not edges:        
        #    for i in enumerate(edges):
        #        if edges[i].name == self.name:
        #            check = False;            
        #if check:
        for i in self.requirements:
            check = self.verify(self.requirements[i], attr, skills, edges, level)
            if not check:
                return False
        return check

    def verify(self, requirement, attr, skills, edges, level):
        checkType = requirement[0].lower()
        name = requirement[1].lower()
        operator = requirement[2].lower()
        operand = requirement[3]
        compareDict = attr;        
        for i in edges:
            if self.name.lower() == edges[i].name.lower():
                return False
        if checkType == "attr":
            compareDict = attr
        elif checkType == "skill":
            compareDict = skills
        elif checkType == "edge":
            compareDict = edges
        elif checkType == ("level" or "charisma" or "toughness"):
            if operator.lower() == "at least":
                return (level >= operand)
            elif operator == "at most":
                return (level <= operand)
            elif operator == "equal":
                return (level == operand)   
        if name in compareDict:
            if compareDict is edges and operator == 'has':
                return True
            else:
                comparison = 0
                if compareDict is attr:
                    comparison = compareDict[name]
                elif compareDict is skills:
                    comparison = compareDict[name][1]
                if operator == "at least":
                    return (comparison >= operand)
                elif operator == "at most":
                    return (comparison <= operand)
                elif operator == "equal":
                    return (comparison == operand)
                    
    def toString(self):
        return self.name + ": " + self.description;
        
