#random module
# a small part of functionality in a project 

import random #importing the library into the project
import ModuleMaking #importing my own created module

#-------------------------------------------------------------------------------------------------# 

#generating random integers
print("Random Integer:")
randInt = random.randint(1,10) #generates random number 1 <= randNum <= 10 and assigns it to var 
print(f"{randInt} \n") #outputs 

#generating random floats 
print("Random Num between 1 and 0:")
randNum0_to_1 = random.random() #will create a number from 0 to 1, not including 1
print(f"{randNum0_to_1} \n")

#generating random floats
print("Random Float")
randFloat = random.uniform(1, 10) #will generate a random floating point num 1 <= randNum <= 10
print(f"{randFloat} \n")

#-------------------------------------------------------------------------------------------------# 

#using my own module! 
print(f"{ModuleMaking.favouriteNum}\n") #will print the var from ModuleMaking.py

#-------------------------------------------------------------------------------------------------# 

#Heaeds or tales activity

coinFlip = random.randint(0,1) #generating random number with a 50/50 chance

print("Heads or tales: ")
if coinFlip == 1:
    print("Heads")
else:
    print("Tails")
    
