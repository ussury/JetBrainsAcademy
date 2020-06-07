class CoffeeMachine:
    def __init__(self):
        self.resources = {'water': 400, 'milk': 540, 'coffee': 120, 'cups': 9, 'money': 550}

    def printer(self, coll):
        print('The coffee machine has:')
        for item in coll:
            if item == 'water':
                print(f'{self.resources[item]} of water')
            if item == 'milk':
                print(f'{self.resources[item]} of milk')
            if item == 'coffee':
                print(f'{self.resources[item]} of coffee beans')
            if item == 'cups':
                print(f'{self.resources[item]} of disposable cups')
            if item == 'money':
                print(f'${self.resources[item]} of money')
        print()

    def fill(self):
        add_water = input('Write how many ml of water do you want to add: ')
        self.resources['water'] += int(add_water)

        add_milk = input('Write how many ml of milk do you want to add: ')
        self.resources['milk'] += int(add_milk)

        add_coffee = int(
            input('Write how many grams of coffee beans do you want to add: '))
        self.resources['coffee'] += add_coffee

        add_cups = int(
            input('Write how many disposable cups of coffee do you want to add: '))
        self.resources['cups'] += add_cups

    def buy(self):
        def get_resources(water, coffee, cups, money, milk=0):
            def new_resources(list):
                list['water'] -= water
                list['coffee'] -= coffee
                list['cups'] -= 1
                list['milk'] -= milk
                list['money'] += money
                return list

            coll = {'water':  water,
                    'coffee': coffee,
                    'cups':   cups,
                    'money':  money,
                    'milk':   milk}

            for k, v in coll.items():
                if self.resources[k] - v < 0:
                    print('Sorry, not enough water!')
                    print()
                    return
                else:
                    print('I have enough resources, making you a coffee!')
                    print()
                    return new_resources(self.resources) 

        choice = input(
            'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')

        cups = self.resources['cups']
        if choice == '1':  # espresso water = 250, coffee = 16, money = 4
            espr_water = 250
            espr_coffee = 16
            espr_money = 4
            get_resources(espr_water, espr_coffee, cups, espr_money)

        if choice == '2':  # latte water = 350, milk = 75, coffee = 20, money = 7
            latte_water = 350
            latte_milk = 75
            latte_coffee = 20
            latte_money = 7
            get_resources(latte_water, latte_coffee, cups, latte_money, latte_milk)

        if choice == '3':  # cappuccino water = 200, milk = 100, coffee = 12, money = 6
            capp_water = 200
            capp_milk = 100
            capp_coffee = 12
            capp_money = 6
            get_resources(capp_water, capp_coffee, cups, capp_money, capp_milk)

    def fill(self):
        add_water = input('Write how many ml of water do you want to add: ')
        self.resources['water'] += int(add_water)

        add_milk = input('Write how many ml of milk do you want to add: ')
        self.resources['milk'] += int(add_milk)

        add_coffee = int(
            input('Write how many grams of coffee beans do you want to add: '))
        self.resources['coffee'] += add_coffee

        add_cups = int(
            input('Write how many disposable cups of coffee do you want to add: '))
        self.resources['cups'] += add_cups

    def take(self):
        print(f"I gave yuo ${self.resources['money']}")
        self.resources['money'] = 0

    def remaining(self):
        CoffeeMachine.printer(self, self.resources)

coffee_machine = CoffeeMachine()

while True:
    param = input('Write action (buy, fill, take, remaining, exit): ')
    if param == 'buy':
        print()
        coffee_machine.buy()
        print()

    if param == 'fill':
        print()
        coffee_machine.fill()
        print()

    if param == 'take':
        print()
        coffee_machine.take()
        print()

    if param == 'remaining':
        print()
        coffee_machine.remaining()

    if param == 'exit':
        break