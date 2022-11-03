from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

CoffeeMenu = Menu()
CoffeeResource = CoffeeMaker()
CoffeeMoney = MoneyMachine()

is_machine_on = True
while is_machine_on:
    CoffeeDrink = input(f'What would you like? {CoffeeMenu.get_items()}: ').lower()

    if CoffeeDrink not in ['espresso', 'latte', 'cappuccino', 'report', 'off']:
        print('invalid option')
    elif CoffeeDrink == 'report':
        CoffeeResource.report()
        CoffeeMoney.report()
    elif CoffeeDrink == 'off':
        is_machine_on = False
    else:
        Drink = CoffeeMenu.find_drink(CoffeeDrink)

        if CoffeeResource.is_resource_sufficient(Drink):
            if CoffeeMoney.make_payment(Drink.cost):
                CoffeeResource.make_coffee(Drink)
