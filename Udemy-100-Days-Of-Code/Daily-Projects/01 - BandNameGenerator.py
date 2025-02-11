#11/2/25

#declare variables 
cityName = "" #str
petName = "" #str
bandName = "" #str

print("Welcome to the Band Name Generator.\n") #outputs welcome message 
cityName = str(input("What`s the name of the city you grew up in: \n")) #asks for input and assgins it to the variable 
petName = str(input("What`s the name of your pet: \n")) #asks for input and assgins it to the variable 
bandName = cityName + " " + petName #concatinates both to create band name 

print("Your band name could be: ", bandName) #outputs band name 

# 1/100  - ROAD 2 100 :D 