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
            print("mogelijke algortimes: Simple, OneStep")
            while True:
                algoritme = input("Welk gok-algoritme wil je gebruiken?").upper()  # unimplemented.
                if algoritme == "SIMPLE" or algoritme == "ONESTEP":
                    break
                else:
                    print("foutieve input!")
        if algoritme == "SIMPLE":
            guess = self.guess_standard(previous_guess, feedback)
        if algoritme == "ONESTEP":
            guess = self.guess_oneStep(previous_guess, feedback)
        print(f"Ronde {counter}.")
        print(f"Computer gokt: {guess}")
        if code == guess:
            print(f"CPU wint in {counter} beurten!")
        elif counter < 6:

            feedback = CodeGenerator().generate_feedback(code, guess)
            print(f"{feedback[0]} full hits, {feedback[1]} semi hits")
            input("Druk op enter om verder te gaan.")
            self.start_game(code, counter + 1, feedback, algoritme, guess)
        else:
            print("Speler wint!")

    def guess_standard(self, prev_guess, feedback=None):
        """ Starts up AI"""
        if feedback is None:
            return "AABC"
        else:
            code = self.a_simple_strategy(feedback, prev_guess)
            return code

    def guess_oneStep(self, prev_guess, feedback=None):
        if feedback is None:
            return "AABC"
        else:
            print(self.combinations)
            if len(self.combinations) == 1:
                return self.combinations[0]
            posiblity_list = []
            for combination in self.combinations:
                possibilities = len(self.generate_temp_combinations(feedback, combination))
                if possibilities != 0:
                    posiblity_list.append([combination, possibilities ])
            print(posiblity_list)
            smallest = None
            for posiblity in posiblity_list:
                if smallest is None:
                    smallest = posiblity[1]
                elif posiblity[1] < smallest:
                    smallest = posiblity[1]
            guess= None
            for posiblity in posiblity_list:
                if posiblity[1] == smallest:
                    temp_combinations = self.generate_temp_combinations(feedback, prev_guess)
                    self.combinations = temp_combinations
                    guess = posiblity[0]
                    break
            if guess is not None:
                return guess
            else:
                return self.combinations[0]

    def completely_random_guess(self):
        """ Returns a random guess"""
        return CodeGenerator().generate_random_code()

    def a_simple_strategy(self, feedback, prev_guess):
        """ A simple strategy algorithm, from article."""

        temp_combinations = self.generate_temp_combinations(feedback, prev_guess)
        self.combinations = temp_combinations
        return self.combinations[0]

    def generate_temp_combinations(self, feedback, prev_guess):
        temp_combinations = []
        for combination in self.combinations:
            hits = CodeGenerator().generate_feedback(combination, prev_guess)
            if [hits[0], hits[1]] == feedback:
                temp_combinations.append(combination)
        return temp_combinations
