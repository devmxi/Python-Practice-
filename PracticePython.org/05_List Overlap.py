#import library 
import random

listlen = 0 #dec int
listlen = int(input("How long would you like the list to be: \n")) #asks for input adn assigns to var 

#generates fully random list, with lengths based on user input 
list1 = random.sample(range(1, random.randint(2, 50)), listlen) #list1 - var \\ random.sample - list with randomly selected items \\ range - creates and defines range \\ random.randint - generates random integer \\ listlen - length of list 
list2 = random.sample(range(1, random.randint(2, 50)), listlen) #list2 - var  ^^ 

# Testing lists 
# list1 = [1,2,3] 
# list2 = [1,4,5]

#printing list for manual check - since their random 
print(list1)
print(list2)

#outputs item if commonality is found 
for item in list1:
    if item in list2:
        print(item)