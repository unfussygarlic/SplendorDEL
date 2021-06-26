from os import name
import numpy as np
from collections import deque, namedtuple
from itertools import product, combinations

from numpy import random
from numpy.lib.function_base import select

class deck(object):

    def __init__(self, n_coins):

        self.m = {"r": n_coins,
                        "b": n_coins,
                        "bl": n_coins,
                        "w": n_coins,
                        "g": n_coins}
        
        self.symbols = ["r", "b", "bl", "w", "g"]
        self.types = ["high", "mid", "low"]

        self.card = namedtuple("DevCards", field_names=["color", "symbol", "value", "requirement", "type"])
        # self.devcards = deque(maxlen= 90)
        self.highcards = deque(maxlen=30)
        self.midcards = deque(maxlen=30)
        self.lowcards = deque(maxlen=30)
        self.devcards = [self.highcards, self.midcards, self.lowcards]

        #currect deck
        self.cd = []

        self.cardmemory = []
        self.__initcards()
    
    #Code by Kevin: https://stackoverflow.com/questions/34517540/find-all-combinations-of-a-list-of-numbers-with-a-given-sum
    def __getCombinations(self, n):
        numbers = [1, 2, 3, 4, 5, 6, 7]
        res = [seq for i in range(len(numbers), 0, -1) for seq in combinations(numbers, i) if sum(seq) == n]
        return res
    
    def __retReq(self, r):
        choice = np.random.choice(r)
        comb = np.random.choice(self.__getCombinations(choice))
        req = {}
        n_sym = len(comb)
        symbols = np.random.choice(self.symbols, n_sym)
        for i in range(len(symbols)):
            req[symbols[i]] = comb[i]
        
        return req
        
    def __initcards(self):
        colors = ["b", "y", "o"]
        reqs = [[3, 4, 5], [6, 7, 8], [7, 8, 9, 10, 11, 12]]
        
        c_i = 0
        values = [[0, 0], [1,2], [3, 4]]
        for i in range(90):
            # c = colors[c_i]
            c = np.random.choice(colors)
            s = np.random.choice(self.symbols)
            v = np.random.choice(values[c_i])
            r = self.__retReq(reqs[c_i])
            t = self.types[c_i]
            dc = self.card(c, s, v, r, t)
            self.devcards[c_i].append(dc)
            if (i+1) % 30 == 0:
                c_i += 1

    def shuffleCards(self):
        for i in range(len(self.devcards)):
            random.shuffle(self.devcards[i])

    def drawCards(self):
        cards = []
        # random.shuffle(self.devcards)
        self.shuffleCards()
        c_i = 0
        for i in range(9):
            card = self.devcards[c_i].pop()
            cards.append(card)
            self.cd.append(card)
            if (i+1) % 3 == 0:
                c_i += 1
        
        return cards
    
    def drawCard(self, card):

        for i, type in enumerate(self.types):
            if card[-1] == type:
                next_card = self.devcards[i].pop()
                break
            break
        
        for i in range(len(self.cd)):
            # if card[0] == self.cd[i][0] and card[1] == self.cd[i][1]:
            if card == self.cd[i]:
                self.cd[i] = next_card
        
        return next_card
                # return self.devcards[i].pop()
        # return self.devcards.pop()
     
    def drawCoin(self, coins):
        for i, keys in enumerate(self.m.keys()):
            self.m[keys] -= coins[i]

    def addCoin(self, coins):
        for i, keys in enumerate(self.m.keys()):
            self.m[keys] += coins[i]
    
    def retMemory(self):
        return self.m
    
    def printCD(self):
        colors = [i[1] for i in self.cd]
        print(colors)

    def retCards(self):
        return self.cd
        
    def __len__(self):
        return len(self.devcards)
    
    def nonNegativeCheck(self):
        for key in self.m:
            if self.m[key] < 0:
                self.m[key] = 0