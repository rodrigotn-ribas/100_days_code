from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

order = Menu()
coffee_maker = CoffeeMaker()

print(order)

order_choice = input(f"What would you like? ({order.get_items()}): ")
print(order.find_drink(order_choice))


coffee_maker.make_coffee(order)