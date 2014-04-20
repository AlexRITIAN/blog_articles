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

#uncover half squares of the board.
count = 0;over =0;
while count <= r*l/2:
	row = random.randint(0,r-1);
	col = random.randint(0,l-1);
	if(statusBoard[row][col]==0):
		statusBoard[row][col]=1;
		count = count + 1;
	print("after uncover an square (%d, %d):" %(row, col))
	gameio.displayBoard(mineBoard, statusBoard);
	if mineBoard[row][col]==-1:
		over =1;
		print("You have uncoverd a mine, game over!")
		gameio.displayBoom(mineBoard,statusBoard, row, col);
		break;

if over ==0:
	count = 0;
	while count <= r*l:
		row,col = input("Enter a row and colunm you want to uncover:\n").split();
		row = int(row)
		col = int(col)
		if(row <0 | col<0):
			break;
		if(row >= r or col >= l):
			print("invalid input ,please input again: ")
			continue;
		if(statusBoard[row][col]==0):
			if mineBoard[row][col]==-1:
				print("You have uncoverd a mine, game over!")
				gameio.displayBoom(mineBoard,statusBoard, row, col);
				break;
			else:	
				statusBoard[row][col]=1;
				gameio.displayBoard(mineBoard, statusBoard);
				count = count + 1;

