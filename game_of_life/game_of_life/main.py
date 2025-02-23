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

#command line arguments :

parser = argparse.ArgumentParser(description='Conway’s Game of Life is a cellular automaton game in which a user provide an initial state that will evolve automatically.')
parser.add_argument('-i', help="to set the path to the initial pattern file")
parser.add_argument('-o', help="to set the path to the output file, that will contain the final state of our simulation, in the same format as the input file")
parser.add_argument('-m', help="to set the number of steps to run, when display is off")
parser.add_argument('-d', action="count", default=0,help="display flag. By default no display is done with pygame (i.e.: we don’t even initialize pygame). When enabled, pygame is enabled and we display each step of the simulation.")
parser.add_argument('-f', help="The number of frames per second to use with pygame")
parser.add_argument('--width', default=800, help="the initial width of the pygame screen")
parser.add_argument('--height', default=600, help="the initial heigth of the pygame screen")
parser.add_argument("--verbose", "-v", dest="verbose", action="count", default=0, help="Verbose level. -v for information, -vv for debug, -vvv for trace.")

args = parser.parse_args()

#define custom named logger
logger=logging.getLogger("foo")
handler = logging.StreamHandler(sys.stderr)
logger.addHandler(handler) #registration of the new handler

#using the verbose integer to set the logging level
if args.verbose == 1:
    logger.setLevel(logging.INFO)
elif args.verbose == 2:
    logger.setLevel(logging.DEBUG)


#this fonction launches the game, registered in the .tomml file
def game_of_life():
    """Main function that starts the game"""
    board=Board(args.i,args.o)
    
    if args.d==1: #if display on, initiates pygame and instantiate Display
        pygame.init()
        logger.info("pygame initialised")
        display=Display(int(args.width),int(args.height),int(args.f))
    
    for k in range(int(args.m)):
        board.step_forward() #moves the cells according to the game of life principles

        if args.d==1: #if display on
            display.draw_update(board) # draws new step and refresh screen
            pygame.display.set_caption("Game of Life - step "+str(k))
            
    board.output_file() #writes the output file representing the final board a txt file
    logger.info("output file written")

    if args.d==1: #if display on, stops pygame
        pygame.quit()
        quit()
        logger.info("pygame quit")
        sys.exit()
    