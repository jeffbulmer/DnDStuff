# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 01:04:52 2017

@author: jeff
"""

from random import randint
import math

class Roller:
    def __init__(self):
        self.num = raw_input("How many dice?: ")
        self.size = raw_input("What dietype?: d");
        self.sum = self.roll(self.num, self.size, False)
        print("Total: " + str(self.sum))
        avg_size = self.getAverage(self.num, self.size)
        print("Average " + self.num +"d" + self.size + " Roll (10000 rolls): " + str(avg_size))
        exp = self.getExpected(self.size)
        print("Expected d" + self.size + " Roll: " + str(exp))
        
    def roll(self, num, size, display):
        curr = 0;
        i = 0
        while(i < int(num)):        
            stop = False        
            iteration = 0;
            while(not stop):
                iteration = iteration + 1
                add = randint(1,int(size))
                curr = curr + add
                printstr = "Iteration " + str(iteration) + ", Rolled  " + str(add)
                if add is not int(size):
                    stop = True
                else:
                    printstr = printstr + " Explode"
                if(display):
                    print(printstr)
                i = i + 1
        return curr
        
    def getAverage(self, num, size):
        i = 0
        raw_avg = 0
        while(i < 10000):
            raw_avg = raw_avg + self.roll(num,size, False)
            i = i+1
        end_avg = raw_avg / i
        return end_avg

    def getExpected(self, size):
        i = 1.0
        expected = 0.0
        modifier = 1.0/int(size)
        #modifier for dice explosion
        #taken from eric22222.wordpress.com: "A Mathematical analysis of Exploding Dice"        
        explosion = int(size) / (int(size) - 1.0)
        while(i <= int(size)):
            expected = expected + (i * modifier)
            i = i+1
        return expected * explosion
        
roller = Roller()
