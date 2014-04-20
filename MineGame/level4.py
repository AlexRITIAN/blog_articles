#!/usr/bin/env python

import game
import gameio


r = 4 ;
l = 4 ;
boardsList =  game.allocBoard(r, l);
mineBoard = boardsList[0];
statusBoard =  boardsList[1];
mineBoard[0][0] = -1;
mineBoard[0][3] = -1;
print("initial board: ")
gameio.displayBoard(mineBoard, statusBoard);

game.uncoverLoc(mineBoard, statusBoard, 2, 2);
print("uncoverint Loction(2,2):")
gameio.displayBoard(mineBoard, statusBoard);

if game.checkEnd(mineBoard, statusBoard)==0:
	print("it is the end of game!")
else:
	print("it is not the end of game.")
