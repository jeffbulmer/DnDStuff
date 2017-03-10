# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 00:02:09 2017

@author: jeff
"""

import Edge
from random import randint

class edgeLibrary:
    
    def __init__(self):
        self.edges = {}
        self.populate()
        
    def selectAtRandom(self):
        return self.edges[randint(0,len(self.edges)-1)]
        
    def populate(self):
        self.edges = [Edge.Edge("Master Sprinter",{1:["attr", "vigor", "at least", 3], 2:["attr","strength","at least",5], 3:["edge","Fleet-Footed", "has", 0]}, "Through rigorous training, this character has gained the ability to run very fast. Permanent pace increase, and this character rolls a d12 at +2 when determining sprint distance", {1:["pace", 0, "plus", 2]}),
                      Edge.Edge("Sailor (Ace)",{1:["attr", "agility", "at least", 3],2:["skill","boating","at least",1]}, "Growing up around water, this character has become an expert sailor", {1:["skill", "boating", "plus", 2]}),
                      Edge.Edge("Acrobat",{1:["attr", "agility", "at least", 3], 2:["attr", "strength", "at least", 2]}, "The character is particularly limber. +2 to nimbleness-based Agility rolls", {1:["parry", "", "plus", 1]}),
                      Edge.Edge("Alertness",{1:["level", "", "at least", 0]}, "Not much gets by this character; he's very observant and perceptive.", {1:["skill", "notice", "plus", 2]}),
                      Edge.Edge("Ambidextrous",{1:["attr", "agility", "at least", 3]}, "Able to use both hands equally well. This character suffers no penalties when using a non-dominant hand.", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Arcane Resistance",{1:["attr", "spirit", "at least", 3]}, "This character has better than average resistance to magic. Add 2 armour against magic, +2 to resist magic effects", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Improved Arcane Resistance",{1:["Edge", "Arcane Resistance", "equal",0]}, "This character has even better resistance to magic. Add 4 armour against magic, +4 to resist magic effects (does not stack with Arcane Resistance)", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Assassin",{1:["attr", "agility", "at least", 3], 2:["skill","climbing","at least",2], 3:["skill", "fighting", "at least", 2], 4:["skill", "stealth", "at least", 3]}, "Possessing a very particular set of skills, this character is an expert killer. +2 damage when attacking an unaware foe", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Attractive",{1:["attr", "vigor", "at least", 2]}, "Easy on the eyes", {1:["charisma", "", "plus", 2]}),
                      Edge.Edge("Very Attractive",{1:["edge", "Attractive", "has", 0]}, "Very Easy on the eyes", {1:["charisma", "", "plus", 2]}),
                      Edge.Edge("Beast Master",{1:["attr", "spirit", "at least", 3]}, "This character is close to an animal familiar", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Beast Bond",{1:["edge", "Beast Master", "has", 0]}, "This character is so close to his/her familiar that the two share a benny pool", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Berserk",{1:["level", "", "at least", 0]}, "Immediately after suffering a wound, make a smarts roll, or go berserk. (See text for more)", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Block",{1:["level", "", "at least", 4], 2:["skill", "fighting", "at least", 3]}, "A skilled fighter, this character parries better than most", {1:["parry", "", "plus", 1]}),
                      Edge.Edge("Improved Block",{1:["level", "", "at least", 8], 2:["edge", "Block","has", 0]}, "A true warrior, this character's defenses are nigh-impenetrable", {1:["parry", "", "plus", 1]}),
                      Edge.Edge("Brave",{1:["attr", "spirit", "at least", 2]}, "Unshaken by terror, this character is so badass s/he watches horror movies for fun. +2 to fear checks", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Brawler",{1:["attr", "strength", "at least", 2]}, "A pugilist at heart, this character gains +2 damage on unarmed attacks", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Bruiser",{1:["edge", "Brawler", "has", 0]}, "A real heavy hitter. Does d8 instead of d6 damage on unarmed rolls", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Brawny",{1:["attr", "strength", "at least", 2], 2:["attr", "vigor", "at least", 2]}, "A real tough cookie, this character can take a beating. This chatacter can also carry eight times their strength", {1:["toughness", "", "plus", 1]}),
                      Edge.Edge("Charismatic",{1:["attr", "spirit", "at least", 3]}, "This character is a fantastic social presence.", {1:["charisma", "", "plus", 2]}),
                      Edge.Edge("Combat Reflexes",{1:["level", "", "at least", 4]}, "You can't keep a good man down. This character gains +2 to recover from being Shaken", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Command",{1:["attr", "smarts", "at least", 2]}, "A natural leader, troops under this character's command gain +1 to recover from being Shaken", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Connections",{1:["level", "", "at least", 0]}, "This character has friends in high places.", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Counterattack",{1:["level", "", "at least", 4], 2:["skill","fighting","at least",3]}, "Combat ready, this character is able to strike immediately after parrying an attack (free, at -2)", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Improved Counterattack",{1:["level", "", "at least", 8], 2:["edge","Counterattack","has",0]}, "Trying to attack but failing to kill this character could be a deadly mistake. No penalty on counterattack", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Danger Sense",{1:["level", "", "at least", 0]}, "This character can sense when things are about to get bad. Free notice roll at -2 to detect ambush/surprise", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Dodge",{1:["level", "", "at least", 4], 2:["attr","agility","at least",3]}, "This character is able to move out of the way of projectiles. -1 to being hit with ranged attacks", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Improved Dodge",{1:["level", "", "at least", 8],2:["edge","Dodge","has",0]}, "Bullets are my friends. I've studied them; learned their ways. (-2 to being hit with ranged attacks", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Elan",{1:["attr", "spirit", "at least", 3]}, "When s/he sets his/her mind to something, this character is a force to be recconed with. +2 when spending a Benny on a trait roll", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Extraction",{1:["attr", "agility", "at least", 3]}, "When the going gets tough, this character gets going. Ignore a foe's free attack when withdrawing from melee with an agility roll", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Improved Extraction",{1:["edge", "Extraction", "has", 0]}, "When the going gets tough, you've already left. Same a 'Extraction', but on a raise, ignore all free attacks.", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Fast Healer",{1:["attr", "vigor", "at least", 3]}, "It's just a flesh wound. This character gains a +2 to natural healing rolls", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Fervor",{1:["level", "", "at least", 8], 2:["attr", "spirit","at least",3], 3:["edge","Command", "has", 0]}, "Troops under this character's command gain +1 to all melee damage", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("First Strike",{1:["attr", "agility", "at least", 3]}, "To get too close would be unwise. This character can attack one foe who moves adjacent for free.", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Improved First Strike",{1:["level", "", "at least", 12],2:["edge","First Strike","has",0]}, "Do not engage! This character can attack any foe who moves adjacent for free", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Fleet-Footed",{1:["attr", "agility", "at least", 2]}, "This character never skips leg day. Roll a d10 to determine sprint distance, instead of a d6", {1:["pace", "", "plus", 2]}),
                      Edge.Edge("Florentine",{1:["attr", "agility", "at least", 3]}, "This character knows exactly how to hurt someone not carrying a shield. +1 vs. foes carrying only a single one-handed weapon, no shield. Ignore 1 point of gang-up bonus", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Frenzy",{1:["level", "", "at least", 4], 2:["skill","fighting","at least", 4]}, "Once this character gets going, there's no stopping him/her. 1 extra fighting attack at -2", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Improved Frenzy",{1:["level", "", "at least", 8], 2:["edge","Frenzy","has",0]}, "This character gains an additional fighting attack without penalty", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Gadgeteer",{1:["level", "", "at least", 0]}, "A tech wiz! This character may 'jury-rig' a device once per session", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Giant Killer",{1:["level", "", "at least", 4]}, "How does one kill a giant? This character knows the answer. +1d6 damage when attacking large creatures (anything with size +2 or greater)", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Healer",{1:["attr", "spirit", "at least", 3]}, "This character knows his/her way around a medical kit. ", {1:["skill", "healing", "plus", 2]}),
                      Edge.Edge("Hold the Line!",{1:["level", "", "at least", 4], 2:["attr","smarts","at least", 3], 3:["edge","Command", "has", 0]}, "They Shall not pass! Troops under this character's command gain +1 Toughness", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Improvisational Fighter",{1:["level", "", "at least", 4], 2:["attr", "smarts", "at least", 2]}, "The key to winning a barfight is to realize that everything is a weapon. Ignore penalties for improvised weapons", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Inspire",{1:["level", "", "at least", 4], 2:["edge", "Command","has",0]}, "'Natural Leader' is an understatement. Troops love this character. Troops gain +1 to Spirit rolls", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Jack-of-all-Trades",{1:["attr", "smarts", "at least", 4]}, "Ain't nothing this character can't do. No -2 on unskilled smarts tests", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Killer Instinct",{1:["level", "", "at least", 12]}, "Wins tied opposed rolls, may reroll oposed skill die if it comes up 1", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Leader of Men",{1:["level", "", "at least", 8], 2:["edge", "Command","has", 0]}, "I don't know if you've heard, but this character is a natural leader. Subordinates gain a d10 wild die", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Level Headed",{1:["level", "", "at least", 4], 2:["attr","smarts", "at least",3]}, "In combat, this character draws two cards, and acts on the best of these", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Improved Level Headed",{1:["level", "", "at least", 4], 2:["edge", "Level Headed", "has", 0]}, "In combat, this character draws three cards, and acts on the best of these", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Liquid Courage",{1:["attr", "vigor", "at least", 3]}, "After one or two beers, this character is just drunk enough to drive. Gain vigor die type after imbibing at least 8 oz of alcohol", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Lucky",{1:["level", "", "at least", 0]}, "This character has one additional benny per session", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Very Lucky",{1:["edge", "Lucky", "has", 0]}, "This character has two additional bennies per session", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Marksman",{1:["level", "", "at least", 4]}, "An unskilled shooter pulls the trigger. A Marksman aims. Gain +2 shooting by taking a turn to aim.", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Martial Artist",{1:["skill", "fighting", "at least", 2]}, "Unarmed? I've got arms, don't I? +d4 to all unarmed rolls", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Improved Martial Artist",{1:["level", "", "at least", 8],2:["edge","Martial Artist","has",0],3:["skill", "fighting", "at least", 4]}, "This character is a regular Danny Rand. +d6 to unarmed damage rolls, instead of d4", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Martial Arts Master",{1:["level", "", "at least", 16], 2:["edge","Improved Martial Artist", "has", 0], 3:["skill", "fighting", "at least", 5]}, "The Fu Manchu of his people, this character gains +2 to unarmed damage rolls. This edge may be taken up to 5 times.", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("McGyver",{1:["attr", "smarts", "at least", 2], 2:["skill","repair", "at least",2],3:["skill", "notice", "at least", 3]}, "Gum, a paperclip and 4 blades of grass? I can make a gun out of that. This character may improvise temporary gadgets.", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Natural Leader",{1:["attr", "spirit", "at least", 3], 2:["edge","Command","has", 0]}, "By the very definition of the phrase, this character is a natural leader.",{1:["parry", "", "plus", 0]}),
                      Edge.Edge("No Mercy",{1:["level", "", "at least", 4]}, "This character may spend bennies on damage rolls", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Quick",{1:["level", "", "at least", 0]}, "Is it go time? It's go time! This character may discard a draw of 5 or less for a new card.", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Quick Draw",{1:["attr", "agility", "at least", 3]}, "This character may draw a weapon as a free action", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Scavenger",{1:["edge", "Luck", "has", 0]}, "A lifetime of dumpster-diving has prepared this character for just such a moment. This character finds an essential piece of equipment once per session", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Sweep",{1:["attr", "strength", "at least", 3],2:["skill","fighting","at least", 3]}, "Best to attack this character from afar. This character may attack all adjacent foes at a -2", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Improved Sweep",{1:["edge", "Sweep", "has", 0]}, "You really should shoot this guy. No penalty when attacking all adjacent foes.", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Strong Willed",{1:["skill", "intimidate", "at least", 2],2:["skill", "taunt", "at least", 2]}, "An unshakeable moral paragon, this character is strong in his/her convictions. +2 to resist tests of will.", {1:["skill", "taunt", "plus", 2], 2:["skill", "intimidate", "plus", 2]}),
                      Edge.Edge("Thief",{1:["attr", "agility", "at least", 3],2:["skill","climbing","at least", 2], 3:["skill","lockpicking","at least", 2], 4:["skill","stealth","at least",3]}, "You have no idea the effort that goes into stealing something... but this character does +2 to disarm traps", {1:["skill", "climbing", "plus", 2], 2:["skill", "lockpicking", "plus", 2], 3:["skill", "stealth", "plus", 2]}),
                      Edge.Edge("Tough as Nails",{1:["level", "", "at least", 16]}, "This edge is misleading. Nails aren't really all that tough, at least not compared to this character.", {1:["toughness", "", "plus", 1]}),
                      Edge.Edge("Improved Tough as Nails",{1:["edge", "Tough as Nails", "has", 0]}, "This edge is misleading. This character isn't really all that tough, at least not compared to this character.", {1:["toughness", "", "plus", 1]}),
                      Edge.Edge("Two-Fisted",{1:["attr", "agility", "at least", 3]}, "This character may attack with a weapon in each hand without penalty", {1:["parry", "", "plus", 0]}),
                      Edge.Edge("Weapon Master",{1:["level", "", "at least", 16],2:["skill","fighting","at least", 5]}, "If you've a weapon, this character can use it.", {1:["parry", "", "plus", 1]}),
                      Edge.Edge("Improved Weapon Master",{1:["edge", "Weapon Master", "has", 0]}, "If you've a weapon, this character has mastered it.", {1:["parry", "", "plus", 1]}),
                      Edge.Edge("Woodsman",{1:["attr", "spirit", "at least", 2], 2:["skill", "survival", "at least", 3], 3:["skill","tracking", "at least", 3]}, "At home in the forest, this character gains special bonuses when in the wilderness", {1:["skill", "survival", "plus", 2], 2:["skill","tracking","plus",2],3:["skill","stealth","plus",2]})
                      ]