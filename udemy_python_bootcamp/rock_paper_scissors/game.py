from random import randint

class RockPaperScissors:
    def __init__(self) -> None:
        self.winning_combos = {
            "rock": "scissors",
            "scissors": "paper",
            "paper": "rock",
        }
        self.your_score = 0
        self.opponent_score = 0
        self.playing = True

    def get_choice(self):
        choice = randint(1,3)
        if choice == 1:
            return "rock"
        elif choice == 2:
            return "scissors"
        elif choice == 3:
            return "paper"

    def game(self, input: str):
        your_choice = input
        opponent_choice = self.get_choice()
        if your_choice == "exit":
            self.playing = False
        elif your_choice == opponent_choice:
            print(f"\nYou both chose {your_choice}")
        elif self.winning_combos[your_choice] == opponent_choice:
            self.your_score += 1
            print(f"\nYour opponent chose {opponent_choice}. You are WINNING!")
        else:
            self.opponent_score += 1
            print(f"\nYour opponent chose {opponent_choice}. You are a LOOOOOOSER!")

    def print_scores(self):
        print(f"\nThe current score. You: {self.your_score}, machine: {self.opponent_score}")
