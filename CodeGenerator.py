from getpass import getpass
from itertools import product
from random import choice


class CodeGenerator:
    def __init__(self):
        self.options = ["A", "B", "C", "D", "E", "F"]

    def get_user_code(self, bericht, invisible):
        """ Vraag de user om een code met doorgegeven bericht, als invisible dan kan de code niet door de
        volgende speler worden gelezen (zet met pycharm emulate terminal in output console aan, als je deze gebruikt anders zie je niets)"""
        while True:
            valid = True
            if invisible:
                code = getpass(bericht).upper()
            else:
                code = input(bericht).upper()
            for letter in code:
                if letter not in self.options or len(code) != 4:
                    valid = False
            if valid:
                return code
            else:
                print("Ongelidige code!")

    def generate_random_code(self):
        """ Genereert een random, geldige, code"""
        code = ""
        for i in range(0, 4):
            code += choice(self.options)
        return code

    def generate_feedback(self, code, guess):
        """ Genereert feedback voor de ingegeven code + gok"""
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

    def get_random_letter(self):
        """Returnt een random kleur"""
        return choice(self.options)

    def generate_all_options(self):
        """ Genereert alle mogelijke opties."""
        return product(self.options, repeat=4)


