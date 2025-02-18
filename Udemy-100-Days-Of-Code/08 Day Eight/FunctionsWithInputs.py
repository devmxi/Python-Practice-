
#* Functions! 
#* recap:

def greeting():
    print("Hello")
    print("Ni Hao")
    print("Hola")
    
greeting()
print("")

#-------------------------------------------------------------------------------------------------#

#* Functions with inputs

def greet(name): #! creating a var in the parenthasis for an input
    print(f"Hello {name}")
    
greet("moksh") #setting the variable name to moksh
print("")

#-------------------------------------------------------------------------------------------------#

#* Functions with more than one input

def greetings(name, location):
    print(f"Hello {name}")
    print(f"Whats it like in {location}?")

greetings("moksh", "UK")
print("")
#! Keyword arguments: 
greetings(location="Nowhere", name="Moksh")

#-------------------------------------------------------------------------------------------------#

