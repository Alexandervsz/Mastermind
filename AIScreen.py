from CodeGenerator import CodeGenerator


class AIScreen:
    def start_game(self, code=None, counter=1, feedback=None, algoritme=None):
        if code is None:
            code = CodeGenerator().get_user_code("Voer je code in: ", False)
        if algoritme is None:
            algoritme = input("Welk gok-algoritme wil je gebruiken?")  # unimplemented.
            algoritme = "test"
        if algoritme:
            guess = self.guess_standard(feedback)
            print(f"Ronde {counter}.")
            print(f"Computer gokt: {guess}")
        if code == guess:
            print(f"CPU wint in {counter} beurten!")
        elif counter < 6:
            input("Druk op enter om verder te gaan.")
            feedback = CodeGenerator().generate_feedback(code, guess)
            self.start_game(code, counter + 1, feedback, algoritme)
        else:
            print("Speler wint!")

    def guess_standard(self, feedback=None):
        return "AAAA"
