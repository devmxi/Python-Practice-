#import library
import random

#vars
RandNum = random.randint(1,9) #random int 1-9
GuessNum = 0 #int
GuessAmt = 0 #int

#conditional loop, if the guessed number doesnt equal randomly generated number
while GuessNum != RandNum: 
    
    GuessNum = input("Please guess a number between 1 - 9 or type `exit` to exit : ") #get user input 
    
    #checks if user entered exit
    if GuessNum == "exit":
        break
    else: 
        GuessNum = int(GuessNum) #turns string input into int 
    
    GuessAmt += 1 # keeps running total of amount of guesses
    
    #input validation 
    while GuessNum < 1 or GuessNum > 9: 
        GuessNum = int(input("Error! Please enter a number between 1 - 9: ")) #error output

    #conditional to check too high / low 
    if GuessNum > RandNum:
        print("Too high! Try again \n")
    elif GuessNum < RandNum:
        print("Too low! Try again \n")

#outputs 
if GuessNum == RandNum: 
    print(f"Well done! You guessed {GuessNum} which was correct!! You guessed correctly in {GuessAmt} guesses!\n")
else:
    print("Try again next time!")
