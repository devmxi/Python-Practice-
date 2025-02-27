MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0, 
    
}

user_action = ""

money = {
    "quarters": 0.0,
    "dimes": 0.0,
    "nickels": 0.0,
    "pennies": 0.0,
}

def get_resources():
    if resources['money'] == 0:
        return(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\n")
    else: 
        return(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: ${resources['money']}")
    
def enough_resources(drink, machine_resources):
    global MENU
    water = 0
    coffee = 0
    milk = 0
    total = 0 
    
    if machine_resources["water"] >= MENU[drink]["ingredients"]["water"]:
        water += 1
    if machine_resources["coffee"] >= MENU[drink]["ingredients"]["coffee"]:
        coffee += 1
    if machine_resources["milk"] >= MENU[drink]["ingredients"]["milk"]:
        milk += 1

    total = milk + coffee + water
    if total == 3: 
        return True
    
     #TODO if no - print not enough resources, return back to start
    elif total == 2 and water == 0: 
        print(f"Sorry there is not enough water.")
        
    elif total == 2 and coffee == 0: 
        print(f"Sorry there is not enough coffee.")
        
    elif total == 2 and milk == 0: 
        print(f"Sorry there is not enough milk.")
        
    else:
        print("Sorry. Not enough ingredients.")
        
    return False 
    
def insert_coins(wallet):  
    print("Please insert coins:")
    for coins in wallet:
        wallet[coins] = input(f"How many {coins}?: ")

def calculate_money(wallet):
    total_value = 0
    
    total_value += float(wallet["quarters"]) * 0.25
    total_value += float(wallet["dimes"]) * 0.1
    total_value += float(wallet["nickels"]) * 0.05    
    total_value += float(wallet["pennies"]) * 0.01
    return round(total_value,2)

def deduct_resources(machine_resources, drink):
    global MENU
    for ingredient in ["water", "milk", "coffee"]:
        machine_resources[ingredient] -= MENU[drink]["ingredients"][ingredient]
    
    
#TODO - turn machine off when action == off 
while user_action != "off": 
    #TODO - check what the user wants to do:

    user_action = input("What would you like? (esspresso / latte / cappuccino // help to view more commands): ").lower()
    #TODO - extra: add help, to show all extra commands
    
    #TODO - if action == report, print the report of resources
    if user_action == "report": 
        print(get_resources())
        
    #TODO - if user wants to make a drink, then check if resources are sufficent
    elif user_action in ["espresso", "latte", "cappuccino"]: 
        
        if enough_resources(user_action, resources):
            #TODO if yes - prompt coin insert
            insert_coins(money)
            total_value = calculate_money(money)
            
            #TODO then check if money is enough to cover the cost
            if total_value >= MENU[user_action]["cost"]:
                #TODO if yes - make drink, deduct needed resources, calculate and offer change, add needed amount to money in resources
                change = total_value - MENU[user_action]["cost"]
                resources["money"] = MENU[user_action]["cost"]
                
                if change > 0:
                    print(f"Here is your change: ${change}") 
                
                #TODO output here is your drink, enjoy! 
                deduct_resources(resources, user_action)
                print(f"Here is your {user_action} Enjoy!\n")

            else:
                   #TODO if no - print money refunded, do not add to resources
                   print("Not enough. Money Refunded.\n")
    
    elif user_action == "restock":
            resources = {
                        "water": 300,
                        "milk": 200,
                        "coffee": 100, 
                        "money": total_value,
                        
                        }
            print("restocked.\n")
        
    elif user_action == "help":
        print("off - turns off the machine\nreport - shows machines stock levels\nrestock - sets stock back to default\nhelp - to view this menue\n")
        
#15/100 - was a challange