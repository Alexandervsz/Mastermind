import random

from CodeGenerator import CodeGenerator


class AIScreen:
    def __init__(self):
        self.guess_list = []
        combinations = CodeGenerator().generate_all_options()
        self.combinations = []
        self.prev_guesses = []
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
            algoritmes = ["SIMPLE", "ONESTEP", "EXPSIZE", "DIFFERENT"]
            letters = ["S", "O", "E", "D"]
            print("Mogelijke algortimes:")
            for algoritme in algoritmes:
                print(algoritme.capitalize())
            while True:
                algoritme = input("Welk gok-algoritme wil je gebruiken: ").upper()

                if algoritme in algoritmes or algoritme in letters:
                    break
                else:
                    print("foutieve input!")
        if algoritme == "SIMPLE" or algoritme == "S":
            guess = self.guess_standard(previous_guess, feedback)
        if algoritme == "ONESTEP" or algoritme == "O":
            guess = self.guess_oneStep(previous_guess, feedback)
        if algoritme == "EXPSIZE" or algoritme == "E":
            guess = self.guess_expsize(previous_guess, feedback)
        if algoritme == "DIFFERENT" or algoritme == "D":
            guess = self.a_different_strategy(feedback, previous_guess)
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
            return "AABB"
        else:
            codedict = {}
            for combination in self.combinations:
                options = len(self.generate_temp_combinations(feedback, combination))

                if options != 0:
                        codedict[combination] = options

            try:
                min(codedict, key=codedict.get)
            except ValueError:
                return self.combinations[0]
            if min(codedict, key=codedict.get) != prev_guess:
                self.a_simple_strategy(feedback, prev_guess)
                return min(codedict, key=codedict.get)
            else:
                self.combinations.pop(0)
                return self.combinations[0]

    def a_simple_strategy(self, feedback, prev_guess):
        """ A simple strategy algorithm, from article YET ANOTHER MASTERMIND STRATEGY by Barteld Kooi."""

        temp_combinations = self.generate_temp_combinations(feedback, prev_guess)
        self.combinations = temp_combinations
        return self.combinations[0]

    def guess_expsize(self, prev_guess, feedback=None):
        if feedback is None:
            return "AABC"
        combdict = {}
        feedbacklist = [[0,0], [0,1] ,[0,2], [0,3], [0,4], [1,0], [1,1], [1,2], [1,3],[2,0],[2,1],[2,2],[3,0],[4,0]]
        for combination in self.combinations:
            for newfeedback in feedbacklist:
                if len(self.generate_temp_combinations(newfeedback, combination)) != 0:
                    try:
                        combdict[combination].append([newfeedback, len(self.generate_temp_combinations(newfeedback,combination))])
                    except KeyError:
                        combdict[combination] = [newfeedback, len(self.generate_temp_combinations(newfeedback,combination))]
        highestdict = {}
        for combination in combdict:
            highest = 0
            if combdict[combination][1] > highest:
                highest = combdict[combination][1]
            highestdict[combination] = highest
        for value in highestdict:
            highestdict[value] = int(highestdict[value]) * int(highestdict[value]) / len(self.combinations)
        best = min(highestdict, key=highestdict.get)
        self.a_simple_strategy(feedback, prev_guess)
        return best

    def generate_temp_combinations(self, feedback, guess):
        """ This function checks whether the guess is valid according to the feedback."""
        temp_combinations = []
        for combination in self.combinations:

            if CodeGenerator().generate_feedback(combination, guess) == feedback:
                temp_combinations.append(combination)
        return temp_combinations

    def a_different_strategy(self, feedback, prev_guess):
        """ A different strategy, looks at whichever combination scores the highest
        then uses that combination as a guess. If no combination can be found, a
        random guess is used."""
        if feedback is None:
            return "AABC"
        combination_list = self.generate_temp_combinations(feedback, prev_guess)
        highest = 0
        combination_list2 = []
        for combination in combination_list:
            if combination not in self.prev_guesses:
                combination_list2.append(combination)
        for combination in combination_list2:
            feedback = CodeGenerator().generate_feedback(combination, prev_guess)
            feedback = float(f"{feedback[0]}.{feedback[1]}")
            if feedback > highest and combination:
                highest = feedback
        if highest == 0:
            while True:
                choice = random.choice(self.combinations)
                if choice not in self.prev_guesses:
                    break
            self.prev_guesses.append(choice)
            self.combinations.pop(self.combinations.index(choice))
            return choice
        for combination in combination_list2:
            feedback = CodeGenerator().generate_feedback(combination, prev_guess)
            feedback = float(f"{feedback[0]}.{feedback[1]}")
            if feedback == highest:
                self.prev_guesses.append(combination)
                return combination
