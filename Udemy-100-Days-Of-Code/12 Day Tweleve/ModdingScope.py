
#*How do we modify something with global scope in a function?

apples = 1 #set amt of apples to one

def increaseApples():
    global apples #* This tells the function to not make a new variable, but to use the global one instead
    apples = 2 
    print(f"Apples inside function {apples}") 
    
increaseApples() #*will output 2
print(f"apples outside the function {apples}") #* will output 2 

#! we dont usually do this as it is confusing and is bug-prone, only when modifying the variable
#* They are helpful to use when using CONSTANTS

#-------------------------------------------------------------------------------------------------#

#? Then what do we do
#* we can use the return statment:

apples = 1 #set amt of apples to one

def increaseApples(amtapples):
    return amtapples + 1
    
print(increaseApples(apples)) #* outputs incremental increase in apples

#-------------------------------------------------------------------------------------------------#

#* Global Constants
PI = 3.14159265 #* always name them in all uppercase, this makes them a constatnt

def circleArea(radius):
    global PI #! as pi will always remain constant it makes sense to use the global.

    area = radius * radius * PI
    return area