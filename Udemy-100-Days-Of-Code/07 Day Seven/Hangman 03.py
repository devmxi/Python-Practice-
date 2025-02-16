#* section two
import random
word_list=["aardvark", "baboon", "camel"]
counter = 0
placeholder = ""
chosen_word = random.choice(word_list)
gameover = False
correct_guess=[]

for char in range(0, len(chosen_word)):
    placeholder += "_"

print(placeholder)

#TODO Use a while loop to get the user to guess words again and again
while gameover == False:
    guess = str(input("Please guess a letter: ")).lower()
    
    #TODO Update for loop for previous guesses aswell
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
        print("You win")
        gameover == True
            