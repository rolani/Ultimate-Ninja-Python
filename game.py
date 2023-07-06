import random
from utils import newline, message, instructions, is_int



balance = 100
moves = [ ]

print("Welcome to the game, Please enter your name: ")
name = input().capitalize()
	
        
def main():
    print("Welcome "+ name )
    print("You currently have a balance of $"+str(balance) )
    welcomeMenu()

def welcomeMenu():
	print("Main Menu: " + newline)
	print("(I)nstructions" + newline + "(P)lay game" + newline + "(Q)uit game" + newline)
	print("Make a choice from the options above: ")
	menuOption()
	

def gameInstruction():
    print(instructions + newline)
    print(message + newline)
    print("Choose wisely. " + newline)
    welcomeMenu()

def playGame(bet):
	try:
		playerMove = int(input())
		if is_int(playerMove) == True:
			moveList = [""] * 7
			moveList[1] = "(1) Punch of Fury"
			moveList[2] = "(2) Kick of Punishment"
			moveList[3] = "(3) Sword of Justice"
			moveList[4] = "(4) Shuriken of Vengeance"
			moveList[5] = "(5) Numchunks of Anger"
			moveList[6] = "(6) Knife of Freedom"
			if playerMove >= 7 or playerMove <= 0:
				print("Please a number enter between 1 and 6: " + newline)
				playGame()
			else:
				move = moveList[playerMove]
				computerMove = int(random.randint(1,6))
				answer = moveList[computerMove]
				print("You chose " + move)
				print("Computer chose " + answer)
				vsMatch(playerMove, computerMove, bet)
				#welcomeMenu()
	except:
		exit()
		#print("Please try again!!!")
		#welcomeMenu()
    
	
def vsMatch(playerMove: int, computerMove: int, bet: int):
	global balance
	global moves

	# moves based on game rules
	attack_board = [[0,0,0,1,1,0],
		[1,0,0,0,1,0],
		[1,1,0,0,0,1],
		[0,1,1,0,0,1],
		[0,0,1,1,0,0],
		[1,1,0,0,1,0]]
	a = playerMove - 1
	b = computerMove - 1
	if playerMove == computerMove:
		print("Tie!! No Winner!!!" + newline)
		balance = balance
	elif attack_board[a][b] == 0:
		print("Player loses!!!" + newline)
		balance = balance - bet
	elif attack_board[a][b] == 1:
		print("Player wins!!!" + newline)
		balance = balance + bet
	print("You currently have a balance of $"+str(balance))
	moves.append(balance)
	welcomeMenu()

def menuOption():
	global balance
	choice = input().upper()
	if choice == "Q":
		quitOption()
		quitGame()
	elif choice == "I":
		gameInstruction()
	elif choice == "P":
		if balance > 0:
			gameAccount()
		else:
			quitGame()
	else:
		print("Invalid choice, enter I for Instruction, P to Play or  Q to Quit")
		menuOption()

def gameAccount():
	global balance
	print("You currently have a balance of $"+str(balance))
	print("Place your bet against the computer in multiples of $5: ") 
	try:
		bet = int(input())
		if is_int(bet) == True:
			if balance <= 0:
				exit()
			if bet > balance:
				print("Sorry you do not have sufficient balance. Try again!!!")
				welcomeMenu()
			else:
				if (bet%5) != 0:
					print("Your bet must be in multiples of $5!!!")
					print("Enter your bet again in multiples of $5: ")
					gameAccount()
				else:
					#balance = balance - bet
					#moves.append(str(bet))
					#print(moves)
					print(message)
					print("Choose an attack by selecting from 1 and 6: " +newline)
					playGame(bet)
		else:
			print("Please enter a valid bet in multiples of $5: ")
			gameAccount()		
					
	except:
		exit()

def quitOption():
	round = 1
	global balance
	global moves
	print("Goodbye! "+name+ ". Your final balance is : $"+str(balance)+newline)
	print("Your balance history is $100")
	#print(moves)
	for mov in moves:
		print("After round " +str(round)+ ": $" +str(mov))
		round += 1
def quitGame():
	exit()	 
if __name__ == '__main__':
	main()
