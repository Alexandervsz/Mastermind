from getpass import getpass
from itertools import product
from random import choice


class CodeGenerator:
    def __init__(self):
        self.options = ["A", "B", "C", "D", "E", "F"]

    def get_user_code(self, message, invisible):
        """Asks the user for a code with message, if invisible the code is hidden from view (for multiplayer games)
        If using pycharm dont forget to turn on emulate terminal in output console or the message won't show up"""

        while True:
            valid = True
            if invisible:
                code = getpass(message).upper()
            else:
                code = input(message).upper()
            for letter in code:
                if letter not in self.options:
                    valid = False
            if valid and len(code) == 4:
                return code
            else:
                print("Ongelidige code!")

    def generate_random_code(self):
        """ Generates a random, valid, code"""
        code = ""
        for i in range(0, 4):
            code += choice(self.options)
        return code

    def generate_feedback(self, code, guess):
        """ returns feedback for the provided code + guess"""
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
        used_letters = ""
        for letter in new_guess:
            if letter in new_code and letter not in used_letters:
                used_letters += letter
                semi_hits += 1
        return [full_hits, semi_hits]

    def get_random_letter(self):
        """ Returns a random color/letter"""
        return choice(self.options)

    def generate_all_options(self):
        """ Generates all possible combinations."""
        return product(self.options, repeat=4)
