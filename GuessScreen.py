from getpass import getpass
from random import choice


class GuessScreen:
    def __init__(self):
        while True:
            self.opponent = input("Wil je spelen tegen een CPU of tegen een andere speler: ").lower()
            if self.opponent == "cpu" or self.opponent == "speler":
                break

    def start_game(self):
        if self.opponent == "cpu":
            code = self.generate_code()
        if self.opponent == "speler":
            code = getpass("Voer je code in: ").upper()
            print(code)

    def generate_code(self):
        options = ["A", "B", "C", "D", "E", "F"]
        code = ""
        for i in range(0, 4):
            code += choice(options)
        return code
