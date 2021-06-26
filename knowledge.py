from player import player
import numpy as np
from itertools import combinations

# class knowledge(object):

#     def __init__(self, deck):
#         self.colors = ["r", "b", "bl", "w", "g"]
#         self.deck = deck
#         self.getCoinWorlds = self.getCoinWorlds()
#         # for player in players:
#         #     print(player.retOverallMemory())
#         # print(self.getCoinWorlds())
    
#     def getCoinWorlds(self):
#         thrice = list(combinations(self.colors, r = 3))
#         twice = []
#         for i in self.colors:
#             twice.append((i, i))
        
#         return thrice + twice
    
#     def updateInfo(self, deck, players):
#         self.deck = deck
        
class coinKnowledge(object):

    def __init__(self, n_players, coins):
        self.colors = ["r", "b", "bl", "w", "g"]
        self.worlds = []
    
    def separateCoins(self, coins):
        high_coins = []
        low_coins = []
        null_coins = []
        for keys in coins.keys():
            if coins[keys] > 1:
                high_coins.append(keys)
            elif coins[keys] == 1:
                low_coins.append(keys)
            else:
                null_coins.append(keys)
        
        return high_coins, low_coins, null_coins

    def getCombinations(self, colors, t):
        if t == 3:
            thrice = list(combinations(colors, r = 3))
            return thrice
        if t == 2:
            twice = []
            for i in colors:
                twice.append((i, i))
            return twice

    def filterCoin(self, combinations, coin):
        filter = []
        for comb in combinations:
            if coin in comb:
                filter.append(comb)
        
        return filter
    
    def getCoinWorlds(self, coins):
        worlds = []
        high, low, null = self.separateCoins(coins)
        if high:
            worlds += self.getCombinations(high, 3)
            worlds += self.getCombinations(high, 2)
        if low:
            for coin in low:
                low_set = high + [coin]
                unfiltered = self.getCombinations(low_set, 3)
                worlds += self.filterCoin(unfiltered)
        
        return worlds

    def updateKnowledge(self, coins, deck, players):
        coinworlds = self.getCoinWorlds(coins)
        print(coinworlds)
        # print(f"worlds: {worlds}")