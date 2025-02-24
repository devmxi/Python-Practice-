import random

#* Everyone makes bugs, so dont be sad about them.
#* This document will go over how to debug a problem:
# TODO, step one describe the problem, break it down into smaller chunks and an understandable format

#* Problem one:
#! this code will never output the string 'You got it!' 

def function1():
    for i in range(1, 20):
        if i == 20:
            print("You got it!")
            
function1()

#* lets describe the problem:
#* what is the loop doing? the loop is setting the variable i to a number that goes from 1, 19 as it starts at index 0 and goes to index 20
#* the function is going to print when the variable i is set to 20 
#* the assumtion is that i will eventually reach 20 

#-------------------------------------------------------------------------------------------------#

#* fixing the issue there: 
#* the assumtion is wrong, and the key thing is to check what assumtion is the inccorect one so we know how to fix it.
#* now that we know i will never hit 20, and we know why it will never hit 20, we can fix the issue. 

def function1():
    for i in range(1, 21):
        if i == 20:
            print("You got it!")
            
function1()

#-------------------------------------------------------------------------------------------------#

#* Problem two:
#! This code will only produce an error sometimes

dicenums = [1,2,3,4,5,6]
dice_pos = random.randint(1,6)
#print(dicenums[dice_pos])

#* With these types of bugs, we should try to reproduce the error so we can truley figure out whats going wrong

#! This code will produce an error 100% of the time, due to testing we found out that its only the 6th index that causes an issue
# dicenums = [1,2,3,4,5,6]
# print(dicenums[6])

#* now that we know where the problem is, and what causes the problem (the index being out of range) we can fix it

dicenums = [1,2,3,4,5,6]
dice_pos = random.randint(0,5)
print(dicenums[dice_pos])

#-------------------------------------------------------------------------------------------------#

#* Problem three: 
#! when you enter the year 1994 this code will do nothing. 

year = int(input("Whats your year of birth"))

if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are Gen Z")
    
#* In this issue, when its a logical issue, we should try to be the computer and predict through each line what its going to do

year = int(input("Whats your year of birth")) #* lets input 1994

if year > 1980 and year < 1994: #* here we can see that it will check if its greater than 1980, which is true
                                #* then we move on to if its less than 1994 which is not true. So this statment cannot be run
    print("You are a millenial.") 
    
elif year > 1994:               #* now it will check of its greater than 1994, which 1994 isnt. so it will move on not doing anything.
    print("You are Gen Z")
    
#* to fix that we simply need to change a statment, so that it catches the time where it does equal to exsactaly 1994

year = int(input("Whats your year of birth"))

if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year >= 1994:
    print("You are Gen Z")
    
#-------------------------------------------------------------------------------------------------#

#* problem four: 

#* fix in editor editors, they will show up highlighted. 

#* look up in console errors

try:
    age = int(input("How old are you: "))
except ValueError:
    print("You have not typed in a number, please use the digits on your keyboard: ")
    
#* this will catch the console error, and display a diffrent pathway

#-------------------------------------------------------------------------------------------------#

#* problem five:

#* use print to find where the error is 

#-------------------------------------------------------------------------------------------------#

#* problem six:

#* use a debugger!
#* I used a debugger to fix this code!

import random
import Maths

def mutate(listA): # function to change every item in a list 
    listB = [] #* assigning a new empty list 
    new_item = 0 #* assigning a new empty item
    
    for item in listA: #* for loop for each item in the original list 
        new_item = item * 2
        new_item += random.randint(1,3)
        new_item = Maths.add(new_item, item)
        listB.append(new_item) #* adds mutilated version to new list 
        
    print(listB) #* prints new list

mutate([1,3,4,5,6,3,6,4])

#-------------------------------------------------------------------------------------------------#