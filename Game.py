import pygame as pg
import Camera as cm

class car():
    def __init__(self, id, color):
        self.ID = id
        self.Color = color

class street():
    def __init__(self, name, start, end):
        self.Name = name
        self.Start = start
        self.End = end

class intersect():
    def __init__(self, name, pos):
        self.Img = pg.image.load('Graphics\\50x50.jpg')
        self.Name = name
        self.Pos = pos
        self.Streets = []

    def blit(self, screen):
        screen.blit(self.Img, self.Pos)
        f1 = pg.font.Font(None, 50)
        f2 = pg.font.Font(None, 30)
        text = f1.render(str(self.Name), True, (180, 0, 0))
        sosedi = f2.render(",".join(map(str, self.Streets)), True, (180, 0, 0))
        screen.blit(text, (self.Pos[0]+10, self.Pos[1]+10))
        screen.blit(sosedi, (self.Pos[0]-20, self.Pos[1]-20))



class game():
    def __init__(self, num_column, num_row):
        self.Arr_Intersects = [intersect(None, (50 + 200 * index, 50 + 200 * column)) for index in range(num_row) for column in range(num_column)]
        indx = 1
        for inter in self.Arr_Intersects:
            inter.Name = indx
            indx += 1
        for inter in self.Arr_Intersects:
            # if(inter.Name - num_row > 0):
            #     inter.Streets.append(inter.Name - num_row)
            # if(inter.Name + num_row <= num_row*num_column):
            #     inter.Streets.append(inter.Name + num_row)
            if((inter.Name % num_column == 0) or (inter.Name % num_row == 0)):
                if(inter.Name - 1 > 0):
                    inter.Streets.append(inter.Name - 1)
            if((inter.Name % num_column == 1) or (inter.Name % num_row == 1)):
                if(inter.Name + 1 <= num_row*num_column):
                    inter.Streets.append(inter.Name + 1)
            # else:
            #     if(inter.Name + 1 <= num_row*num_column):
            #         inter.Streets.append(inter.Name + 1)
            #     if(inter.Name - 1 > 0):
            #         inter.Streets.append(inter.Name - 1)



    def show(self, screen):
        for inter in self.Arr_Intersects:
            inter.blit(screen)
            # screen.blit(inter.Img, inter.Pos)
