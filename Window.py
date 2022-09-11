import pygame as pg
from Game import game

def ClickBt():
    if(self.bt_exit.pressed(pg.mouse.get_pos())):
        print ("bt_exit")
        sys.exit()
    if(self.bt_new.pressed(pg.mouse.get_pos())):
        print("bt_new")
        return True
    else:
        return False

pg.init()
#screen = pg.display.set_mode((0,0),pg.FULLSCREEN,pg.HWSURFACE)
# screen = pg.display.set_mode((0,0),pg.FULLSCREEN)
screen = pg.display.set_mode((800,600),pg.RESIZABLE)
#screen = pg.display.set_mode((1280,1024),pg.FULLSCREEN)
# pg.display.set_caption('Mafia')
# icon = pg.image.load('images\\icon.bmp')
# pg.display.set_icon(icon)
while True:
    pg.time.delay(50)
    for event in pg.event.get():
        if event.type == pg.QUIT: #if close
            sys.exit()

        if event.type == pg.MOUSEBUTTONUP:
            if(ClickBt()== True):
                pg.display.update()
                pg.mixer.music.stop()
                break

    # screen.blit(pg.image.load('Graphics\\16.jpg'), (400, 300))
    new_game = game(4,4)
    new_game.show(screen)


    # screen.blit(background,(0,0))
    # buttons.UpdateBt()
    # buttons.CheckBt()
    pg.display.update()
