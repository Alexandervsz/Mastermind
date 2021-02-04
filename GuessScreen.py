import getpass
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
            code = getpass.getpass("Voer je code in: ")

    def generate_code(self):
        return "AAAA"
