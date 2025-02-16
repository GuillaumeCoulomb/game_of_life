import argparse
import pygame
import sys

class Display:

    def __init__(self,width,height,fps):
        pygame.init()

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

        pygame.display.update()
        self._clock.tick(self._fps)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                