from display import display
from deck import deck
from player import player
from config import dimensions, BG_COLOR
from config import getPlayerText
import pygame

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

while running:

    cardmemory = deck.retMemory()
    playermemory = [i.retMemory() for i in players]

    disp.screen.fill(BG_COLOR)

    pos = pygame.mouse.get_pos()
    disp.hoverCoins(*dimensions["coin"], pos, cardmemory)
    disp.hoverCards(*dimensions["card"], pos, cards)
    # disp.dispPlayerCoins(*dimensions["player"], playermemory)
    # disp.dispPlayerText(player_text)
    disp.displayPlayerStats(playercoords, 30, 30, 30, playermemory)
    disp.dispTurn(1)

    pidx = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            coins = disp.getCoinEncoding(*dimensions["coin"], pos)

            cardidx, card = disp.getCardDetail(*dimensions["card"], pos, cards)

            if card:
                buystat = players[pidx].checkBuy(card)
                print(buystat)
                if buystat:
                    players[pidx].addCards(card)
                    cards[cardidx] = deck.getCard()

            # if sum(coins) > 0:
            #     pidx += 1
            deck.drawCoin(coins)
            players[pidx].addCoins(coins)
    
    pygame.display.update()