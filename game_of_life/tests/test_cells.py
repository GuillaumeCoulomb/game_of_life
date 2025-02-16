import pytest

from .cells import Board
from .cells import Cell

def test_nb_raws():
    board=Board("gosper_glider_gun.txt","my_output_file.txt")
    assert board._n_columns==36
    assert board._n_raws==10

def number_of_neighboors():
    board=Board("glider.txt","my_output_file.txt")
    assert board.cells[0,0].number_of_neighboors(board)==1
    assert board.cells[1,1].number_of_neighboors(board)==5
    assert board.cells[2,1].number_of_neighboors(board)==3

