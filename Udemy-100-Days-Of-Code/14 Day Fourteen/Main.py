
#TODO import libraries
import random
import Art
from GameData import data

userInput = ""
celeb1 = random.choice(data)
celeb2 = {}
celebs = [""] * 2
score = 0 
gameOver = False

#TODO get random dictionary values function
def randCeleb(celeb1, celeb2, celebrities):
    
    '''Generates random second celebrity, and adds all celebrities to the list. Makes sure it cant be two of the same celeb, returns list with both celebrities in dictionaries. '''
    
    #TODO get + return random values from the dictionaries
    celeb2 = random.choice(data)
    
    celebrities[0] = celeb1
    celebrities[1] = celeb2
    
    while celebrities[0] == celebrities[1]:
        celebrities[1] = random.choice(data)
    
    return celebrities 
    
#TODO display + comparasin fucntion inputs: values from prev function 
def displayCelebs(celebrities):
    ''' Displays the logo and both celebrities, if the score is greater than 1 then also displays current score. returns nothing'''
    print(Art.logo)
     #TODO display both celeberities
     
    if score >= 1:
        print(f"You`re right! Current score: {score}")
        
    print(f"Compare A: {celebrities[0]['name']}, a {celebrities[0]['description']}, from {celebrities[0]['country']}")
    print(Art.vs)
    print(f"Compare B: {celebrities[1]['name']}, a {celebrities[1]['description']}, from {celebrities[1]['country']}")
    
   
    
#TODO Compare follower counts inputs: values from random dictionary function
def compareFollowers(celebrities):
    '''Compares the follower counts of both celebrities, returns a or b corresponding for what celeb has the higher follow count.'''
    # used for testing print(celebrities[0]['follower_count'])
    # used for testing print(celebrities[1]['follower_count'])
    
    #TODO check follower counts, return A // B 
    if celebrities[0]['follower_count'] > celebrities[1]['follower_count']:
        # used for testing print("A")
        return "a"
    else:
        # used for testing print("B")
        return "b"
   
#TODO Get user Char input function
def getUserInput(userGuess):
    '''Gets users guess, validates input to a or b, returns user guess.'''
    userGuess = str(input("Who has more insta followers? Type 'A' or 'B': ")).lower()
    
    #TODO input validation
    while userGuess not in ["a","b"]:
        userGuess = str(input("ERROR: Who has more insta followers? Type 'A' or 'B': ")).lower()
        
        
    #TODO Return user input
    return userGuess
    
#TODO Get game result function
def getGameResult(userInput, compareFollowers):
    '''Calculates if user got it correct or incorrect, if correct clears console. returns bool'''
    #TODO Return if choice inputted and choice comparasin are equal or not
    if compareFollowers == userInput:
        
        print('\033c')
        return False
    #TODO else: game over
    else: 
        return True
    
def newCelebrity(celebrities, compareFollowers):
    '''Sets Correct guess to new celebrity, returns new celebrity'''
    if compareFollowers == "a":
            nextceleb = celebrities[0]
    else:
            # used for testing print("reassigned")
            nextceleb = celebrities[1]
    
    return nextceleb
        
    
    
while gameOver == False:
    
    randCeleb(celeb1, celeb2, celebs)
    # used for testing print(celebs[0])
    # used for testing print(celebs[1])
    displayCelebs(celebs)
    gameOver = getGameResult(getUserInput(userInput), compareFollowers(celebs)) #* assigns to game over
    
    if gameOver == False: #* only runs if its false
        
        celeb1 = newCelebrity(celebs, compareFollowers(celebs)) #* gets new celebrity and assigns to celeb 1, the first to be displayed
        score += 1 #* score increase // running total 
        # used for testing print(score)
        # used for testing print(celeb1)
        
    else:
        break
    
print(f"You lost. Your final score is {score}.") #* final output message
    
    