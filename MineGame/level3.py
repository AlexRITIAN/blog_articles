#!/usr/bin/env python

import game
import gameio

r = 4 ;
l = 4;
boardsList =  game.allocBoard(r, l);
mineBoard = boardsList[0];
statusBoard =  boardsList[1];
mineBoard[0][0] = -1;
mineBoard[0][3] = -1;
print("initial board: ")
gameio.displayBoard(mineBoard, statusBoard);

game.uncoverLoc(mineBoard, statusBoard, 2, 2);
print("uncovering Loction(2,2):")
gameio.displayBoard(mineBoard, statusBoard);


