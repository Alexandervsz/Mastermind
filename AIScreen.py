from CodeGenerator import CodeGenerator


class AIScreen:
    def start_game(self, code=None, counter=1, feedback=None, algoritme=None, previous_guess=None):
        if code is None:
            code = CodeGenerator().get_user_code("Voer je code in: ", False)
        if algoritme is None:
            algoritme = input("Welk gok-algoritme wil je gebruiken?")  # unimplemented.
            algoritme = "test"
        if algoritme:
            guess = self.guess_standard(previous_guess, feedback)
            print(f"Ronde {counter}.")
            print(f"Computer gokt: {guess}")
        if code == guess:
            print(f"CPU wint in {counter} beurten!")
        elif counter < 6:
            input("Druk op enter om verder te gaan.")
            feedback = CodeGenerator().generate_feedback(code, guess)
            self.start_game(code, counter + 1, feedback, algoritme, guess)
        else:
            print("Speler wint!")

    def guess_standard(self, prev_guess, feedback=None):
        if feedback is None:
            return "ABCC"
        else:
            full_hits = feedback[0]
            semi_hits = feedback[1]
            new_guess = ""
            for letter in prev_guess:
                if full_hits != 0:
                    new_guess += letter
                    full_hits -= 1
                elif semi_hits != 0:
                    new_guess += letter
                    semi_hits -= 1
                else:
                    new_guess += CodeGenerator().get_random_letter()
            return new_guess
