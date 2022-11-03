from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_machine_on = True
while is_machine_on:
    coffee_drink = input(f'What would you like? {coffee_menu.get_items()}: ').lower()

    if coffee_drink not in ['espresso', 'latte', 'cappuccino', 'report', 'off']:
        print('invalid option')
    elif coffee_drink == 'report':
        coffee_maker.report()
        money_machine.report()
    elif coffee_drink == 'off':
        is_machine_on = False
    else:
        Drink = coffee_menu.find_drink(coffee_drink)

        if coffee_maker.is_resource_sufficient(Drink):
            if money_machine.make_payment(Drink.cost):
                coffee_maker.make_coffee(Drink)
