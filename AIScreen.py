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
            code = self.a_simple_strategy(feedback, prev_guess, "simple")
            return code

    def guess_oneStep(self, prev_guess, feedback=None):
        if feedback is None:
            return "AABC"
        else:
            print(self.combinations)
            comb_list = []
            feedback_list = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1],
                             [2, 2], [3, 0], [4, 0]]

            for feedback2 in feedback_list:
                for combination in self.combinations:
                    pass
                    #comb_dict[(combination,'feedback')] = feedback2
                    #comb_dict[(combination,'possibilities')] = self.a_simple_strategy_2(feedback2, combination)

                    comb_list.append([self.a_simple_strategy_2(feedback2, combination), feedback2, combination])
            smallest = None
            for combination in comb_list:
                print(combination[0])
                print(smallest)
                if smallest is None:
                    smallest = combination[0]
                elif combination[0] < smallest:
                    smallest = combination[0]
            code = ""
            for combination in comb_list:
                if combination[0] == smallest:
                    code = combination[3]
                    break
            return code


            print(comb_list)

    def completely_random_guess(self):
        """ Returns a random guess"""
        return CodeGenerator().generate_random_code()

    def a_simple_strategy(self, feedback, prev_guess, mode):
        """ A simple strategy algorithm, from article."""
        temp_combinations = []
        for combination in self.combinations:
            hits = CodeGenerator().generate_feedback(combination, prev_guess)
            if [hits[0], hits[1]] == feedback:
                temp_combinations.append(combination)


        self.combinations = temp_combinations
        return self.combinations[0]

    def a_simple_strategy_2(self, feedback, guess):
        temp_combinations = []
        for combination in self.combinations:
            hits = CodeGenerator().generate_feedback(combination, guess)
            if [hits[0] , hits[1]] == feedback:
                temp_combinations.append(combination)
        return  len(temp_combinations)

