
#* nesting lists and dictionaries inside dictionaries

#eg dictionary: 
capitals = {
    "Spain": "Madrid",
    "France": "Paris",
}

#-------------------------------------------------------------------------------------------------#

#* nested list in dictionary 
#* this dictionary has a key of countries and the values are lists of cities visited within thoes countries 

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany" : ["Munich", "Berlin"],
    
}

#-------------------------------------------------------------------------------------------------#

#* outputting something from said nested list:

print(travel_log["France"][1]) #prints lille 

#-------------------------------------------------------------------------------------------------#

#* outputting C from this list:
nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][0]) #* goes to third item, then first item in the third item

#-------------------------------------------------------------------------------------------------#

#* Updated Travel Log 

travel_log_new = { #dictionary
    "France": { #nested dictionary 
        "Times Visited" : 8,
        "Cities Visited": ["Paris", "Lille", "Dijon"] #nested list, inside a nested dictionary 
        },
    
    "Germany": {
        "Times Visited" : 12,
        "Cities Visited": ["Munich", "Berlin", "Hamburg"]
        },
}  

#Traversing the nested lists and nested dictionaries
print(travel_log_new["Germany"]["Cities Visited"][2])#* Hamburg