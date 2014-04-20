#!/usr/bin/env python

import game
import gameio
import random

r,l,num = input("Enter a row, colunm and numbers of mines:\n").split();
r = int(r)
l = int(l)
num = int(num)
boardsList =  game.allocBoard(r, l);
mineBoard = boardsList[0];
statusBoard =  boardsList[1];
print("initial board: ")
gameio.displayBoard(mineBoard, statusBoard);

game.setMineNum(mineBoard, num);

#uncover half squares of the board in random.
print("start to uncover the square in random: ")
count = 0;
over = 0;
while count <= r*l/2:
	row = random.randint(0,r-1);
	col = random.randint(0,l-1);
	if(statusBoard[row][col]==0):
		statusBoard[row][col]=1;
		#game.setMatrixNum(mineBoard);
		count = count + 1;
	print("after uncover an square (%d, %d):" %(row, col));
	gameio.displayBoard(mineBoard, statusBoard);
	if mineBoard[row][col]==-1:
		print("You have uncoverd a mine, game over!")
		over = 1;
		break;

#uncover the left squares of the board.
if over==0:
	i = 0;j =0;
	while i < r:
		j = 0;
		while j < l:
			if statusBoard[i][j]==0 and mineBoard[i][j]!=-1:
        			statusBoard[i][j] = 1;
			#game.setMatrixNum(mineBoard);
			j = j+1;
		i = i+1;
	print("after uncover all squares:")
	gameio.displayBoard(mineBoard, statusBoard);

