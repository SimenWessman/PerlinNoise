import numpy as np
import pygame as pg

def pixel(surface, color, pos):
    surface.fill(color, (pos, (1, 1)))

class Cell:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    

class Grid:
    def __init__(self, width, height, cellcount):
        self.width = width
        self.height = height
        self.cellcount = cellcount

        self.cellSize = (width / cellcount, height / cellcount)

    # Use this function to draw the grid lines.
    def draw(self, surface):
        # Then draw each cell:
        for i in range(0, self.cellcount):
            for j in range(0, self.cellcount):
                pg.draw.rect(surface, pg.Color(0, 0, 0), pg.Rect(self.cellSize[0]*j, self.cellSize[1]*i, self.cellSize[0], self.cellSize[1]))
