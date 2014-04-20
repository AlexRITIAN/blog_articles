#!/usr/bin/env python
import sys
import game
import gameio

def main(r, l, num):
	#allocate the game boards
	boardsList =  game.allocBoard(r, l);
	mineBoard = boardsList[0];
	statusBoard =  boardsList[1];
	
	#place the desired number of mines on a given mine board
	game.setMineNum(mineBoard, num);	

	print("Here is the minefield: ")
	gameio.displayBoard(mineBoard, statusBoard);
	
	#call the game-loop procedure
	re = gameio.gameLoop(mineBoard, statusBoard)
	if re==2 :
		print("You win the game. Congratuations!")

if __name__ == "__main__":
	if len(sys.argv) > 1:
		if len(sys.argv) == 2:
			r = int(sys.argv[1]);
			l,num = input("Enter a colunm and numbers of mines:\n").split();
		elif len(sys.argv) == 3:
			r = int(sys.argv[1]);
			l = int(sys.argv[2]);
			num  = input("Enter the numbers of mines:\n");
		elif len(sys.argv) >= 4:
			r = int(sys.argv[1]);
			l = int(sys.argv[2]);
			num = int(sys.argv[3]);

	else:
        	r,l,num = input("Enter a row, colunm and numbers of mines:\n").split();

	main(int(r), int(l), int(num));

