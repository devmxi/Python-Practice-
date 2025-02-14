#14/2/25 - VALENTINES, ily amelia 
#importing module
import random

#vars
Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
Symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '[', ']', '{', '}', '|', ';', "'", ':', ',', '.', '<', '>', '?', '/']
numLetters = 0 
numNums = 0 
numSymbols = 0 
password = ""
totalchars = 0 

print("Welcome to the Python Password Generator!")
numLetters = int(input("How many letters would you like in your password: "))
numNums = int(input("How many numbers would you like in your password: "))
numSymbols = int(input("How many symbols would you like in your password: "))

for i in range(0, numLetters):
   password += random.choice(Letters)

for i in range(0, numNums):
   password += random.choice(Numbers)
    
for i in range(0, numSymbols):
   password += random.choice(Symbols)

print("")
print(f"your password is {password}")