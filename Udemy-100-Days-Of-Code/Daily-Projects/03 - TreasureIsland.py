#12/2/25

#vars 
choice = "" #string 

#welcome message
print('''   
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK - ascii.co.uk]
*******************************************************************************
''')

print("Welcome to Treasure Island. \nYour mission is to find the treasure. \nGood luck. \n")
choice = str(input("You`re at a crossroad. Where do you want to go? \nType left or right: ")).lower() #getting first user input, ALSO LOWERCASES ALL INPUT

#checking if user said left, if not game over
if choice == "left":
    choice = str(input("You reach a loch, theres a boat station. Do you wait for the boat or swim across? \nType swim or wait: ")).lower() #getting user input for next path, ALSO LOWERCASES ALL INPUT
    
    #checking if user said wait, if not game over
    if choice == "wait":
        choice = str(input("The boat arrives. It takes you to a nearby town. Theres three hotels with three colored doors. \nType red or yellow or blue: ")).lower() #gets final user input, ALSO LOWERCASES ALL INPUT

        if choice == "red":
            print("You got burned by fire. \nodd for a hotel, but whatever. \nGame over.") #final game over message
            
        elif choice == "blue":
            print("You got eaten by beasts. \nodd for a hotel, but whatever. \nGame over.") #final game over message
            
        elif choice == "yellow": 
            print("You win! \nYou found the treasure!") #game win condition \\ left, wait, yellow 
            
        else:
            print("Game over.") #final game over message
    else: 
        print("You got attacked by phirannas. \nGame over.")
        
else:
    print("You fall into a hole. \nGame over.")