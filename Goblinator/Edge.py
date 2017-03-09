# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 00:02:09 2017

@author: jeff
"""

import Modifier

class Edge(Modifier.Modifier):
    
    def __init__(self, name, requirements, description, effects):
        super(Edge, self).__init__(name, requirements, description, effects)
    
    