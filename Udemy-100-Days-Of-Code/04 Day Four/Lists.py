#Arrays // Lists 
# a data structure, for multiple peices of data 

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", 
                     "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", 
                     "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", 
                     "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", 
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", 
                     "Alaska", "Hawaii"]
 
#* array of the US states in order they joined 
#! arrays start from 0 

#-------------------------------------------------------------------------------------------------# 

#outputting from list 

print(f"First U.S state: {states_of_america[0]}") #how to get hold of specific data from list \\ this outputs first item in list 
print(f"Second to last U.S state: {states_of_america[-2]}") #negative numbers make it start counting from the end of the list 

#-------------------------------------------------------------------------------------------------# 

#changing specific items in lists 

#* tates_of_america[4] = "connect-iccut" refrence specific item, then set it to new data
#* print(states_of_america[4]) 

#-------------------------------------------------------------------------------------------------# 

#adding items to the end of the lists 
#* .append adds ONE item to the END of the list 

states_of_america.append("Canada") #adding canada to list of us states (never gonna happen btw)

print(f"NEW U.S state: {states_of_america[-1]} (not gonna happen)")

#* .extend will be added to the END of the list, adding all elements at once 
states_of_america.extend(["Greenland", "Mexico", "China"]) #adds 3 other countries to the states (also never going to happen, current news is crazy)

print(f"NEW U.S states: {states_of_america[-1]} {states_of_america[-2]} {states_of_america[-3]} (not gonna happen)")

#* .insert will add ONE item to a SPECIFIC POINT in the list 
states_of_america.insert(0, "Insert Test")  #put position in list first, then item
print(f"Insert test: {states_of_america[0]}")

#for more, look at google 

#-------------------------------------------------------------------------------------------------# 

#! challange
# Who will pay the bill challange (bill roulette)

import random

friends = ["Amelia","Alex", "David", "Matt", "Moksh", "Owen"] #list of names

print(random.choice(friends)) #random.choice chooses a random element from a list 