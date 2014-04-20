#!/usr/bin/env python

import game
import gameio

r, l, num = input("Enter a row, column and numbers of mines:\n").split();
r = int(r);
l = int(l);
num = int(num);

boardsList =  game.allocBoard(r, l);
mineBoard = boardsList[0];
statusBoard =  boardsList[1];
game.setMineNum(mineBoard, num);

print("initial board: ")
gameio.displayBoard(mineBoard, statusBoard);
print("move on:")
re = gameio.move(mineBoard, statusBoard);
if re==2:
        print("it is the end of game!")

print("move on:")
re = gameio.move(mineBoard, statusBoard);
if re==2:
	print("it is the end of game!")

print("move on:")
re = gameio.move(mineBoard, statusBoard);
if re==2:
        print("it is the end of game!")


