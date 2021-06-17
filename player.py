import numpy as np

class player(object):

    def __init__(self):

        self.m = {"r": 0,
                "b": 0,
                "bl": 0,
                "w": 0,
                "g": 0}
        
        self.points = 0
        
    def addCoins(self, coins):
        for i, keys in enumerate(self.m.keys()):
            self.m[keys] += coins[i]
    
    def addCards(self, card):
        for keys in self.m.keys():
            if card[1] == keys:
                self.m[keys] += 1
        
        self.points += card[2]
    
    def checkBuy(self, card):
        reqs = card[-1]
        counter = 0
        for keys in reqs.keys():
            if self.m[keys] >= reqs[keys]:
                counter += 1
        
        return counter
    
    def retMemory(self):
        return self.m
    
    def retPoints(self):
        return self.points
    
    def showCoins(self):
        print(self.m)