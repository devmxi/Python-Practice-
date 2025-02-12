#* if conditional
#! indentation is important

#bath tub analogy
waterlevel = 50

if waterlevel > 80:
    print("drain water")
else:
    print("continue")
    
#if the water level in the bathtub hits 80 units, then the overflow will start to drain the water to maintain the water level

#-------------------------------------------------------------------------------------------------# 

#ticket box test

height = 0.0
age = 0 
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in CM: ")) #gets user input
height = round(height) #rounds height

if height >= 120: #checks if height is bigger than 120
    print("YAAY! You can ride the ride!") #output
    
    if age < 12: #nested if else statment
        print("Your ticket will cost $5")
        
    elif age <= 18: #else if statment, for more conditionals
           print("Your ticket will cost $7")
           
    else:
        print("Your ticket will cost $12")
        
else: #if height is less than 120
    print("Awh! You cannot ride the ride.")

#-------------------------------------------------------------------------------------------------# 

#* Comparison Operators:

#* > - greater than \\ < - less than
#* >= - greater than or equals to \\ <= - less than or equals to
#* == - equal to \\ != - not equal to
#* % - modulo \\ works out the remainder after the division: eg: 10 % 5 = 0 as theres no remainder eg: 10 % 3 = 1 as the remainder is one

#-------------------------------------------------------------------------------------------------# 

#odd or even

num = 0 
num = int(input("Please enter a number: "))

if num % 2 == 0: #checks if it divides cleanly therfore it would be even 
    print(f"{num} is even")
else: #if its not even, it has to be odd 
    print(f"{num} is not even")
    
#-------------------------------------------------------------------------------------------------# 

