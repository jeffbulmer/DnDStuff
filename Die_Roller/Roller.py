# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 01:04:52 2017

@author: jeff
"""

from random import randint
import math

class Roller:
    #Prompt a user for a number of dice and the dietype
    #The program will then roll that number of that dietype
    #It will also calculate the average roll for that number of that dietype, 
    #As well as the expected roll for that number of that dietype.
    #avgPrecision is 4 by default, but can be increased to get a higher precision
    #for the average roll, or decreased to speed up the program.
    def __init__(self, avgPrecision):
        self.num = int(raw_input("How many dice?: "))
        self.size = int(raw_input("What dietype?: d"))
        self.sum = self.roll(self.num, self.size, False)
        print("Total: " + str(self.sum))
        avg_size = self.getAverage(self.num, self.size, avgPrecision)
        print("Average " + str(self.num) +"d" + str(self.size) + " Roll ("+str((10 ** avgPrecision)) + " rolls): " + str(avg_size))
        exp = self.getExpected(self.size, self.num)
        print("Expected d" + str(self.size) + " Roll: " + str(exp))
        
    def roll(self, num, size, display):
        curr = 0;
        i = 0
        while(i < num):        
            stop = False        
            iteration = 0;
            while(not stop):
                iteration = iteration + 1
                add = randint(1,size)
                curr = curr + add
                printstr = "Iteration " + str(iteration) + ", Rolled  " + str(add)
                if add is not size:
                    stop = True
                else:
                    printstr = printstr + " Explode"
                if(display):
                    print(printstr)
                i = i + 1
        return curr
        
    def getAverage(self, num, size, precision):
        i = 0
        raw_avg = 0
        while(i < (10 ** precision)):
            raw_avg = raw_avg + self.roll(num,size, False)
            i = i+1
        end_avg = raw_avg / i
        return end_avg

    #this function gets the expected value for the number of dice rolled. 
    #on a single die, it can also account for die explosion
    def getExpected(self, size, number):
        explodes = (number == 1.0)
        i = 1.0
        expected = 0.0
        modifier = 1.0/size
        #modifier for dice explosion
        #taken from eric22222.wordpress.com: "A Mathematical analysis of Exploding Dice"        
        if(explodes):
            explosion = size / (size - 1.0)
        else:
            explosion = 1.0
        while(i <= size):
            expected = expected + (i * modifier)
            i = i+1
        return expected * explosion * number
        
        
roller = Roller(4)
