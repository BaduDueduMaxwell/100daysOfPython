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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


profit = 0

def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there's not enough {item}")
            return False
        return True

def process_coins():
    print("Please insert coins")
    total = 0
    total += int(input("How many quarters? ")) * 0.25
    total += int(input("How manu dimes? ")) * 0.10
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total

def transaction_successful(money_received,drink):
    global profit
    if money_received < MENU[drink]['cost']:
        print("Sorry that's not enough moneu. Money refunded.")
        return False
    elif money_received >= MENU[drink]['cost']:
        change = round(money_received - MENU[drink]['cost'], 2)
        print(f"Here is ${change} in change.")
        profit += MENU[drink]['cost']
        return True
    
def make_coffee(drink_name, order_ingrendient):
    for item in order_ingrendient:
        resources[item] -= order_ingrendient[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")
    

while True:
    choice = input("​What would you like? (espresso/latte/cappuccino):")

    if choice == 'off':
        break
    if choice == 'report':
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {profit}")
    else:
        drink = MENU[choice]
        if check_resources(drink['ingredients']):
            payment = process_coins()
            if transaction_successful(payment, choice):
                make_coffee(choice, drink['ingredients'])   