RULES = {
            "R": "S",
            "S": "P",
            "P": "R",
}


def find_winning_choice(choice_p1: str, choice_p2: str) -> str:
    if choice_p1 == choice_p2:
        return ""
    elif RULES[choice_p1] == choice_p2:
        return choice_p1
    elif RULES[choice_p2] == choice_p1:
        return choice_p2


if __name__ == "__main__":
    
    scores = {"player_1": 0, "player_2": 0}

    player_1 = "PSPRSPR"
    player_2 = "SRPRRSP"

    for c1, c2 in zip(player_1, player_2):

        choices = {"player_1": c1, "player_2": c2}
        winning_choice = find_winning_choice(c1, c2)

        if winning_choice != "":
            winner = list(choices.keys())[list(choices.values()).index(winning_choice)]
            scores[f"{winner}"] +=1

    winner = max(scores, key=scores.get)        
    print(f"Winner: {winner}. Score: {scores[winner]}")
