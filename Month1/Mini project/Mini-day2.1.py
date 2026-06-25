# 1

class Game():
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def show_details(self):
        print (f"Game: {self.name}")
        print (f"Price: {self.price}")

class Cart():
    def add_game(self, game):
        print (f"Added to cart{game.name}")

fifa = Game("FIFA",2999)

fifa.show_details()

cart_object = Cart()
cart_object.add_game(fifa)

