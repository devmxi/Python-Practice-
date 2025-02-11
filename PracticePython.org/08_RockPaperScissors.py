#vars
player1Input = ""
player2Input = ""
newGame = False

#conditional loop, making sure game loops 
while newGame != True: 
    
    player1Input = str(input("PLayer 1: please enter: rock, paper, or scissors: \n")) #asking for player 1 input 
    player2Input = str(input("Player 2: please enter: rock, paper, or scissors: \n")) #asking for player 2 input 

    # Win conditionals
    #rock win conditionals 
    if player1Input == "rock" and player2Input =="scissors":
        print("Player One Wins!!")
      
    #scissor win conditionals
    elif player1Input == "scissors" and player2Input =="paper":
        print("Player One Wins!!")
        
    #paper win conditionals 
    elif player1Input == "paper" and player2Input =="rock":
        print("Player One Wins!!")
    
    #tie conditional 
    elif player1Input == player2Input:
        print("Its a tie!!")

    #since weve already checked for player ones winnings, if none of them are true, and its not a draw, player two mustve won
    else: 
        print("Player Two wins!! ")
        

    newGame = bool(input("Would you like to stop? (True // False)\n")) #get user input for continuation of game 
    

    