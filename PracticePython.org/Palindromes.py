#vars
word = ""

word = str(input("Please enter a word: ")) #getting user input 

#testing print, words should be the same 
print(word)
print(word[::-1]) #* the slice statment - [::-1] - meaans to start at the end of the string, and finish at the begining (pos 0 ) and move each character -1 space 

if word[::-1] == word: #checking if reversed word = word 
    print("The word is a palindrome")
else:
    print("The word is NOT a palindrome")