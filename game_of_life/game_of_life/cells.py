 #import modules
import pygame
import logging

#global variables
ALIVE=True
DEAD=False

#define custom named logger
logger=logging.getLogger("foo")

class Board:
    """Main class"""
    def __init__(self,initial_pattern_path,output_path)-> None:
        """Object initialisation"""
        self._initial_pattern_path=initial_pattern_path
        self._output_path=output_path
        self._cells={} #the cells will be instantied in this dict

        try:
            with open(self._initial_pattern_path, 'r') as fichier: # opening file in reading mode
                lignes = fichier.readlines()
                for i in range(len(lignes)):
                    for j in range(len(lignes[i].strip())):
                        if lignes[i].strip()[j]=='0':
                            self._cells[(i,j)]=Cell(i,j,DEAD) #the cells are instantied in self._cells, their keys are their positions
                        if lignes[i].strip()[j]=='1':
                            self._cells[(i,j)]=Cell(i,j,ALIVE)
        except:
            logger.critical("the program failed to read the input file")
        
        #grid size
        self._n_raws=max([c._x_pos for c in self._cells.values()])+1
        self._n_columns=max([c._y_pos for c in self._cells.values()])+1

        logger.info("input_read")
                
    def step_forward(self) ->None:
        """moves the board to the next step"""
        for elt in self._cells.values(): 

            #implement the game of life principle :
            n_b=elt.number_of_neighboors(self)
            if elt._current_state==ALIVE:              
                if n_b==0 or n_b==1 :
                    elt._next_state=DEAD
                if n_b==2 or n_b==3 :
                    elt._next_state=ALIVE
                if n_b>3:
                    elt._next_state=DEAD

            if elt._current_state==DEAD:
                if n_b==3:
                    elt._next_state=ALIVE
            
        for elt in self._cells.values(): #makes the calculated next step current
            elt._current_state=elt._next_state

        logger.info("step forward")

    def output_file(self)->None:
        """writes the outputfile according to the final situation"""
        try:
            # opening file in writing mode
            with open(self._output_path, 'w') as fichier:
                for i in range(self._n_raws):
                    for j in range(self._n_columns):
                        if self._cells[(i,j)]._current_state==ALIVE: 
                            fichier.write("1")
                        if self._cells[(i,j)]._current_state==DEAD:     
                            fichier.write("0")

                    fichier.write("\n") #line break at the end of each line
        except:
            logger.critical("the program failed to write the output file")


class Cell(Board):
    """Class that represent the cell"""
    def __init__(self,x_pos,y_pos,state)->None:
        """Object initialisation"""
        self._x_pos=x_pos
        self._y_pos=y_pos
        self._current_state=state #ALIVE or DEAD
        self._next_state=state #used to calculate a new step
        self._cell_size=10

    def number_of_neighboors(self,board)->int:
        """returns the number of neighboors of a cell"""
        n=0
        circle=[(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
        for elt in circle: #travels the 8 positions surrounding a cell
            tested_position=self._x_pos + elt[0],self._y_pos + elt[1]
            if (tested_position) in board._cells.keys() and board._cells[tested_position]._current_state==ALIVE :
                n=n+1 
        return n

    def draw(self, screen)->None:
        """draws one cell"""
        if self._current_state==ALIVE:
            color=(0,0,0) #living cells drawn in black
        if self._current_state==DEAD:
            color=(255,255,255) #dead cells drawn in white
        rect = pygame.Rect(self._y_pos * self._cell_size, self._x_pos * self._cell_size,self._cell_size,self._cell_size)
        pygame.draw.rect(screen, color, rect)
