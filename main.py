from Utility.grid import *
from Utility.vector import *
from Utility.const import *
import pygame as pg
import numpy as np
import sys

pg.init()
window = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption(WINDOW_TITLE)

def main():

    myGrid = Grid(WINDOW_WIDTH, WINDOW_HEIGHT, 8)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        # Grid line color:
        window.fill((107, 171, 255))

        # Draw the grid cells.
        myGrid.draw(window)


        # Update the screen:
        
        pg.display.flip()


if __name__ == '__main__':
    main()