from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



drink_name = Menu()
coffee_maker = CoffeeMaker()
payment_process = MoneyMachine()

is_on=True

while is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "off":
        is_on = False
    elif user_input == "report":
        coffee_maker.report()
        payment_process.report()
    else:
        drink_ordered=drink_name.find_drink(user_input)
        if drink_ordered:
            if coffee_maker.is_resource_sufficient(drink_ordered):
                if payment_process.make_payment(drink_ordered.cost):
                    coffee_maker.make_coffee(drink_ordered)

