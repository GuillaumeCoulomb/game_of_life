import pytest

from .main import game_of_life

def fichiers_sont_egaux(fichier1_path, fichier2_path):
    try:
        with open(fichier1_path, 'r', encoding='utf-8') as fichier1, \
             open(fichier2_path, 'r', encoding='utf-8') as fichier2:

            # Lire toutes les lignes des deux fichiers
            lignes_fichier1 = fichier1.readlines()
            lignes_fichier2 = fichier2.readlines()

            # Comparer les lignes
            if lignes_fichier1 == lignes_fichier2:
                print("Les fichiers sont égaux.")
                return True
            else:
                print("Les fichiers ne sont pas égaux.")
                return False

    except FileNotFoundError as e:
        print(f"Erreur : {e}")
        return False



def test_output():
    game_of_life("blinker.txt","my_output_file.txt",1,0,10,800,600)
    assert fichiers_sont_egaux("my_output_file.txt","blinker_vertical.txt")==True


