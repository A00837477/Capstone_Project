# My name is Javier Cruz Villarreal, a 1st semester University student at ITESM
# This is my final programming project for my class, where i will be making a special game based on a 6x6 board
import numpy as np

#Asks player for info

#Function that makes the matrix
board = np.matrix([["---" , " 0 " , " 1 " , " 2 " , " 3 " , " 4 " , " 5 "],
     [" 0 " , " * " , " _ " , " X " , " X " , " _ " , " * "],
     [" 1 " , " _ " , " _ " , " _ " , " _ " , " _ " , " _ "],
     [" 2 " , " _ " , " _ " , " @ " , " @ " , " _ " , " _ "],
     [" 3 " , " _ " , " _ " , " _ " , " _ " , " _ " , " _ "],
     [" 4 " , " _ " , " _ " , " _ " , " _ " , " _ " , " _ "],
     [" 5 " , " * " , " _ " , " O " , " O " , " _ " , " * "]])

def askmove(board):
     player = input("Which Player? X or O?")
     row = int(input("Row Number?"))
     col = int(input("Column Number?"))
     move = input("Where do you want to move? left (key a), down (key s), up (key w), right (key d)")
     return player, row, col, move

"""def check(player, row, col, move):
     checker = input(f" {newboard(player, row, col, move)} \n Do you want to move like this? (y) for yes or (n) for no ")
     if checker == "y":
          return
     elif checker == "n":
          askmove(board)
          check(player, row, col, move)"""

#el board siendo edited despues de el los moves          
#def newboard(player, row, col, move):

#Player Moving function
#if playermovement

#main function
def main():
     #askmove(board)
     print(board)

#to run
main()