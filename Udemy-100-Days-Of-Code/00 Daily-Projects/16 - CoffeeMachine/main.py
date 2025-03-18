from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_power = "on"
user_choice = ""
drink_choice = ""
machine = CoffeeMaker()
machine_money = MoneyMachine()
menu = Menu()

def print_report():
        machine.report()
        machine_money.report()
    

while machine_power == "on":
    #*gets user input
    user_choice = input(f"What would you like to drink? {menu.get_items()}: ").lower()
    
     #*checks for custom commands
    if user_choice == "off": 
        break
    elif user_choice == "report":
        print_report()
        
    #* gets menu item of selected drink
    order = menu.find_drink(user_choice)
    if machine.is_resource_sufficient(order): #*checks for sufficient resources
        price = order.cost #* gets cost of drink
        if machine_money.make_payment(price): #*gets payment
            machine.make_coffee(order) #*makes coffee
            