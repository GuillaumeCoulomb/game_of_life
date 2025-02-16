#pour ce code dédié aux tests, les command line arguments seront passès en arguments de la fonction game_of_life

import argparse
import pygame
import sys

from .display import Display
from .cells import Board
from .cells import Cell

#python -m pip install pygame
#poetry add pygame
#poetry run game_of_life -i="my_input_file.txt" -o="my_output_file.txt" -m=5 -f=0 --width=800 --height=600
#il faut l'executer dans le dossier game_of_life contenant main.py


#command line arguments :

#-d=1 si display wanted

# parser = argparse.ArgumentParser(description='Some description.')
# parser.add_argument('-i', help="to set the path to the initial pattern file")
# parser.add_argument('-o', help="to set the path to the output file, that will contain the final state of our simulation, in the same format as the input file")
# parser.add_argument('-m', help="to set the number of steps to run, when display is off")
# parser.add_argument('-d', default=0,help="display flag. By default no display is done with pygame (i.e.: we don’t even initialize pygame). When enabled, pygame is enabled and we display each step of the simulation")
# parser.add_argument('-f', help="The number of frames per second to use with pygame")
# parser.add_argument('--width', help="the initial width of the pygame screen")
# parser.add_argument('--height', help="the initial heigth of the pygame screen")

#args = parser.parse_args() # to call an arg : args.i or args.o ...

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


    