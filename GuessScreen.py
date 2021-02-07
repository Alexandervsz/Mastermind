from CodeGenerator import CodeGenerator


class GuessScreen:

    def start_game(self, code=None, counter=1):
        if code is None:
            while True:
                opponent = input("Wil je spelen tegen een CPU of tegen een andere speler: ").lower()
                if opponent == "cpu" or opponent == "speler":
                    break
                else:
                    print("Foutieve invoer!")
            if opponent == "cpu":
                code = CodeGenerator().generate_random_code()
            if opponent == "speler":
                code = CodeGenerator().get_user_code("Voer je code in: ", True)
                """Zet in je build configurations emulate terminal in output console aan (pycharm)"""

        print(f"Poging {counter}.")
        guess = CodeGenerator().get_user_code("Voer je gok in: ", False)
        feedback = CodeGenerator().generate_feedback(code, guess)
        if guess == code:
            print(f"Je hebt gewonnen! Het heeft je {counter} beurten gekost.")
        elif counter < 6:
            print(
                f"Je hebt {feedback[0]} op de juiste plaats en de juiste kleur, en {feedback[1]} "
                f"van de juiste kleur alleen.")
            self.start_game(code, counter + 1)

        else:
            print(f"Je hebt verloren! Het antwoord was: {code}.")
