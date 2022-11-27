from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_obj = Menu()
coffee_obj = CoffeeMaker()
money_obj = MoneyMachine()
is_CoffeeMachine_on = True
profit = 0


def take_coffee_order():
    global is_CoffeeMachine_on
    input_coffee_order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    user_order = input_coffee_order
    if user_order == "report":
        coffee_obj.report()
        money_obj.report()
    elif user_order == "off":
        is_CoffeeMachine_on = False
    else:
        drink = menu_obj.find_drink(user_order)
        print(f"drink ingredients {drink.ingredients}")
        print(f"drink cost {drink.cost}")
        if coffee_obj.is_resource_sufficient(drink):
            print("resource sufficient")
            if money_obj.make_payment(drink.cost):
                coffee_obj.make_coffee(drink)
        else:
            print("Nooooooooo")



while is_CoffeeMachine_on:
    take_coffee_order()