#Nested lists

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", 
                     "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", 
                     "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", 
                     "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", 
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", 
                     "Alaska", "Hawaii"]

#-------------------------------------------------------------------------------------------------# 

#! Index out of range errors 
# finding length of list:

print(len(states_of_america)) # outputs amount of items in list (50)

# if you tried to print something out of the range you get an `index out of range error`
#* print(states_of_america[len(states_of_america)]) - would produce error, because its larger than the range of the list, final list item is 49 because it starts counting from 0
#* print(states_of_america[len(states_of_america)-1]) - fixes it 

#-------------------------------------------------------------------------------------------------# 

#* nested lists

#list of fruits that have the most pesticides (2019)
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears",]

#list of veg that have the most pesticides (2019)
vegtables = [ "Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

#list of combined fruit and veg
dirtyDozen = [fruits, vegtables] #* Nested List, with the fruits list and vegtables list in the same list
print(dirtyDozen) #showcases structutre 
print(dirtyDozen[0]) #*prints out first list, as its the first item
print(dirtyDozen[0][2]) #* goes to the first list, fruits, then prints out the 2nd item in that list, which is my fav fruit: apples 

