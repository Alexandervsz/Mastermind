from getpass import getpass
from random import choice


class CodeGenerator:
    def __init__(self):
        self.options = ["A", "B", "C", "D", "E", "F"]

    def get_user_code(self, invisible):
        while True:
            valid = True
            if invisible:
                code = getpass("Voer je code in: ").upper()
            else:
                code = input("Voer je gok in: ").upper()
            for letter in code:
                if letter not in self.options or len(code) != 4:
                    valid = False
            if valid:
                return code
            else:
                print("Ongelidige code!")

    def generate_random_code(self):

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