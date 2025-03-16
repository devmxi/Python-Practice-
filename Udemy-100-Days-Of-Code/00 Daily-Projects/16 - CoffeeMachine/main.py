from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_power = "on"
user_choice = ""
drink_choice = ""
machine = CoffeeMaker()
machine_money = MoneyMachine()
menu = Menu()

while machine_power == "on": 
    user_choice = input(f"What would you like to drink? {menu.get_items()}: ").lower
    
    if user_choice == "off":
        break
    elif user_choice == "report":
        machine.report()
        machine_money.report()
    else:
        order = menu.find_drink(user_choice)
        if machine.is_resource_sufficient(order) and machine_money.make_payment(order.cost):
            machine.make_coffee(order)
        
