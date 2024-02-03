# WAP a program in which the class is using @dataclass decorator. Come up with
# your own idea of a data class.
# [Name of the file should be dataclass.py](1point)

from dataclasses import dataclass

@dataclass
class Game:
    game_type: str
    price: float
    name: str

def main():
    games = [
        Game("board game", 29.99, "tsuro"),
        Game("Computer Game", 59.99, "Elden Ring"),
        Game("Phone game", 0.00, "Clash of Clans")
    ]

    mostExpensive = max(games, key = lambda p: p.price)
    print("The most expensive game: ", mostExpensive.name)

if __name__ == '__main__':
    main()
