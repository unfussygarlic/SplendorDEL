import numpy as np
import pygame
from collections import deque, namedtuple

from config import colors, dim_colors, dimensions
from config import BG_COLOR, PURPLE

class display(object):

    def __init__(self, width, height):
        self.screen = pygame.display.set_mode((width, height))
        self.cc = ["r", "b", "bl", "w", "g"]

        self.coinfont = pygame.font.Font(None, 20)
        self.playerfont = pygame.font.Font(None, 40)
        self.deck = deque(maxlen=9)
    
    def hoverCoins(self, w, h, coords, pad, pos, memory):
        posx, posy = pos
        x, y = coords
        memory = {x:y for x,y in memory.items() if y!=0}

        for i, keys in enumerate(memory.keys()):
            if x <= posx <= (x + w) and y <= posy <= y + h:
                pygame.draw.rect(self.screen, dim_colors[self.cc[i]], (x, y, w, h))
            else:
                pygame.draw.rect(self.screen, colors[self.cc[i]], (x, y, w, h))
            
            cpad = 5
            center = ((x + (x+w))/2 - cpad, (y+ (y+h))/2 - cpad)
            text = self.coinfont.render(f"{memory[keys]}", True, PURPLE)
            self.screen.blit(text, center)

            y += (h+pad)
    
    def getCardCoords(self, coords, w, h):
        x, y = coords
        sc = (x+10, y+10, 10, 10)
        vc = (x + w - 20, y + h - 20)
        
        ypad = 30
        cw = 20
        ch = 20
        rc = ((x+10, y+30, cw, ch), (x+w-10-cw, y+30, cw, ch), (x+10, y+30+ypad, ch, ch), (x+w-10-cw, y+30+ypad, ch, cw))
        # rcc = (())

        return (sc, vc, rc)
    
    def dispCard(self, coords, w, h, card, color):
        sc, vc, rc = self.getCardCoords(coords, w, h)
        
        pygame.draw.rect(self.screen, color[card[1]], sc)
        
        value = self.coinfont.render(f"{card[2]}", True, PURPLE)
        self.screen.blit(value, vc)

        for idx, keys in enumerate(card[-1].keys()):
            pygame.draw.rect(self.screen, color[keys], rc[idx])
    
    def hoverCards(self, n, w, h, coords, pad, pos, cards):
        x, y = coords
        posx, posy = pos
        c_i = 0

        for i in range(n):
            card = cards[i]
            if x <= posx <= (x + w) and y <= posy <= y + h:
                pygame.draw.rect(self.screen, dim_colors["w"], (x, y, w, h))
                self.dispCard((x,y), w, h, card, colors)
            else:
                pygame.draw.rect(self.screen, colors["w"], (x, y, w, h))
                self.dispCard((x, y), w, h, card, dim_colors)

            x += (w + pad)

            if (i+1) % 3 == 0:
                c_i += 1
                y += (h + pad)
                x = coords[0]
    
    def getCardDetail(self, n, w, h, coords, pad, pos, cards):
        x, y = coords
        posx, posy = pos

        for i in range(n):
            if x <= posx <= (x + w) and y <= posy <= y + h:
                card = cards[i]
                return i, card
            
            x += (w+pad)
            if (i+1)%3 == 0:
                y += (h+pad)
                x = coords[0]
        return None, None
    
    def getCoinEncoding(self, w, h, coords, pad, pos):
        encoding = np.zeros(len(self.cc), dtype = np.int)
        posx, posy = pos
        x, y = coords
        for i in range(len(self.cc)):
            if x <= posx <= (x + w) and y <= posy <= y + h:
                encoding[i] = 1
            
            y += (h+pad)
        
        return encoding
    
    def dispPlayerCoins(self, w, h, coords, pad, memory):
        x, y = coords
        memory = {x:y for x,y in memory.items() if y!=0}

        for idx, keys in enumerate(memory.keys()):
            pygame.draw.rect(self.screen, colors[keys], (x, y, w, h))

            cpad = 5
            text = self.coinfont.render(f"{memory[keys]}", True, PURPLE)
            center = ((x + (x+w))/2 - cpad, (y+ (y+h))/2 - cpad)
            self.screen.blit(text, center)

            x += (w + pad)
        
    def dispPlayerText(self, coords):

        for i, keys in enumerate(coords.keys()):
            text = self.playerfont.render(f"Player {i+1}", True, PURPLE)
            self.screen.blit(text, coords[keys])
    
    def dispTurn(self, i):
        text = self.playerfont.render(f"Player {i+1}'s Turn", True, PURPLE)
        self.screen.blit(text, dimensions["turn"])