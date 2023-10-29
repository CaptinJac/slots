# Slot machine lets go
import random
import json

items = ["🍒", "🍋", "🍊", "💎", "🎰"]

def load_player():
    with open('player.json', "r+") as f:
        player_data = json.load(f)
        if player_data['name'] == "":
            name_input = str(input("What is your name: "))
            player_data['name'] = name_input
            player_data['bank'] = 25
            f.seek(0)
            json.dump(player_data, f, indent = 4)
            f.truncate()
            print("Welcome %s, You currently have 25 credits!")
            return player_data['name'], player_data['bank']
        else:
            print("Welcome back %s!\nYou currently have %s credits!"%(player_data['name'], player_data['bank']))
            return player_data['name'], player_data['bank']
        
def update_player(amount):
    with open('player.json', 'r+') as f:
        player_data = json.load(f)
        player_data['bank'] = amount + player_data['bank']
        f.seek(0)
        json.dump(player_data, f, indent = 4)
        f.truncate()
        return player_data['bank']

player = load_player()


def wheel_spin(items):
   random_item = random.randint(0, len(items) - 1)
   return items[random_item]

def spin():
    wheel_one = None
    wheel_two = None
    wheel_three = None

    wheel_one = wheel_spin(items)
    wheel_two = wheel_spin(items)
    wheel_three = wheel_spin(items)

    print("---"+wheel_one+wheel_two+wheel_three+"---")

def play(items, player):
    while True:
        print("Welcome to Capt'n Jac's Casino!\nIn order to win at slots you have to match the following symbols in a row:\n🍒🍒🍒 pays 25 credits!\n🍋🍋🍋 pays 30 credits!\n🍊🍊🍊 pays 50 credits!\n💎💎💎 pays 75 credits!\n🎰🎰🎰 pays 500 credits!\n\n\n")
        player_bank = update_player(player[1])
        while player_bank != 0:
            try:
                spins = int(input("How many spins would you like to purchase (Each spin costs 1 credit): "))
                player = update_player(-spins)
                for x in range(spins):
                    spin()
                    print("\n\n\n")
            except ValueError:
                print("I am sorry that is not a valid value! Please try again!")

        break
play(items, player)