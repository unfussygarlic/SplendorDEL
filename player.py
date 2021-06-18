import numpy as np

class player(object):

    def __init__(self):

        self.coinmem = {"r": 0,
                "b": 0,
                "bl": 0,
                "w": 0,
                "g": 0}
        
        self.cardmem = {"r": 0,
                        "b": 0,
                        "bl": 0,
                        "w": 0,
                        "g": 0}
        
        self.points = 0
        
    def addCoins(self, coins):
        for i, keys in enumerate(self.coinmem.keys()):
            self.coinmem[keys] += coins[i]
    
    def addCards(self, card, type = "card"):
        for keys in self.cardmem.keys():
            if card[1] == keys:
                self.cardmem[keys] += 1
        
        if type == "coin":
            reqs = card[-2]
            for keys in reqs.keys():
                self.coinmem[keys] -= reqs[keys]
        
        self.points += card[2]
    
    def checkBuy(self, card):
        reqs = card[-2]
        coincounter = 0
        cardcounter = 0

        for keys in reqs.keys():
            if self.coinmem[keys] >= reqs[keys]:
                coincounter += 1
            
            if self.cardmem[keys] >= reqs[keys]:
                cardcounter += 1
        
        if cardcounter > 0:
            return (True, "card")
        
        elif coincounter > 0:
            return (True, "coin")
        
        else:
            return (False, None)
        
        # return True if counter > 0 else False
    
    def retCoinMemory(self):
        return self.coinmem
    
    def retCardMemory(self):
        return self.cardmem
    
    def retPoints(self):
        return self.points
    
    def showCoins(self):
        print(self.m)
    
    def nonNegativeCheck(self):
        for key in self.coinmem:
            if self.coinmem[key] < 0:
                self.coinmem[key] = 0
            if self.cardmem[key] < 0:
                self.cardmem[key] = 0