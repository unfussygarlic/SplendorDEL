from os import name
import numpy as np
from collections import deque, namedtuple
from itertools import product, combinations

from numpy import random

class deck(object):

    def __init__(self, n_coins):

        self.m = {"r": n_coins,
                        "b": n_coins,
                        "bl": n_coins,
                        "w": n_coins,
                        "g": n_coins}
        
        self.symbols = ["r", "b", "bl", "w", "g"]
        self.card = namedtuple("DevCards", field_names=["color", "symbol", "value", "requirement"])
        self.devcards = deque(maxlen= 90)
        # self.highcards = deque(maxlen=30)
        # self.midcards = deque(maxlen=30)
        # self.lowcards = deque(maxlen=30)
        # self.devcards = [self.highcards, self.midcards, self.lowcards]

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
            dc = self.card(c, s, v, r)
            self.devcards.append(dc)
            if (i+1) % 30 == 0:
                c_i += 1

    def getCards(self):
        cards = []
        random.shuffle(self.devcards)
        for i in range(9):
            card = self.devcards.pop()
            cards.append(card)
        
        return cards
    
    def getCard(self):
        return self.devcards.pop()

            
    def drawCoin(self, coins):
        for i, keys in enumerate(self.m.keys()):
            self.m[keys] -= coins[i]
        
    def drawCard(self, color):
        pass

    def addCoin(self, coins):
        for i, keys in enumerate(self.m.keys()):
            self.m[keys] += coins[i]
    
    def retMemory(self):
        return self.m
        
    def __len__(self):
        return len(self.devcards)
    
    def nonNegativeCheck(self):
        for key in self.m:
            if self.m[key] < 0:
                self.m[key] = 0