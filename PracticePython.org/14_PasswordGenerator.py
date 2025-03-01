#importing module
import random

Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
Symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '[', ']', '{', '}', '|', ';', "'", ':', ',', '.', '<', '>', '?', '/']
numLetters = 0 
numNums = 0 
numSymbols = 0 
password = ""
totalchars = 0 

def generate_password(letters, numbers, symbols, output):
    for i in range(0, letters):
        output += random.choice(Letters)

    for i in range(0, numbers):
        output += random.choice(Numbers)
        
    for i in range(0, symbols):
        output += random.choice(Symbols)
        
    return output


print("Welcome to the Python Password Generator!")
numLetters = int(input("How many letters would you like in your password: "))
numNums = int(input("How many numbers would you like in your password: "))
numSymbols = int(input("How many symbols would you like in your password: "))

print("")
print(f"your password is {generate_password(numLetters, numNums, numSymbols, password)}")
