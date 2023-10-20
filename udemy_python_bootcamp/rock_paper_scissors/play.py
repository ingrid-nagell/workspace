from game import RockPaperScissors
from time import sleep

if __name__ == "__main__":
    rps = RockPaperScissors()
    print("\nLet's play RockPaperScissors! It's you against the Machine!")
    while rps.playing==True:
        rps.print_scores()
        sleep(3)
        user_input = input("\nYour guess (must match either rock/paper/scissors, type exit to end the game):\n")
        rps.game(user_input)
    rps.print_scores()