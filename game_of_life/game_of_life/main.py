import argparse

#poetry run game_of_life -i="my_input_file.txt" -o="my_output_file.text" -m=5 -f=0 --width=800 --height=600
#il faut l'executer dans le dossier game_of_life contenant main.py


#command line arguments 

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
        self.cells=[]
        # Ouvrir le fichier en mode lecture ('r')
        with open(initial_pattern, 'r') as fichier:
            lignes = fichier.readlines()
            for i in range(len(lignes)):
                for j in range(len(lignes[i].strip())):
                    if lignes[i].strip()[j]=='0':
                        self.cells.append(Cell(i,j,DEAD))
                    if lignes[i].strip()[j]=='1':
                        self.cells.append(Cell(i,j,ALIVE))
        
    
    def step_forward(self):

        #appliquer les règles du jeu

        for elt in self.cells:
            if elt.current_state==ALIVE:
                if elt.number_of_neighboors(self)==0 or elt.number_of_neighboors(self)==1 :
                    self.next_state=DEAD
                if elt.number_of_neighboors(self)==2 or elt.number_of_neighboors(self)==3 :
                    self.next_state=ALIVE
                if elt.number_of_neighboors(self)>3:
                    self.next_state=DEAD

            if elt.current_state==DEAD:
                if elt.number_of_neighboors(self)==3:
                    self.next_state=ALIVE

        for elt in self.cells:
            elt.current_state=elt.next_state

        

        

    def output_file(self):

        

        n_raws=max([c.x_pos for c in self.cells])+1
        n_columns=max([c.y_pos for c in self.cells])+1

        
        # Ouverture du fichier en mode écriture ('w')
        with open(args.o, 'w') as fichier:
            for i in range(n_raws):
                for j in range(n_columns):
                    for elt in self.cells:
                        if elt.x_pos==i and elt.y_pos==j:
                            if elt.current_state==ALIVE: 
                                fichier.write("1")
                            if elt.current_state==DEAD :      
                                fichier.write("0")

                    
        
                
                fichier.write("\n")

class Cell(Board):
    def __init__(self,x_pos,y_pos,state):
        self.x_pos=x_pos
        self.y_pos=y_pos
        self.current_state=state #living or dead
        self.next_state=None #None because initialisation

    def number_of_neighboors(self,board):
        n=0
        circle=[(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
        for elt in circle:
            if any(c.x_pos==self.x_pos + elt[0] and c.y_pos==self.y_pos + elt[1] and c.current_state==ALIVE for c in board.cells):
                n=n+1
        return n
    
def game_of_life():
    board=Board(args.i)
    for k in range(int(args.m)):
        board.step_forward()
    board.output_file()
        







