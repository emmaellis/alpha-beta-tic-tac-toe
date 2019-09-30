from graphics import *
import copy
""" A move is a tuple which correspond to both coordinates on the board and the 
elements of the two dimensional list called spots."""

#NOTE: Need to check for tie

def ticTacToe():
	#intializing the board to empty
	#initializing the two players to our default settings
	spots = [[None, None, None],[None, None, None],[None, None, None]]
	player1 = ("user", 1)
	player2 = ("computer", 0)
	currPlayer = player1
	
	#Opening up the graphics window so we can see the game!
	win = GraphWin("Tic Tac Toe", 500, 500)
	win.setBackground(color_rgb(229, 194, 192))
	
	ptUsr = Point(167, 250)
	ptComp = Point(333, 250)
	ptPrompt = Point(250, 150)
	txt0 = Text(ptUsr, "User")
	txt1 = Text(ptComp, "Computer")
	txt2 = Text(ptPrompt, "Who would you like to play against?")
	rect0 = Rectangle(Point(150, 240), Point(186,260))
	rect1 = Rectangle(Point(300, 240), Point(365, 260))
	rect0.setFill('white')
	rect1.setFill('white')
	rect0.draw(win)
	rect1.draw(win)
	txt0.draw(win)
	txt1.draw(win)
	txt2.draw(win)
	choice = win.getMouse()
	# if user selects "user" they're playing against another human player
	if choice.x < 250:
		player2 = ("user", 0)
	txt0.undraw()
	txt1.undraw()
	txt2.undraw()
	rect0.undraw()
	rect1.undraw()

	#Drawing the board
	pt1 = Point(5, 167)
	pt2 = Point(495, 167)
	pt3 = Point(5, 333)
	pt4 = Point(495, 333)
	pt5 = Point(167, 5)
	pt6 = Point(167, 495)
	pt7 = Point(333, 5)
	pt8 = Point(333, 495)
	ln1 = Line(pt1, pt2)
	ln1.setOutline(color_rgb(0, 0, 0))
	ln1.draw(win)
	ln2 = Line(pt3, pt4)
	ln2.setOutline(color_rgb(0, 0, 0))
	ln2.draw(win)
	ln3 = Line(pt5, pt6)
	ln3.setOutline(color_rgb(0, 0, 0))
	ln3.draw(win)
	ln4 = Line(pt7, pt8)
	ln4.setOutline(color_rgb(0, 0, 0))
	ln4.draw(win)
	



	#GAME PLAY
	status = gameOver(spots)
	while not status[0]:
		makeMove(win, spots, currPlayer[1], currPlayer[0])
		if currPlayer == player1:
			currPlayer = player2
		else:
			currPlayer = player1
		status = gameOver(spots)
	if status[1] == 1:
		rect = Rectangle(Point(180, 180), Point(320, 320))
		rect.setFill('white')
		txt = Text(Point(250, 230), "X wins")
		txt.setSize(20)
		rect.draw(win)
		txt.draw(win)
	elif status[1] == 0:
		rect = Rectangle(Point(180, 180), Point(320, 320))
		rect.setFill('white')
		txt = Text(Point(250, 230), "O wins")
		txt.setSize(20)
		rect.draw(win)
		txt.draw(win)
	else:
		rect = Rectangle(Point(180, 180), Point(320, 320))
		rect.setFill('white')
		txt = Text(Point(250, 230), "it's a tie")
		txt.setSize(20)
		rect.draw(win)
		txt.draw(win)
	txt1 = Text(Point(250, 290), "click anywhere to exit.")
	txt1.draw(win)
	win.getMouse()
	win.close()

#Update a move in spots and in win
def makeMove(win, spots, xo, player):
		if player == "computer":
			computerMove(win, spots, xo)
		else:
			userMove(win, spots, xo)

#User makes a move and updates win and spots
def userMove(win, spots, xo):
	Move_Coord = win.getMouse()
	Move = clickConvert(Move_Coord)
	while not validSpot(Move, spots):
		Move_Coord = win.getMouse()
		Move = clickConvert(Move_Coord)
	spots[Move[0]][Move[1]] = xo
	winUpdate(win, Move, xo)
	

#Computer makes a move and updates win and spots
def computerMove(win, spots, xo):
	Move = bestMove(spots)
	spots[Move[0]][Move[1]] = xo
	winUpdate(win, Move, xo)

