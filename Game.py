import pygame as pg

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
        self.Img = pg.image.load('Graphics\\40x40.jpg')
        self.Name = name
        self.Pos = pos


class game():
    def __init__(self, num_column, num_row):
        self.Arr_Intersects = [intersect(index+column, (100 + 200 * index, 100 + 200 * column)) for index in range(num_row) for column in range(num_column)]

    def show(self, screen):
        for inter in self.Arr_Intersects:
            screen.blit(inter.Img, inter.Pos)
