MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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


def ask():
    print("Please insert coins.")
    quarter = int(input("how many quarters?:"))
    dimes = int(input("how many dimes?:"))
    nickles = int(input("how many nickles?:"))
    pennies = int(input("how many pennies?:"))
    return 0.25*quarter+0.1*dimes+0.05*nickles+0.01*pennies


def lack(ingredient):
    print(f'''Sorry that's not enough {ingredient}.
Here is your money''')


water = 300
milk = 200
coffee = 100
money = 0
turn_off = False
while not turn_off:
    answer = input("What would you like? (espresso/latte/cappuccino):").lower()
    if answer == "report":
        print(f'''Water: {water}
Milk: {milk}
Coffee:{coffee} 
Money: {money}''')
    elif answer == "espresso" or answer == "latte" or answer == "cappuccino":

        my_coffee = MENU[answer]
        ingredients = my_coffee["ingredients"]
        cost_required = my_coffee["cost"]
        water_required = ingredients["water"]
        milk_required = ingredients["milk"]
        coffee_required = ingredients["coffee"]
        if water < water_required:
            lack("water")
        elif coffee < coffee_required:
            lack("coffee")
        elif milk < milk_required:
            lack("milk")
        else:
            amount = ask()
            if amount < cost_required:
                lack("money")
            else:
                money += cost_required
                milk -= milk_required
                water -= water_required
                coffee -= coffee_required
                return_money = round(amount - cost_required,2)
                if return_money > 0:
                    print(f"Here is ${return_money} in change")
                    print(f"Here is your {answer} ☕️. Enjoy!")
    elif answer == "off":
        turn_off = True








