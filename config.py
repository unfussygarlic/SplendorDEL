from pygame.constants import BIG_ENDIAN


def getPlayerText(n):
    x, y = (100, 100)
    pad = 100

    pdict = {}

    for i in range(n):
        pdict[f"player{i}"] = (x, y)
        y += pad
    
    return pdict

colors = {"r": (255, 0, 0),
          "b": (0, 0, 255),
          "bl": (0, 0, 0),
          "w": (255, 255, 255),
          "g": (0, 255, 0)}

dim_colors = {"r": (200, 0, 0),
                "b": (0, 0, 200),
                "bl": (60, 60, 60),
                "w": (200, 200, 200),
                "g": (0, 200, 0)}

dimensions = {"coin": (100, 30, (500, 150), 30),
                "card": (9, 100, 150, (700, 150), 50),
                "player": (30, 30, (100, 150), 30),
                "turn": (1280//2 - 100, 30)}

BG_COLOR = (255, 170, 0)
# BG_COLOR = (150, 75, 0)
PURPLE = (128,0,128)