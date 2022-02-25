from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_off = False
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
menu_item = MenuItem("name", "water", "milk", "coffee", "cost")

while not machine_off:
    wanted_coffee = input(f"What would you like? ({menu.get_items()}): ")
    if wanted_coffee == "off":
        machine_off = True
    elif wanted_coffee == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(wanted_coffee)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
