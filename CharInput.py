#var 
name = ""
age = 0
repeat = 0 
CenAgeYear = 0

name = str(input("Please enter your name: "))
age = int(input("Please enter your current age: "))

while age < 0:
    age = int(input("Please enter an age greater than 0"))

CenAgeYear = 100 - age

if CenAgeYear <  0: 
    print("Youve already turned 100 years old! congrats!")

CenAgeYear = 2025 + CenAgeYear

for i in range(repeat):
    print(name, "You will turn 100 years old in ",CenAgeYear)
    