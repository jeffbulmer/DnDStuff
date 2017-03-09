# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 12:07:28 2017

@author: jeff
"""

import Modifier

class Hindrance(Modifier.Modifier):
    
    def __init__(self, name, requirements, description, effects, hindType):
        super(Hindrance, self).__init__(name, requirements, description, effects)
        self.hindType = hindType
        
    def isCompatible(self, attr, skills, edges, hindrances, level, containsMajor):
        for i in hindrances:
            if self.name.lower() == hindrances[i].name.lower():
                return False
        if self.hindType.lower() == "major" and containsMajor:
            return False;
        else:
            return super(Hindrance, self).isCompatible(attr, skills, hindrances, level)
