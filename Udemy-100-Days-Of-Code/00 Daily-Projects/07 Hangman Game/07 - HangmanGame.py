import random
import Word_List 
import Art 
#!MADE BY: chrishorton on github
stages= ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

counter = 0
placeholder = ""
chosen_word = random.choice(Word_List.words)
gameover = False
correct_guess=[]
lives = 6

for char in range(0, len(chosen_word)):
    placeholder += "_"

print(Art.art)
print("")
print("This is your word:")
print(placeholder)
print("")

while gameover == False:
    print(f"You have {lives} lives left \n")
    
    guess = str(input("Please guess a letter: ")).lower()
    
    while guess in correct_guess:
        guess = str(input(f"You`ve already guessed {guess}. Please guess again: ")).lower()
    
    if guess not in chosen_word:
        print(f"{guess}, was not in the word. You loose a life.")
        lives -= 1
        
    if lives == 6:
        print(stages[0])
    elif lives == 5:
        print(stages[1])
    elif lives == 4:
        print(stages[2])
    elif lives == 3:
        print(stages[3])
    elif lives == 2:
        print(stages[4])
    elif lives == 1:
        print(stages[5])
    elif lives == 0:
        print(stages[6])
        gameover = True
        print(f"You Lose, You lost all your lives. The word was: {chosen_word}")
        break
        
    
    display = ""
    
    for letter in chosen_word:
        if letter == guess:
            display += guess
            correct_guess.append(guess)
        elif letter in correct_guess:
            display += letter
        else:
            display += "_"

    print(display)
    

    
    if "_" not in display:
        print("You win!! You guessed the word!! Well done!")
        gameover = True
    if lives <= 0:
        print("You Lose")
        gameover = True
        
