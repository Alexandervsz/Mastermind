from CodeGenerator import CodeGenerator


class AIScreen:
    def __init__(self):
        self.guess_list = []
        combinations = CodeGenerator().generate_all_options()
        self.combinations = []
        for combination in combinations:
            combination_letters = ""
            for letter in combination:
                combination_letters += letter
            self.combinations.append(combination_letters)

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
            code = self.a_simple_strategy(feedback, prev_guess)
            return code

    def completely_random_guess(self):
        """ Returns a radom guess"""
        return CodeGenerator().generate_random_code()

    def a_simple_strategy(self, feedback, prev_guess):
        """ A simple strategy algorithm, from article."""
        temp_combinations = []
        for combination in self.combinations:
            hits = CodeGenerator().generate_feedback(combination, prev_guess)
            if [hits[0], hits[1]] == feedback:
                temp_combinations.append(combination)
        self.combinations = temp_combinations
        return self.combinations[0]


