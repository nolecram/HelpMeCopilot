import random

class FruitMarket:
    def __init__(self):
        self.fruits = {"apples": 5, "bananas": 3, "pears": 4}
        self.inventory = {"apples": 0, "bananas": 0, "pears": 0}
        self.money = 100

    def update_prices(self):
        for fruit in self.fruits:
            self.fruits[fruit] = random.randint(1, 10)

    def buy(self, fruit, quantity):
        cost = self.fruits[fruit] * quantity
        if cost > self.money:
            print("You don't have enough money!")
        else:
            self.inventory[fruit] += quantity
            self.money -= cost

    def sell(self, fruit, quantity):
        if self.inventory[fruit] < quantity:
            print("You don't have enough " + fruit + "!")
        else:
            self.inventory[fruit] -= quantity
            self.money += self.fruits[fruit] * quantity

    def print_status(self):
        print("Money: ", self.money)
        print("Prices: ", self.fruits)
        print("Inventory: ", self.inventory)

game = FruitMarket()

while True:
    game.update_prices()
    game.print_status()
    action = input("Do you want to buy or sell? ")
    fruit = input("Which fruit (apples, bananas, pears)? ").lower()
    quantity = int(input("How many? "))
    if action == "buy":
        game.buy(fruit, quantity)
    elif action == "sell":
        game.sell(fruit, quantity)

    # Change the price by up to 2, either up or down
    for fruit in game.fruits:
        change = random.randint(-2, 2)
        new_price = game.fruits[fruit] + change
        # Make sure the price is at least 1
        game.fruits[fruit] = max(new_price, 1)

        # 10% chance for a special event
        if random.random() < 0.1:
            # Choose a random fruit
            fruit = random.choice(list(game.fruits.keys()))
            # 50% chance for a boom (price doubles) or bust (price halves)
            if random.random() < 0.5:
                game.fruits[fruit] *= 2
                print(f"Fruit boom! {fruit.capitalize()} prices have doubled.")
            else:
                game.fruits[fruit] //= 2
                print(f"Fruit bust! {fruit.capitalize()} prices have halved.")
