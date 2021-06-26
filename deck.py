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
        self.types = ["high", "mid", "low"]

        self.card = namedtuple("DevCards", field_names=["color", "symbol", "value", "requirement", "type"])
        # self.devcards = deque(maxlen= 90)
        self.highcards = deque(maxlen=30)
        self.midcards = deque(maxlen=30)
        self.lowcards = deque(maxlen=30)
        self.devcards = [self.highcards, self.midcards, self.lowcards]

        self.cardmemory = []
        self.__initcards()
    
    #Code by Kevin: https://stackoverflow.com/questions/34517540/find-all-combinations-of-a-list-of-numbers-with-a-given-sum
    def __getCombinations(self, n):
        numbers = [1, 2, 3, 4, 5, 6, 7]
        res = [seq for i in range(len(numbers), 0, -1) for seq in combinations(numbers, i) if sum(seq) == n]
        # res = [i for i in res if len(i) == 3 or len(i) == 4]
        print(res)

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
        reqs = [7, 8, 9]
        
        c_i = 0
        value = 3
        for i in range(90):
            # c = colors[c_i]
            c = np.random.choice(colors)
            s = np.random.choice(self.symbols)
            v = 3
            r = self.__retReq(reqs)
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
            if (i+1) % 3 == 0:
                c_i += 1
        
        return cards
    
    def drawCard(self, card):
        for i, type in enumerate(self.types):
            if card[-1] == type:
                return self.devcards[i].pop()
        # return self.devcards.pop()
     
    def drawCoin(self, coins):
        for i, keys in enumerate(self.m.keys()):
            self.m[keys] -= coins[i]

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