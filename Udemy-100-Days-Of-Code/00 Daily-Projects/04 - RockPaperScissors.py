#13/2/25

#import module
import random

#vars
#! Credit to: wynand1004 on github for ASCII art 

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

#art

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

#art 

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

#art

#! Credit to: wynand1004 on github for ASCII art 

userChoice = 0  #int
compChoice = 0  #int 
art = [rock, paper, scissors]

#welcome nessage
print("Welcome to the Rock Paper Scissors game! \nYou will be playing against the computer.")

#getting user input
userChoice = int(input("Please select: Rock (type: 1) \ Paper (type: 2) \ Scissors (type: 3)\n"))

#input validation
while userChoice < 1 or userChoice > 3:
    userChoice = int(input("Error, please enter a valid input: Rock (type: 1) \ Paper (type: 2) \ Scissors (type: 3)\n"))
    
#generating random number, correlating to rock paper or scissors
compChoice = random.randint(1,3)

#printing art of choice user made
print(art[userChoice -1]) #* -1 because the choices are adjusted for counting from 0
    
#printing art of choice computer made
print(f"Computer chose: \n{art[compChoice -1]}")
    
#checking users win conditions 
#rock win condition
if userChoice == 1 and compChoice == 3: #user choice = rock \\ comp choice = scissors 
        print("You Win!!")

#paper win conditionals 
elif userChoice == 2 and compChoice == 1: #user choice = paper  \\ comp choice = rock 
        print("You Wins!!")
      
#scissor win conditionals
elif userChoice == 3 and compChoice == 2: #user choice = scissors \\ comp choice = paper
        print("You Win!!")
    
#tie conditional 
elif userChoice == compChoice: 
        print("Its a tie!!")

    #since weve already checked for player ones winnings, if none of them are true, and its not a draw, player two mustve won
else: 
        print("You lose :c ")