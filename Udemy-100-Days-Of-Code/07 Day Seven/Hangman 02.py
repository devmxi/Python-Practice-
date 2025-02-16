#* section two
import random
word_list=["aardvark", "baboon", "camel"]
counter = 0
placeholder = ""
chosen_word = random.choice(word_list)

#TODO Create a string called placeholder that has the same number as blanks as the chosen word. 
for char in range(0, len(chosen_word)):
    placeholder += "_"

print(placeholder)

guess = str(input("Please guess a letter: ")).lower()

#TODO Create a display that puts the letters in the right places 
display = ""
for letter in chosen_word:
    if letter == guess:
        display += guess
    else:
        display += "_"
        
print(display)
        

