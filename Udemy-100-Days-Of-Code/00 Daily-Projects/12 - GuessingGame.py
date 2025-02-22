import random

RANDNUM = random.randint(1,100)
guessnum = 0 
difficulty = ""
lives = 0
GameOver = False

def chooseDifficulty():
    '''Gets the user to choose a difficulty, and assigns lives based on it'''
    difficulty = str(input("Choose a difficulty: Type 'easy' or 'hard': ")).lower()\
        
    while difficulty != "easy" and difficulty != "hard":
        difficulty = str(input("ERROR. Please choose a difficulty: Type 'easy' or 'hard': ")).lower()
        
    if difficulty == "easy":
        return 10
    else: 
        return 5
    
def guess(guessamt):
    '''Gets User to guess a number, then outputs if its too high or too low, returns if they got it right or not.'''
    global RANDNUM, lives
    
    guessamt = int(input("Please make a guess: "))
    
    if lives != 1:
        if guessamt > RANDNUM:
            print("Too high. \nGuess again.")
            return False
        
        elif guessamt < RANDNUM:
            print("Too low. \nGuess again.")
            return False
        
    if guessamt == RANDNUM:
        print("Correct! You got it right!")
        return True
    
#TODO Print welcome message
print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 - 100.")
#print(f"correct num: {RANDNUM}") #*used for testing

#TODO check difficulty and assign lives
lives = chooseDifficulty()

while GameOver == False:
    print(f"You have {lives} attempts remaining to guess the number.")
    #TODO get user guess
    GameOver = guess(guessnum) #* assgigning to result of guess 

    if guess != RANDNUM: #*checking if guess is wrong
        lives -= 1 #* losing life for wrong guess
        if lives == 0:
            print("You have 0 lives remaining. You lose.") #* loss output
            GameOver = True
        
        
