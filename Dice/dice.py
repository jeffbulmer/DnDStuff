# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 14:44:27 2017

@author: robert
"""



import random
import matplotlib.pyplot as plt
import numpy as np

takeAverage = False
explodingDice = False
input_string = ''
end = False

def parseCommands():
    global takeAverage
    global explodingDice
    global input_string
    global end
    if (input_string.find("--average") != -1):
        takeAverage = True
        input_string = input_string.replace("--average", "")
    if (input_string.find("--exploding") != -1):
        explodingDice = True
        input_string = input_string.replace("--exploding", "")
    if (input_string.find("--end") != -1):
        end = True
        input_string = input_string.replace("--end", "")
        

def parseRoll(roll_string, exploding):
    result = 0;
    for newroll in (roll_string.rsplit("+")):
        newroll = newroll.strip(" ")
        if (newroll[0] == "d"):
           result +=  roll(int(newroll.split("d")[1]), exploding)
        elif (len(newroll.split("d")) == 1):
            result += int(newroll.split("d")[0])
        else:
            numrolls = int(newroll.split("d")[0])
            dyetype = int(newroll.split("d")[1])
            for i in range(0, numrolls):
                result += roll(dyetype, exploding)
    return result
  
def roll(roll_to, exploding):
    rolled = random.randint(1, roll_to)
    if exploding:
        explodeRoll = roll_to
    else:
        explodeRoll = 0
    if rolled == explodeRoll:
        return rolled + roll(roll_to, True)
    else:
        return rolled
  
def parseAverage(roll_string, exploding):
    result = 0
    for newroll in (roll_string.rsplit("+")):
        newroll = newroll.strip(" ")
        if (newroll[0] == "d"):
            result += calcAverage(1, int(newroll.split("d")[1]), exploding)
            
        elif (len(newroll.split("d")) == 1):
            result += int(newroll.split("d")[0])
            
        else:
            result += calcAverage(int(newroll.split("d")[0]), int(newroll.split("d")[1]), exploding)
    return "%.1f" % result

def calcAverage(numrolls, dye, exploding):
    result = 0
    for i in range(0, 100000):
        result += roll(dye, exploding)
    return (result / 100000.0) * numrolls
  


while (not end):   

    takeAverage = False
    explodingDice = False               
    input_string = raw_input("Enter Dice Command: ")
    
    parseCommands()
    if input_string.strip(' ') != '':
        if (takeAverage):
                print "AVERAGE: ", parseAverage(input_string, explodingDice)
        else:
            print "Your Roll: ", parseRoll(input_string, explodingDice)
