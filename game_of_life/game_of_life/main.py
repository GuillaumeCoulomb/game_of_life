#import modules
import argparse
import pygame
import sys
import logging

#import classes
from .display import Display
from .cells import Board
from .cells import Cell

#global variables
ALIVE=True
DEAD=False

#define custom named logger
logger=logging.getLogger("foo")

#command line arguments :

parser = argparse.ArgumentParser(description='Some description.')
parser.add_argument('-i', help="to set the path to the initial pattern file")
parser.add_argument('-o', help="to set the path to the output file, that will contain the final state of our simulation, in the same format as the input file")
parser.add_argument('-m', help="to set the number of steps to run, when display is off")
parser.add_argument('-d', default=0,help="display flag. -d=1 if display wanted. By default no display is done with pygame (i.e.: we don’t even initialize pygame). When enabled, pygame is enabled and we display each step of the simulation")
parser.add_argument('-f', help="The number of frames per second to use with pygame")
parser.add_argument('--width', default=800, help="the initial width of the pygame screen")
parser.add_argument('--height', default=600, help="the initial heigth of the pygame screen")

args = parser.parse_args()
        
#this fonction launches the game, registered in the .tomml file
def game_of_life():
    
    board=Board(args.i,args.o)
    
    if int(args.d)==1: #if display on, initiates pygame and instantiate Display
        pygame.init()
        logger.info("pygame initialised")
        display=Display(int(args.width),int(args.height),int(args.f))
    
    for k in range(int(args.m)):
        board.step_forward() #moves the cells according to the game of life principles

        if int(args.d)==1: #if display on
            display.draw_update(board) # draws new step and refresh screen
            pygame.display.set_caption("Game of Life - step "+str(k))
            
    board.output_file() #writes the output file representing the final board a txt file
    logger.info("output file written")

    if int(args.d)==1: #if display on, stops pygame
        pygame.quit()
        quit()
        logger.info("pygame quit")
        sys.exit()
    