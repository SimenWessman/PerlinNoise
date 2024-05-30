import numpy as np
import pygame as pg

def pixel(surface, color, pos):
    surface.fill(color, (pos, (1, 1)))

class Grid:
    def __init__(self, width, height, cellcount):
        self.width = width
        self.height = height
        self.cellcount = cellcount

        self.cellSize = (width / cellcount, height / cellcount)

    def draw(self, surface, color, pos):
        
