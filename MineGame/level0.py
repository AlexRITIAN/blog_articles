#!/usr/bin/env python

import game
import gameio

def displayBoard(board):

        # display the board
        r = len(board);
        l = len(board[0])

        i = 0;j =0;
        while i <= r:
                j = 0;

                while j <= l:
                        if i== 0:
                                if j==0:
                                        print("   ",end="")
                                else:
                                        print(" %d " %(j-1),end="")
                        elif j==0:
                                print(" %d " %(i-1),end="")
                        else:
                                print("[%d]" %(board[i-1][j-1]),end="")
                        j = j + 1;

                print('\n');
                i = i + 1;


#test the 1st function
row,col,num = input("Enter a row, colunm and numbers of mines:\n").split();
row = int(row)
col = int(col)
num = int(num)
boardsList =  game.allocBoard(int(row), int(col));
mineBoard = boardsList[0]
statusBoard = boardsList[1];


#test the 5th funciton
print("initialize the given status board:")
game.initStatusBoard(statusBoard);
displayBoard(statusBoard)

print("initial mine board: ")
displayBoard(mineBoard)

#test the 2nd function
game.setMineNum(mineBoard, num);
print("place the desired number of mines:")
displayBoard(mineBoard)

#test the 3rd function
print("calculates the number of mines adjacent to that location:")
row, col = input("Enter a row and colunm  of board:\n").split();
row = int(row);
col = int(col);
print("the number of mines adacent to (%d, %d) location: %d." %(row, col, game.getLocNum(mineBoard, row, col)))
print("\n")

#test the 4th function
game.setMineBoardNum(mineBoard);
print("place the number of adjacent mines in each square in a given mine board:")
displayBoard(mineBoard)

