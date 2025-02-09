#var 
name = "" #str 
age = 0 #int 
repeat = 0  #int
CenAgeYear = 0 #int 

name = str(input("Please enter your name: ")) #assigning value to var and asking for input 
age = int(input("Please enter your current age: ")) #assigning value to var and asking for input 
repeat = int(input("Please enter how many times youd like the final message to repeat. "))

#input validation for ages under 0 
while age < 0:
    age = int(input("Error! Please enter an age greater than 0")) #outputting error message 

#calculating diffrence
CenAgeYear = 100 - age

#checking if value is negative 
if CenAgeYear <  0: 
    print("Youve already turned 100 years old! congrats!")

# calculating year based on the year 2025 (current)
CenAgeYear = 2025 + CenAgeYear

# looping final message amount of times asked to repeat 
for i in range(repeat):
    print(name, "You will turn 100 years old in ",CenAgeYear) #final output 
