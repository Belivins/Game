import pygame as pg
import Game as gm
import Handler as hn

pg.init()
screen = pg.display.set_mode((1080,920),pg.RESIZABLE)
newGame = gm.game(4, 4)



while True:
    hn.CheckEvent()
    newGame.show(screen)
    pg.display.update()

# hn.CheckEvent()
# newGame.show(screen)
# pg.display.update()
