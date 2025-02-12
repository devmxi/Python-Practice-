#operators 
#* and - a and b are true: then runs
#* or - a or b are true: then runs
#* not - reverses output

#-------------------------------------------------------------------------------------------------# 

num = 12 

if num > 2 and num < 13:
    print("Both are true!") #if one is not true, whole statment becomes false 
else:
    print("One is UN-true!")
    
# OR 

if 13 > num > 2:
    print("Both are true!") #if one is not true, whole statment becomes false 
else:
    print("One is UN-true!")

    
#-------------------------------------------------------------------------------------------------# 

if num == 12 or num == 13: # if one is true, whole statment becomes true, only if both are false does the whole statment become false 
    print("One is true!")

#-------------------------------------------------------------------------------------------------# 

if not num < 0: #eg: not FALSE is true and not TRUE is false 
    print("num is NOT less than zero!!")

#-------------------------------------------------------------------------------------------------# 

# addition to ticket challange:
#vars
height = 0.0 #float
age = 0 #int
ticketPrice = 0 #int
photos = True #bool
age = int(input("Please enter your age: ")) #gets user input
height = float(input("Please enter your height in CM: ")) #gets user input
height = round(height) #rounds height

if height >= 120: #checks if height is bigger than 120
    print("YAAY! You can ride the ride!") #output
    
    if age < 12: #nested if else statment
        print("Your ticket will cost $5")
        ticketPrice = 5
    elif age <= 18: #else if statment, for more conditionals
           print("Your ticket will cost $7")
           ticketPrice = 7
    
    elif 45 <= age <= 55: #* SIMPLER WAY OF WRITING AND OPERATOR 
        
        print("Your ticket price is free!")
        
    else: 
        print("Your ticket will cost $12")
        ticketPrice = 12
    
    photos = bool(input("Would you like photos with your ticket? (True / False: )")) #asks user if they want photos, no matter age
    
    if photos == True:
        ticketPrice += 3 #adds to ticket bill
    
    print(f"Your final ticket cost is ${ticketPrice}") #outputs full ticket price 

else: #if height is less than 120
    print("Awh! You cannot ride the ride.")
