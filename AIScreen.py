from CodeGenerator import CodeGenerator


class AIScreen:
    def __init__(self):
        self.guess_list = []
        self.combinations = CodeGenerator().generate_all_options()

    def start_game(self, code=None, counter=1, feedback=None, algoritme=None, previous_guess=None):
        """Starts the game, or the next round."""
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
        """ Starts up AI"""
        if feedback is None:
            return "ABCC"
        else:
            code_old = self.a_simple_strategy(feedback, prev_guess)
            code_format = ""
            for letter in code_old:
                code_format += letter
            return code_format

    def completely_random_guess(self):
        """ Returns a radom guess"""
        return CodeGenerator().generate_random_code()

    def a_simple_strategy(self, feedback, prev_guess):
        """ A simple strategy algorithm, from article."""
        for combination in self.combinations:
            full_hits = 0
            semi_hits = 0
            new_code = ""
            new_guess = ""
            for x in range(0, 4):
                if prev_guess[x] == combination[x]:
                    full_hits += 1
                else:
                    new_code += prev_guess[x]
                    new_guess += combination[x]
            for letter in new_guess:
                if letter in new_code:
                    semi_hits += 1
            if [full_hits, semi_hits] == feedback:
                return combination
