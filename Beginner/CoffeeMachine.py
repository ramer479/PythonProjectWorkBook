MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_CoffeeMachine_on = True


class InvalidArgumentException(Exception):
    pass


def validate_user_order(order):
    """validates the user order. raises exception for wrong input"""
    valid_input = list(MENU.keys())
    valid_input.append("report")
    valid_input.append("off")
    if order not in valid_input:
        raise InvalidArgumentException("The order provided by you is not served here. Please check menu options again")
    else:
        return order


def get_resource_report():
    """returns the report of resources"""
    print("The current resources are: ")
    print(f"Water content is {resources['water']} \nMilk content is {resources['milk']}"
          f" \nCoffee content is {resources['coffee']} \n ")
    print(f"The profit : {profit}")


def is_resources_sufficient(order):
    """Calculates existing resources and lets the user know if they are sufficient"""
    coffee_needs = MENU[order]['ingredients']
    for i in coffee_needs:
        if coffee_needs[i] >= resources[i]:
            return False
    return True


def user_coin_prompt():
    """Returns the total user money from coins inserted"""
    print("Please insert coins")
    total_money = int(input("how many quarters?: ")) * 0.25
    total_money += int(input("how many dimes?: ")) * 0.1
    total_money += int(input("how many nickles?: ")) * 0.05
    total_money += int(input("how many pennies?: ")) * 0.01
    return total_money


def calculate_money(money, order):
    """Calculate the money"""
    order_cost = MENU[order]['cost']
    if order_cost > money:
        print("Sorry bro, money is not sufficient. Please order again")
        return {'change': 0, "status": False}
    else:
        return {'change': money - order_cost, "status": True}


def get_coffee(order):
    global resources
    resources['coffee'] -= MENU[order]['ingredients']['coffee']
    resources['water'] -= MENU[order]['ingredients']['water']
    if order != "espresso":
        resources['milk'] -= MENU[order]['ingredients']['milk']
    print(f"Here You Go. There is Your {order} $COFFEE")


def take_coffee_order():
    global profit
    global is_CoffeeMachine_on
    input_coffee_order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    user_order = validate_user_order(input_coffee_order)
    if user_order == "report":
        get_resource_report()
    elif user_order == "off":
        is_CoffeeMachine_on = False
    else:
        if is_resources_sufficient(user_order):
            user_money = user_coin_prompt()
            print(f"User money inserted : {user_money}")
            is_money_sufficient = calculate_money(user_money, user_order)['status']
            if is_money_sufficient:
                get_coffee(user_order)
                user_change = round(calculate_money(user_money, user_order)['change'], 2)
                profit += MENU[user_order]['cost']
                if user_change > 0:
                    print(f"Here is your change {user_change}")
        else:
            print("Not Enough resources to take Order")


while is_CoffeeMachine_on:
    take_coffee_order()
