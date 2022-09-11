import pygame as pg
import Camera as cm
from random import randint, choices

class car():
    def __init__(self, id, color):
        self.ID = id
        self.Color = color

class street():
    def __init__(self, name, start, end, p_s, p_e):
        self.Name = name
        self.Start = start
        self.End = end
        self.pos_start = p_s
        self.pos_end = p_e

    def blit(self, screen):
        f3 = pg.font.Font(None, 30)
        stroka = ''
        for elm in self.Streets:
            stroka += ',' + elm.Name
        sosedi = f3.render(stroka, True, (180, 0, 0))
        # res = tuple(map(lambda i, j: i - j, test_tup1, test_tup2))
        print(self.pos_start, self.pos_end)
        screen.blit(sosedi, (self.Pos[0]-20, self.Pos[1]-20))

class intersect():
    def __init__(self, name, pos):
        self.Img = pg.image.load('Graphics\\50x50.jpg')
        self.Name = name
        self.Pos = pos
        self.Streets = []
        self.index_Streets = []

    def blit(self, screen):
        screen.blit(self.Img, self.Pos)
        f1 = pg.font.Font(None, 50)
        f2 = pg.font.Font(None, 30)
        text = f1.render(str(self.Name), True, (180, 0, 0))
        # sosedi = f2.render(",".join(map(str, self.index_Streets)), True, (180, 0, 0))
        screen.blit(text, (self.Pos[0]+10, self.Pos[1]+10))
        # screen.blit(sosedi, (self.Pos[0]-20, self.Pos[1]-20))

        f3 = pg.font.Font(None, 30)
        stroka = ''
        for elm in self.Streets:
            stroka += ',' + elm.Name
            print(elm.pos_start, elm.pos_end)
            print(tuple(map(lambda i, j: i - j, elm.pos_end, elm.pos_start)))
            pg.draw.line(screen, (255, 0, 0), elm.pos_start, elm.pos_end)
        sosed = f3.render(stroka, True, (180, 0, 0))
        # res = tuple(map(lambda i, j: i - j, test_tup1, test_tup2))

        screen.blit(sosed, (self.Pos[0]-20, self.Pos[1]-20))



class game():
    def __init__(self, num_column, num_row):
        self.Arr_Streets = []
        self.Arr_Intersects = [intersect(None, (50 + 200 * index, 50 + 200 * column)) for index in range(num_row) for column in range(num_column)]
        indx = 1
        for inter in self.Arr_Intersects:
            inter.Name = indx
            indx += 1
        for inter in self.Arr_Intersects:
            if(inter.Name - num_row > 0):
                inter.index_Streets.append(inter.Name - num_row)
            if(inter.Name + num_row <= num_row*num_column):
                inter.index_Streets.append(inter.Name + num_row)
            if((inter.Name % num_column == 0) or (inter.Name % num_row == 0)):
                if(inter.Name - 1 > 0):
                    inter.index_Streets.append(inter.Name - 1)
            elif((inter.Name % num_column == 1) or (inter.Name % num_row == 1)):
                if(inter.Name + 1 <= num_row*num_column):
                    inter.index_Streets.append(inter.Name + 1)
            else:
                if(inter.Name + 1 <= num_row*num_column):
                    inter.index_Streets.append(inter.Name + 1)
                if(inter.Name - 1 > 0):
                    inter.index_Streets.append(inter.Name - 1)
            # print(inter.Name, inter.index_Streets)
        self.init_streets()




    def init_streets(self):
        for inter in self.Arr_Intersects:
            for indx in inter.index_Streets:
                name = str(inter.Name) + '-' + str(indx)
                # print(name)
                inter.Streets.append(street(name, inter.Name, indx, inter.Pos, self.Arr_Intersects[indx-1].Pos))
            # else:
            #     for elm in choices(inter.index_Streets, k=randint(1, len(inter.index_Streets))):
            #         name = str(inter.Name) + '-' + str(elm)
            #         inter.Streets.append(street(name, inter.Name, elm))

    def show(self, screen):
        for inter in self.Arr_Intersects:
            inter.blit(screen)
            # screen.blit(inter.Img, inter.Pos)
