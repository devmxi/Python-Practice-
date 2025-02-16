#* section one 
import random
word_list=["aardvark", "baboon", "camel"]

#TODO choose random word from word list and give it a variable then print
chosen_word = random.choice(word_list)
print(chosen_word)

#TODO ask user to guess a letter, assign it to a variable and make it lowercase
guess = str(input("Please guess a letter: ")).lower()

#TODO check if the guessed letter is in the chosen word
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")