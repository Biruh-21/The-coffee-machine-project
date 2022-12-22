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

resource = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0
}


def check_resource(your_order):
    if "water" in MENU[your_order]["ingredients"] and MENU[your_order]["ingredients"]["water"] > resource["Water"]:
        print("Sorry, there is not enough water.")
        return False
    elif "milk" in MENU[your_order]["ingredients"] and MENU[your_order]["ingredients"]["milk"] > resource["Milk"]:
        print("Sorry, there is not enough Milk.")
        return False
    elif "coffee" in MENU[your_order]["ingredients"] and MENU[your_order]["ingredients"]["coffee"] > resource["Coffee"]:
        print("Sorry, there is not enough Milk.")
        return False
    else:
        return True


while True:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order in MENU:
        if check_resource(order):
            print("Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))

            money_sum = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
            money_sum = round(money_sum, 2)
            cost = MENU[order]["cost"]

            if money_sum >= cost:
                changes = money_sum - cost
                changes = round(changes, 2)
                if money_sum > cost:
                    print(f"Here is ${changes} in change.")
                print(f"Here is your {order}☕️. Enjoy!")
                resource["Money"] += cost
                if "water" in MENU[order]["ingredients"]:
                    resource["Water"] -= MENU[order]["ingredients"]["water"]
                if "milk" in MENU[order]["ingredients"]:
                    resource["Milk"] -= MENU[order]["ingredients"]["milk"]
                if "coffee" in MENU[order]["ingredients"]:
                    resource["Coffee"] -= MENU[order]["ingredients"]["coffee"]
            else:
                print("Sorry that's not enough money. Money refunded.")
    elif order == "report":
        print(f"Water: {resource['Water']}ml")
        print(f"Milk: {resource['Milk']}ml")
        print(f"Coffee: {resource['Coffee']}g")
        print(f"Money: ${resource['Money']}")
    elif order == "off":
        break
