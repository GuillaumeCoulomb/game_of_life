import argparse
import pygame
import sys
import logging

logger=logging.getLogger("foo")

class Display:

    def __init__(self,width,height,fps):
        
        try:
            pygame.init()
        except:
            logger.error("the program failed to initiate pygame")

        self._width=width
        self._height=height
        self._cell_size=10
        self._fps=fps
        self._clock= pygame.time.Clock()
        screen_size = (int(self._width),int(self._height))

        self._screen = pygame.display.set_mode(screen_size)
        self._screen.fill((128,128,128))

    def draw_update(self,board):
        
        for cell in board._cells.values():
            cell.draw(self._screen) 

        try:
            pygame.display.update()
        except:
            logger.warning("the program failed to update the display")

        self._clock.tick(self._fps)

        try:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
        except:
            logger.error("the program failed to quit")          