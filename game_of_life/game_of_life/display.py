#import modules
import argparse
import pygame
import sys
import logging

#define custom named logger
logger=logging.getLogger("foo")

class Display:

    def __init__(self,width,height,fps):
        
        try:
            pygame.init()
        except:
            logger.error("the program failed to initiate pygame")

        self._width=width
        self._height=height
        self._fps=fps
        self._clock= pygame.time.Clock() #starts the pygame clock
        screen_size = (int(self._width),int(self._height)) #creates the screen

        self._screen = pygame.display.set_mode(screen_size)
        self._screen.fill((128,128,128)) #the boundaries of the grid are drawn in grey

    def draw_update(self,board):
        
        for cell in board._cells.values(): #travels the cells to draw them
            cell.draw(self._screen)

        try:
            pygame.display.update() #update the drawing
        except:
            logger.warning("the program failed to update the display")

        self._clock.tick(self._fps) #limits the fps

        try:
            for event in pygame.event.get(): #quits pygame when if user presses q key
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
        except:
            logger.error("the program failed to quit")  
        