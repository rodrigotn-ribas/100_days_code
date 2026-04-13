from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Objects
order = Menu() # create an object of the class Menu()
coffee_maker = CoffeeMaker() # create an object of the class CoffeeMaker()
money_machine = MoneyMachine() # create an object of the class MoneyMachine()

is_on = True

while is_on:
    choice = input(f"What would you like? ({order.get_items()}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report() # report the ingredients
        money_machine.report() # report the money
    else:
        drink = order.find_drink(choice)  # return an object of the class MenuItem()
        if coffee_maker.is_resource_sufficient(drink):
            is_transaction_successful = money_machine.make_payment(drink.cost) # try to make the payment
            if is_transaction_successful:
                coffee_maker.make_coffee(drink) # makes the coffee