#Update the graphics with a new 'x' or 'o' based on player's move
def winUpdate(win, move, xo):
	coords = (0, 0)
	if move[0] == 0:
		if move[1] == 0:
			coords = (84, 84)
		elif move[1] == 1:
			coords = (84, 249)
		else:
			coords = (84, 411)
	elif move[0] == 1:
		if move[1] == 0:
			coords = (249, 84)
		elif move[1] == 1:
			coords = (249, 249)
		else:
			coords = (249, 411)
	else:
		if move[1] == 0:
			coords = (411, 84)
		elif move[1] == 1:
			coords = (411, 249)
		else:
			coords = (411, 411)
	if xo == 1:
		img = Image(Point(coords[0], coords[1]), "X.png")
		img.draw(win)
	else:
		img = Image(Point(coords[0], coords[1]), "O.png")
		img.draw(win)

#wrapper for the minimax alpha beta function that returns the best move
def bestMove(spots):
	move = None
	bestScore = -1000000
	for i in range(0,3):
		for j in range(0,3):
			if spots[i][j] == None:
				newMove = (i,j)
				spots[i][j] = 0
				newScore = minimax(spots, 1, 1, -100000, 100000)
				spots[i][j] = None
				if newScore > bestScore:
					move = newMove
					bestScore = newScore
	return move

#returns minimax scores for various game states given by bestMove
def minimax(spots, xo, depth, alpha, beta):
	over = gameOver(spots)
	if over[1] == 1:
		return -1/depth
	elif over[1] == 0:
		return 1/depth
	elif over[0] == True and over[1] == None:
		return 0
	if xo == 0:
		maxVal = -10000000
		for i in range(0,3):
			for j in range(0,3):
				if spots[i][j] == None:
					spots[i][j] = 0
					newVal = minimax(spots, 1, depth+1, alpha, beta)
					spots[i][j] = None
					maxVal = max(maxVal, newVal)
					alpha = max(newVal, alpha)
					if alpha >= beta:
						return maxVal
		return maxVal
	else:
		minVal = 10000000
		for i in range(0,3):
			for j in range(0,3):
				if spots[i][j] == None:
					spots[i][j] = 1
					newVal = minimax(spots, 0, depth+1, alpha, beta)
					spots[i][j] = None
					minVal = min(minVal, newVal)
					beta = min(newVal, beta)
					if alpha >= beta:
						return minVal
		return minVal


#Check whether user's requested move is valid
def validSpot(move, spots):
	if spots[move[0]][move[1]] == None:
		return True
	return False

#Convert a click into coordinates in a tuple form 
def clickConvert(click):
	if click.x < 167:
		if click.y < 167:
			return (0,0)
		elif click.y < 333:
			return (0,1)
		else:
			return (0,2)
	elif click.x < 333:
		if click.y < 167:
			return (1,0)
		elif click.y < 333:
			return (1,1)
		else:
			return (1,2)
	else:
		if click.y < 167:
			return (2,0)
		elif click.y < 333:
			return (2,1)
		else:
			return (2,2)

#Returns whether there are three x's or o's in a row or tie. output: 'x' 'o' 'tie' or None
def gameOver(spots):
	for i in range(0, 3): #i represents rows/columns
		#check for vertical win
		if spots[i][0] != None and spots[i][0] == spots[i][1] == spots[i][2]:
			if spots[i][0] == 1:
				return (True, 1)
			return (True, 0)
		#check for horizontal win
		if spots[0][i] != None and spots[0][i] == spots[1][i] == spots[2][i]:
			if spots[0][i] == 1:
				return (True, 1)
			return (True, 0)
	#check for diagonal top left to bottom right win
	if spots[0][0] != None and spots[0][0] == spots[1][1] == spots[2][2]:
		if spots[0][0] == 1:
				return (True, 1)
		return (True, 0)
	#check for diagonal bottom left to top right win
	if spots[0][2] != None and spots[0][2] == spots[1][1] == spots[2][0]:
		if spots[0][2] == 1:
				return (True, 1)
		return (True, 0)
	# Check for a tie by seeing whether each spot on the board has a 'x' or 'o' in
	# it but does not satisfy any of the previous win conditions
	if spots[0][0] != None and spots[0][1] != None and spots[0][2] != None and \
		spots[1][0] != None and spots[1][1] != None and spots[1][2] != None and \
		spots[2][0] != None and spots[2][1] != None and spots[2][2] != None:
		return (True, None)
	return (False, None)

if __name__ == '__main__':
    ticTacToe()
