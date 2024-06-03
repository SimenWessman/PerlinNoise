import numpy as np
import pygame as pg
import random as rand

def pixel(surface, color, pos):
    surface.fill(color, (pos, (1, 1)))

class Cell:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width * 0.95 # Doing this for grid effect
        self.height = height * 0.95 # Doing this for grid effect
        self.color = color

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width * 0.95
        self.height = height * 0.95
        scale = rand.random() * 255
        self.color = (scale, scale, scale)

    def draw(self, surface):
        pg.draw.rect(surface, pg.Color(self.color), pg.Rect(self.x, self.y, self.width, self.height))

    

class Grid:
    def __init__(self, width, height, cellcount):
        self.width = width
        self.height = height
        self.cellcount = cellcount

        self.cells = []

        self.cellSize = (width / cellcount, height / cellcount)

        for i in range(0, self.cellcount):
            for j in range(0, self.cellcount):
                self.cells.append(Cell(j * self.cellSize[0], i * self.cellSize[1], self.cellSize[0], self.cellSize[1]))

    # Use this function to draw the grid lines.
    def draw(self, surface):
        for cell in self.cells:
            cell.draw(surface)
