#Dec Vars 
word = "" #str

word = str(input("Please input a word: \n")) #gets user input 

#test check
print(word) #prints inputted word 
print(word[::-1]) #prints word backwards \\ uses slice statment - [::-1] means start at the end of the string, and move everything from the end of the string with the step -1, stop at the first letter, pos 0 

#conditional 
if word[::-1] == word: #checking if word backwards is = to the regular word
    print("it is a palindrome") #prints its a palindrome 
else:  #if doesnt meet condition, its not a palindrome 
    print("it is NOT a palindrome")#outputs message