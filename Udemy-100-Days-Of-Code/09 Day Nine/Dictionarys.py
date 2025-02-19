#Python Dictionaries
#* theyre like irl dictionaries, show the value of a key 

colors = {
    "apple": "red",
    "banana": "yellow",
    "kiwi": "brown",
    }

#* this dictionarys key is fruits and the value is the color of the fruits
print(colors["apple"]) #* prints value of key

#-------------------------------------------------------------------------------------------------#

#* adding to dictionaries
colors["pear"] = "green" 
      #* key      value 
print(colors)

#-------------------------------------------------------------------------------------------------#

#* editing an item in a dictionary
colors["kiwi"] = "browngreen"
print(colors["kiwi"])

#-------------------------------------------------------------------------------------------------#

#* looping through dictionaries
for key in colors:
    print(key) #? this outputs each key in the dictionary without its value attached to it
    
#-------------------------------------------------------------------------------------------------#

#* wiping a dictionary
colors = {}
print(colors)

