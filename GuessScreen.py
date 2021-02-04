from getpass import getpass
from random import choice


class GuessScreen:
    def __init__(self):
        self.options = ["A", "B", "C", "D", "E", "F"]
        while True:
            self.opponent = input("Wil je spelen tegen een CPU of tegen een andere speler: ").lower()
            if self.opponent == "cpu" or self.opponent == "speler":
                break
            else:
                print("Foutieve invoer!")

    def start_game(self, code=None, counter=1):
        if code is None:
            if self.opponent == "cpu":
                code = self.generate_code()
            if self.opponent == "speler":
                while True:
                    valid = True
                    code = getpass("Voer je code in: ").upper()
                    for letter in code:
                        if letter not in self.options or len(code) != 4:
                            valid = False
                    if valid:
                        break
                    else:
                        print("Ongelidige code!")

        guess = input(f"Poging {counter}: ").upper()
        feedback = self.generate_feedback(code, guess)
        if guess == code:
            print(f"Je hebt gewonnen! het heeft je {counter} beurten gekost.")
        elif counter < 6:
            print(
                f"Je hebt {feedback[0]} op de juiste plaats en de juiste kleur, en {feedback[1]} "
                f"van de juiste kleur alleen.")
            self.start_game(code, counter + 1)

        else:
            print(f"Je hebt verloren! Het antwoord was: {code}.")

    def generate_code(self):

        code = ""
        for i in range(0, 4):
            code += choice(self.options)
        return code

    def generate_feedback(self, code, guess):
        full_hits = 0
        semi_hits = 0
        new_code = ""
        new_guess = ""
        for x in range(0, 4):
            if guess[x] == code[x]:
                full_hits += 1
            else:
                new_code += code[x]
                new_guess += guess[x]
        for letter in new_guess:
            if letter in new_code:
                semi_hits += 1
        return [full_hits, semi_hits]
