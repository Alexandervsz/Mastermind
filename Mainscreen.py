from AIScreen import AIScreen
from GuessScreen import GuessScreen


def open_beginscreen():
    """ Opens the beginsceen."""
    while True:
        try:
            mode = int(input("Wil je de gene zijn die raadt (1) of de code bedenkt (2): "))
            if 0 <= mode < 3:
                break
            else:
                print("Foutieve invoer!")
        except ValueError:
            print("Foutieve invoer!")
    if mode == 1:
        GuessScreen().start_game()
        open_beginscreen()

    if mode == 2:
        AIScreen().start_game()
        open_beginscreen()

    if mode == 0:
        return


open_beginscreen()
