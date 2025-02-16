import argparse
import pygame
import sys

#this file is used to test, that is what arguments are directly given to the game_of_life fonction

#import classes
from .display import Display
from .cells import Board
from .cells import Cell

#global variables
ALIVE=True
DEAD=False


def game_of_life(input_path,output_path,m,d,f,width,height):
    
    board=Board(input_path,output_path)
    
    if int(d)==1: #if display on, initiates pygame and instantiate Display
        pygame.init()
        display=Display(int(width),int(height),int(f))
    
    for k in range(int(m)):
        board.step_forward() #moves the cells according to the game of life principles

        if int(d)==1: #if display on
            display.draw_update(board) # draws new step and refresh screen
            pygame.display.set_caption("Game of Life - step "+str(k))
            

    if int(d)==1: #if display on, stops pygame
        pygame.quit()
        quit()
        sys.exit()
        
    board.output_file() #writes the output file representing the final board a txt file
