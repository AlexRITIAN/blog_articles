#!/usr/bin/env python

import random


'''Level 0
A board can be represented as a two-dimensional array or matrix. A location on the board can be represented as a row and a column. Define a set of functions and procedures for allocating and populating a board, given the specifications from the command line.
'''

'''
Thr 1st function: allocate an empty board. 
Two boards will be allocated with this function, 
one which will hold mine information (the mine board) and 
one which holds the covered/uncovered status of each square (the status board).
'''
def allocBoard(r, l):
	mineBoard=[];
	statusBoard=[];
	i = 0;j =0;
	while i < r:
		mm = [];
		sm = [];
		while j < l:
			mm.append(0) # the initial value is zero
			sm.append(0)
			j = j+1;
		mineBoard.append(mm);
		statusBoard.append(sm);
		j = 0	
		i = i+1;
	boardsList = [mineBoard, statusBoard]
	return boardsList;


'''
The 2nd function: place the desired number of mines on a given mine board.
'''
def setMineNum(mineBoard, num):
	count =1;
	r = len(mineBoard);
	l = len(mineBoard[0])
	
	#define the numbers of mines is not more then half the value of r*l;	
	while num > l*r/2 :
		print ("num is too large!!!")
		num = int(input("Enter the number of mines:\n"));

	while count <= num: # the location of a mine is in random
		row = random.randint(0,r-1);
		col = random.randint(0,l-1);
		if(mineBoard[row][col] != -1):
			mineBoard[row][col]=-1;
			count = count+1;


'''
The 3rd function: calculates the number of mines adjacent to that location  when given a mine board and a location. 
It does this by checking each of its eight (or fewer) neighbors for mines.
'''
def getLocNum(matrix, row, col):
	count = 0;
	r = len(matrix);
	l = len(matrix[0]);

	# invalid input
	if row > r-1 or col > l-1:
		return;
	
	# the location has a mine and returs itself
	if matrix[row][col]==-1:
		return -1;

	# for row-1
	if row-1 >= 0:
		if (col-l >= 0 and matrix[row-1][col-1]==-1):
			count = count + 1;
	 
		if (matrix[row-1][col]==-1):
			count = count + 1;
		if (col+1 <= l-1 and matrix[row-1][col+1]==-1):
			count = count + 1;

	# for row
	if (col-1 >=0 and matrix[row][col-1]==-1):
		count = count + 1;

	if (col+1 <=l-1 and matrix[row][col+1]==-1):
		count = count + 1;

	#foe row +1
	if row+1 <= r-1:
		if (col-1 >= 0 and matrix[row+1][col-1]==-1):
			count = count + 1;  

		if (matrix[row+1][col]==-1):
			count = count + 1;

		if (col+1 <= l-1 and matrix[row+1][col+1]==-1):
			count = count + 1;
	return count;

'''
The 4th function: place the number of adjacent mines in each square in a given mine board (via the third function).
set the square's value of the mine board: mineBoard[row][col] = count
'''
def setLocNum(mineBoard, row, col):
	r = len(mineBoard);
	l = len(mineBoard[0]);
	if row > r-1 or col > l-1:
		print ("invalid input!!!")
		return;

	count = getLocNum(mineBoard, row, col);
	mineBoard[row][col] = count;

def setMineBoardNum(mineBoard):
	r = len(mineBoard);
	l = len(mineBoard[0]);
 
	i = 0;j =0;
	while i < r:
		j = 0;
		while j < l:
			#call setLocNum func.
			setLocNum(mineBoard, i, j);
			j = j+1;

		i = i+1;


'''
The 5th function: initialize the given status board so that every square is considered covered.
'''
def initStatusBoard(statusBoard):
	r = len(statusBoard);
	l = len(statusBoard[0]);
	i = 0;j =0;
	while i < r:
		j = 0;
		while j < l:
			statusBoard[i][j]=0;
			j = j+1;
                
		i = i+1;


'''
initialize the given mine board
'''
def initMineBoard(mineBoard):
	r = len(mineBoard);
	l = len(mineBoard[0]);
	i = 0;j =0;
	while i < r:
		j = 0;
		while j < l:
			mineBoard[i][j]=0;
			j = j+1;

		i = i+1;


'''Level 3
The uncovering function: uncovers the square on the given board when given a mine board, a status board, and a location. If the square has no adjacent mines, the function recursively calls itself to uncover all the neighbors of the square. If the function uncovers a square with a mine, it should return 1. Otherwise, it should return 0.
'''
def uncoverLoc(mineBoard, statusBoard, row, col):
	r = len(mineBoard);
	l = len(mineBoard[0]);
	if row > r-1 or col > l-1:
		print ("invalid input!!!")
		return 0;
	if statusBoard[row][col]==1:
		return 0;
	statusBoard[row][col] = 1;

	if mineBoard[row][col]==-1:
		return 1;
	else:
		if getLocNum(mineBoard, row, col)==0:
		        # for row-1
			if row-1 >= 0:
				if (col-l >= 0):
					uncoverLoc(mineBoard, statusBoard, row-1, col-1);
				
				uncoverLoc(mineBoard, statusBoard, row-1, col);

				if (col+1 <= l-1):
					uncoverLoc(mineBoard, statusBoard, row-1, col+1);
        		# for row
			if (col-1 >=0):
				uncoverLoc(mineBoard, statusBoard, row, col-1)

			if (col+1 <=l-1):
				uncoverLoc(mineBoard, statusBoard, row, col+1)

        		#foe row +1
			if row+1 <= r-1:
				if (col-1 >= 0):
                        		uncoverLoc(mineBoard, statusBoard, row+1, col-1)

                	
				uncoverLoc(mineBoard, statusBoard, row+1, col)

				if (col+1 <= l-1):
					uncoverLoc(mineBoard, statusBoard, row+1, col+1)
			

		return 0;


'''
"end of game" checking function that, when given a mine board and a status board, returns 0 if all covered squares contain mines and 1 otherwise.
'''
def checkEnd(mineBoard, statusBoard):
        r = len(mineBoard);
        l = len(mineBoard[0]);

        i = 0;j =0;
        while i < r:
                j = 0;
                while j < l:
                        if statusBoard[i][j]==0:
                                if mineBoard[i][j] != -1:
                                        return 1;
                        #game.setMatrixNum(mineBoard);
                        j = j+1;
                i = i+1;
        return 0;



