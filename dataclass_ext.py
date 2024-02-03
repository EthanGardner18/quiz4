# Extend the above program (program-4) to include an extra function inside of the
# @dataclass class.
# Example:
# @dataclass
# class xyz:
# name: str
# price: float
# quantity: int = 0
# def write_your_own_function(self) -> Return_type:
# #your function code here
# So there will be an extra function. Implement the function to something meaningful.
# [Name of the file should be dataclass_ext.py](1point)

from dataclasses import dataclass

@dataclass
class Game:
    game_type: str
    price: float
    name: str

    def reducePrice(self, percentOff)->float:
        discount = (percentOff/100) * self.price
        newPrice = self.price - discount
        self.price = newPrice



def main():
    games = [
        Game("board game", 29.99, "tsuro"),
        Game("Computer Game", 59.99, "Elden Ring"),
        Game("Phone game", 0.00, "Clash of Clans")
    ]

    mostExpensive = max(games, key = lambda p: p.price)
    print("The most expensive game: ", mostExpensive.name)

    discountGame = mostExpensive.reducePrice(10)
    print("After the sale the game is now: ",mostExpensive.price)

if __name__ == '__main__':
    main()