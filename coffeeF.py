class CoffeeMachine:
    def __init__(self, water, milk, beans, cups, money):
        self.water = int(water)
        self.milk  = int(milk)
        self.beans = int(beans)
        self.cups  = int(cups)
        self.money = int(money)

    def __str__(self):
        return f'''The coffee machine has:
        {self.water} ml of water
        {self.milk} ml of milk
        {self.beans} g of coffee beans
        {self.cups} disposible cups
        ${self.money} of money'''

    def buy(self, type):
        self.type = type
        if type == "1":
            if self.water >= 250 and self.beans >= 16 and self.cups >= 1:
                self.water -= 250
                self.beans -= 16
                self.cups  -= 1
                self.money += 4
                print("I have enough resources, making you a coffee!")
            else:
                if self.water < 250:
                    print("Sorry, not enough water!")
                if self.beans  < 16:
                    print("Sorry, not enough beans!")
                if self.cups < 1:
                    print("Sorry, not enough cups!")
        if type == "2":
            if self.water >= 350 and self.milk >= 75 and self.beans >= 20 and self.cups >= 1:
                self.water -= 350
                self.milk  -= 75
                self.beans -= 20
                self.cups  -= 1
                self.money += 7
                print("I have enough resources, making you a coffee!")
            else:
                if self.water < 350:
                    print("Sorry, not enough water!")
                if self.milk < 75:
                    print("Sorry, not enough milk!")
                if self.beans  < 20:
                    print("Sorry, not enough beans!")
                if self.cups < 1:
                    print("Sorry, not enough cups!")
        if type == "3":
            if self.water >= 200 and self.milk >= 100 and self.beans >= 12 and self.cups >= 1:
                self.water -= 200
                self.milk  -= 100
                self.beans -= 12
                self.cups  -= 1
                self.money += 6
                print("I have enough resources, making you a coffee!")
            else:
                if self.water < 200:
                    print("Sorry, not enough water!")
                if self.milk < 100:
                    print("Sorry, not enough milk!")
                if self.beans  < 12:
                    print("Sorry, not enough beans!")
                if self.cups < 1:
                    print("Sorry, not enough cups!")
        if type == "back":
            pass
    
    def fill(self):
        self.water += int(input('Write how many ml of water you want to add: '))
        self.milk  += int(input('Write how many ml of milk you want to add: '))
        self.beans += int(input('Write how many grams of coffee beans you want to add: '))
        self.cups  += int(input('Write how many disposable cups you want to add: '))

    def take(self):
        print(f"I gave you ${self.money}")
        self.money -= self.money

coffee = CoffeeMachine(400, 540, 120, 9, 550)
start = True
while start:
    action = input("Write action (buy, fill, take, remaining, exit):")
    if action == "buy":
        type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        coffee.buy(type)
    elif action == "fill":
        coffee.fill()
    elif action == "take":
        coffee.take()
    elif action == "remaining":
        print(coffee)
    elif action == "exit":
        start = False
