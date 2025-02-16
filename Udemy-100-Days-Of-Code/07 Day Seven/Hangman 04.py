import random
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

#Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ')
#!MADE BY: chrishorton on github
word_list=["aardvark", "baboon", "camel"]
counter = 0
placeholder = ""
chosen_word = random.choice(word_list)
gameover = False
correct_guess=[]
lives = 6 #TODO SET Lives to 6 and loose one whenever they guess an incorrect letter

for char in range(0, len(chosen_word)):
    placeholder += "_"

print(placeholder)

while gameover == False:
    guess = str(input("Please guess a letter: ")).lower()
    print(stages[1])

    display = ""
    
    for letter in chosen_word:
        if letter == guess:
            display += guess
            correct_guess.append(guess)
        elif letter in correct_guess:
            display += letter
        else:
            display += "_"
    if guess not in correct_guess:
        lives -= 1
        
    if lives == 6:
        print(stages[1])
    elif lives == 5:
        print(stages[2])
    elif lives == 4:
        print(stages[3])
    elif lives == 3:
        print(stages[4])
    elif lives == 2:
        print(stages[5])
    elif lives == 1:
        print(stages[6])
    elif lives == 0:
        print(stages[7])

    
    if "_" not in display:
        print("You win")
        gameover == True
    if lives <= 0:
        print("You Lose")
        gameover == True
        
            