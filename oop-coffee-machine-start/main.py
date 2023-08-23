# import coffee_maker
# import money_machine
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
menu = Menu()
name = menu.get_items()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while is_on:

    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == 'off':
        break
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()

    else:
        selected_drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(selected_drink):
            money_machine = MoneyMachine()
            if money_machine.make_payment(selected_drink.cost):
                coffee_maker.make_coffee(selected_drink)

