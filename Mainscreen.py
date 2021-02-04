from GuessScreen import GuessScreen
from AIScreen import AIScreen
mode = int(input("Wil je de gene zijn die raadt (1) of de code bedenkt (2): "))
if mode == 1:
    GuessScreen().start_game()

if mode == 2:
    AIScreen()
