#!/usr/bin/env python

import os
import game
import time


'''Level 1
Define a procedure that displays a board. This function is given two boards, a mine board and a status board. As the board is being drawn, the function checks the status board to see if a covering mark should be displayed or if the number of adjacent mines (found on the mine board) should be displayed.
'''
def displayBoard(mineBoard, statusBoard):
	
	# display the mine board
	r = len(mineBoard);
	l = len(mineBoard[0])
	
	#place the number of adjacent mines in each square in a given mine board
	game.setMineBoardNum(mineBoard);
	
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
				if statusBoard[i-1][j-1]==0:
					print("[-]",end="")
				elif mineBoard[i-1][j-1]!=-1:
					print("[%d]" %(mineBoard[i-1][j-1]),end="")
				else: 
					print("BOM",end="")	
			j = j + 1;

		print('\n');
		i = i + 1;

'''Level 2
Define an pyrotechnic display procedure. At the start, this procedure should just print the word BOOM.
'''
def displayBoomEachCol(mineBoard,statusBoard, col, boomFlag,bombFlag):
	r = len(mineBoard);
	l = len(mineBoard[0])

        #place the number of adjacent mines in each square in a given mine board
	game.setMineBoardNum(mineBoard);

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
				if statusBoard[i-1][j-1]==0:
					if mineBoard[i-1][j-1]==-1:
						if j-1 == col:
							print("%s" %(boomFlag),end="")
						else:
							print("%s" %(bombFlag),end="")
					else:
						print("[-]",end="")
				elif mineBoard[i-1][j-1]!=-1:
					print("[%d]" %(mineBoard[i-1][j-1]),end="")
				else:
					print("BOM",end="")
				
			j = j + 1;

		print('\n');
		i = i + 1;



def displayBoom(mineBoard,statusBoard, row, col):
	
	l = len(mineBoard[0])

	boomList = ["   ","BOM","   ","BOM","   ","BOM"]
	time.sleep(1);
	os.system('clear');
	bombFlag ="bob"
	i = 0; c1 = col; c2 =col;
	while i< 10:
		if c1 >= 0:
			for boomFlag in boomList:
				os.system('clear');
				displayBoomEachCol(mineBoard,statusBoard, c1, boomFlag,bombFlag);
				time.sleep(0.1);
			c1 = c1 - 1;
	
		if c2 <= l-1:
			for boomFlag in boomList:
				os.system('clear');
				displayBoomEachCol(mineBoard,statusBoard, c2, boomFlag,bombFlag);
				time.sleep(0.1);
			c2 = c2 + 1;

		i = i+1;
	print("game over!")

'''Level 5
Define a "move" function that, when given a mine board and a status board, immediately calls the end-of-game checking function. 
If it returns 0, then the this function should return 2. 
Otherwise, this function prompts for a location and then uncovers that square using the function from Level 3. If the uncovering function returns a 0, this function should display the board using the procedure from Level 1 and return a 0. If the uncovering function returns a 1, then the pyrotechnic display procedure from Level 2 should be called and a value of 1 returned.
'''
def move(mineBoard, statusBoard):
	if game.checkEnd(mineBoard, statusBoard) == 0:# is the end!
		return 2;
	else:
		row, col = input("Which square do you wish to uncover?\nEnter the row and colunm:").split();
		row = int(row);
		col = int(col);
		#print("row:%d,col=%d" %(row,col))
		re = game.uncoverLoc(mineBoard, statusBoard, row, col);
		if re ==0:
			displayBoard(mineBoard, statusBoard);
			return 0;
		elif re == 1:#is the mine	
			displayBoom(mineBoard,statusBoard, row, col);
			return 1;
			

'''Level 6
Define a "game loop" procedure that implements a classic "reading" loop for running the game. The initial mine and status boards should be passed to this procedure. Before the loop starts, the move function from Level 5 should be called and the return value saved. As long as this saved return value is 0, the loop should run. The body of the loop reruns the move function, resaving the return value. When the loop exits, either call the pyrotechnic display procedure or a congratulatory message.
'''	
def gameLoop(mineBoard, statusBoard):
	re = move(mineBoard, statusBoard)
	while (re==0):
		re = move(mineBoard, statusBoard);
	return re;
