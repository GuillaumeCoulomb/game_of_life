import argparse

#poetry run game_of_life -i="my_input_file.txt" -o="my_output_file.text" -m=5 -f=0 --width=800 --height=600
#il faut l'executer dans le dossier game_of_life contenant main.py


#command line arguments :

parser = argparse.ArgumentParser(description='Some description.')
parser.add_argument('-i', help="to set the path to the initial pattern file")
parser.add_argument('-o', help="to set the path to the output file, that will contain the final state of our simulation, in the same format as the input file")
parser.add_argument('-m', help="to set the number of steps to run, when display is off")
parser.add_argument('-d', help="display flag. By default no display is done with pygame (i.e.: we don’t even initialize pygame). When enabled, pygame is enabled and we display each step of the simulation")
parser.add_argument('-f', help="The number of frames per second to use with pygame")
parser.add_argument('--width', help="the initial width of the pygame screen")
parser.add_argument('--height', help="the initial heigth of the pygame screen")

args = parser.parse_args() # to call an arg : args.i or args.o ...

ALIVE=True
DEAD=False

class Board:
    def __init__(self,initial_pattern):
        self.cells={} #the cells will be instantied in this dict
        with open(initial_pattern, 'r') as fichier: # opening file in reading mode
            lignes = fichier.readlines()
            for i in range(len(lignes)):
                for j in range(len(lignes[i].strip())):
                    if lignes[i].strip()[j]=='0':
                        self.cells[(i,j)]=Cell(i,j,DEAD) #the cells are instantied in self.cells, their keys are their positions
                    if lignes[i].strip()[j]=='1':
                        self.cells[(i,j)]=Cell(i,j,ALIVE)
        

    def step_forward(self): #moves the board to the next step

        for elt in self.cells.values(): #implement the game of life principle
            n_b=elt.number_of_neighboors(self)
            if elt.current_state==ALIVE:
                if n_b==0 or n_b==1 :
                    elt.next_state=DEAD
                if n_b==2 or n_b==3 :
                    elt.next_state=ALIVE
                if n_b>3:
                    elt.next_state=DEAD
            
            if elt.current_state==DEAD:
                if n_b==3:
                    elt.next_state=ALIVE
            
        for elt in self.cells.values():
            elt.current_state=elt.next_state


    def output_file(self):

        #calulate the size of the output file
        n_raws=max([c.x_pos for c in self.cells.values()])+1
        n_columns=max([c.y_pos for c in self.cells.values()])+1

        # opening file in writing mode
        with open(args.o, 'w') as fichier:
            for i in range(n_raws):
                for j in range(n_columns):
                    if self.cells[(i,j)].current_state==ALIVE: 
                        fichier.write("1")
                    if self.cells[(i,j)].current_state==DEAD:     
                        fichier.write("0")

                fichier.write("\n") #line break at the end of each line

class Cell(Board):
    def __init__(self,x_pos,y_pos,state):
        self.x_pos=x_pos
        self.y_pos=y_pos
        self.current_state=state #ALIVE or DEAD
        self.next_state=state #used to calculate a new step

    def number_of_neighboors(self,board):
        n=0
        circle=[(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
        for elt in circle: #travels the 8 positions surrounding a cell
            tested_position=self.x_pos + elt[0],self.y_pos + elt[1]
            if (tested_position) in board.cells.keys() and board.cells[tested_position].current_state==ALIVE :
                n=n+1 
        return n
    
def game_of_life():
    board=Board(args.i)
    for k in range(int(args.m)):
        board.step_forward()
    board.output_file()
        







