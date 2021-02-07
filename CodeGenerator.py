from getpass import getpass
from random import choice


class CodeGenerator:
    def __init(self):
        self.options = ["A", "B", "C", "D", "E", "F"]

    def get_user_code(self):
        while True:
            valid = True
            code = getpass("Voer je code in: ").upper()
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
