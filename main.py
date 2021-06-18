from numpy.core.fromnumeric import argmax
from display import display
from deck import deck
from player import player
from config import dimensions, BG_COLOR
from config import getPlayerText
import pygame
import numpy as np

pygame.init()
WIDTH = 1280
HEIGHT = 720
n_players = 5

disp = display(WIDTH, HEIGHT)
deck = deck(10)

players = []

for i in range(n_players):
    players.append(player())

print(players)
p1 = player()

running = True

cards = deck.getCards()
playercoords = getPlayerText(n_players, HEIGHT)

pidx = 0
cm = []

while running:

    if pidx >= n_players:
        pidx = 0

    cardmemory = deck.retMemory()
    playermemory = [i.retMemory() for i in players]

    disp.screen.fill(BG_COLOR)

    pos = pygame.mouse.get_pos()
    disp.hoverCoins(*dimensions["coin"], pos, cardmemory)
    disp.hoverCards(*dimensions["card"], pos, cards)
    # disp.dispPlayerCoins(*dimensions["player"], playermemory)
    # disp.dispPlayerText(player_text)
    disp.displayPlayerStats(playercoords, *dimensions["player"], playermemory)
    disp.dispTurn(pidx)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            coins = disp.getCoinEncoding(*dimensions["coin"], pos)

            cardidx, card = disp.getCardDetail(*dimensions["card"], pos, cards)

            if coins.any():
                # print(coins)
                cm.append(coins)
                if len(cm) == 2:
                    if np.argmax(cm[0]) == np.argmax(cm[1]):
                        print("same coin selected")
                        for i in range(len(cm)):
                            players[pidx].addCoins(cm[i])
                        cm = []
                        pidx += 1

                elif len(cm) == 3:
                    x, y, z = (np.argmax(cm[0]), np.argmax(cm[1]), np.argmax(cm[2]))
                    if x != y and y != z and x != z:
                        print("3 different coin selected")
                        for i in range(len(cm)):
                            players[pidx].addCoins(cm[i])
                        cm = []
                        pidx += 1

                    else:
                        for i in range(len(cm)):
                            deck.addCoin(cm[i])
                        print("Invalid Selection")
                        cm = []

            if card:
                buystat = players[pidx].checkBuy(card)
                if buystat:
                    players[pidx].addCards(card)
                    cards[cardidx] = deck.getCard()
                    pidx += 1

            # if sum(coins) > 0:
            #     pidx += 1
            deck.drawCoin(coins)
    
    pygame.display.update()