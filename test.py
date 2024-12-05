import random

# Initialize game variables
gold = 20
inventory = {"apple": 0, "banana": 0, "orange": 0}
days = 20

# Function to display inventory and gold
def display_status(day, gold, inventory):
    print(f"Day {day}")
    print(f"Gold: {gold}")
    print("Inventory:")
    for fruit, quantity in inventory.items():
        print(f"  {fruit}: {quantity}")
    print()

# Function to buy fruit
def buy_fruit(gold, inventory):
    fruit = input("Enter the fruit to buy (apple, banana, orange): ").lower()
    if fruit not in inventory:
        print("Invalid fruit.")
        return gold, inventory
    price = random.randint(1, 5)
    quantity = int(input(f"Enter the quantity to buy (price per unit: {price}): "))
    cost = price * quantity
    if cost > gold:
        print("Not enough gold.")
        return gold, inventory
    gold -= cost
    inventory[fruit] += quantity
    return gold, inventory

# Function to sell fruit
def sell_fruit(gold, inventory):
    fruit = input("Enter the fruit to sell (apple, banana, orange): ").lower()
    if fruit not in inventory:
        print("Invalid fruit.")
        return gold, inventory
    quantity = int(input("Enter the quantity to sell: "))
    if quantity > inventory[fruit]:
        print("Not enough fruit in inventory.")
        return gold, inventory
    price = random.randint(1, 5)
    gold += price * quantity
    inventory[fruit] -= quantity
    return gold, inventory

# Function to handle special events
def special_event(gold, inventory):
    event = random.choice(["none", "find_gold", "fruit_spoil", "bonus_fruit"])
    if event == "find_gold":
        found_gold = random.randint(5, 15)
        gold += found_gold
        print(f"Special Event: You found {found_gold} gold!")
    elif event == "fruit_spoil":
        fruit = random.choice(list(inventory.keys()))
        if inventory[fruit] > 0:
            spoiled_quantity = random.randint(1, inventory[fruit])
            inventory[fruit] -= spoiled_quantity
            print(f"Special Event: {spoiled_quantity} {fruit}(s) spoiled!")
    elif event == "bonus_fruit":
        fruit = random.choice(list(inventory.keys()))
        bonus_quantity = random.randint(1, 5)
        inventory[fruit] += bonus_quantity
        print(f"Special Event: You received {bonus_quantity} bonus {fruit}(s)!")
    return gold, inventory

# Main game loop
for day in range(1, days + 1):
    display_status(day, gold, inventory)
    gold, inventory = special_event(gold, inventory)
    action = input("Do you want to buy or sell fruit? (buy/sell): ").lower()
    if action == "buy":
        gold, inventory = buy_fruit(gold, inventory)
    elif action == "sell":
        gold, inventory = sell_fruit(gold, inventory)
    else:
        print("Invalid action.")
    display_status(day, gold, inventory)

# Final status
print("Game over!")
display_status("Final", gold, inventory)