
#* imageine you have a house with a fence around it, inside the garden you have an apple tree. This means that only you and your family can access it as you live in the house
#* now imagine you have an apple tree out on the curb, thats a free for all, any one of you or your neighbors can take the fallen apples.

#* this is scope

apples = 1 #set amt of apples to one

def increaseApples():
    apples = 2 #sets amt of apples to 2, but only inside the function 
    print(f"Apples inside function {apples}") 
    
increaseApples() #*will output 2
print(f"apples outside the function {apples}") #* will output 1

#-------------------------------------------------------------------------------------------------#

# def drinkPotion():
#     potionStrength = 1 
#     print(potionStrength)
    
# drinkPotion()
# print(potionStrength) #! this shows local scope, as the var is only defined in the function, it can only be used in the function

#-------------------------------------------------------------------------------------------------#

# health = 10 #! Globale Variable as it was defined in the 'body' of the program
# def drinkPotion():
#     potionStrength = 1  #! this shows local scope, as the var is only defined in the function, it can only be used in the function
#*    print(health)
    
# drinkPotion()
#*print(health)

#-------------------------------------------------------------------------------------------------#

#* There is no block scope in python

if 3 < 5:
    oranges = 1

print(oranges) #! this shows that it isnt blocked by if or while loops

#-------------------------------------------------------------------------------------------------#