import re
from math import floor

data_path = "AoC\\2023\\04_1_test.txt"
data_path = "AoC\\2023\\04_input.txt"
input = [line.strip() for line in open(data_path, 'r')]


# pt I
def get_numbers(row: list) -> tuple[list, list]:
    split_row = re.split(r"[\|:]", row)
    winning_numbers = re.findall(r"\d+", split_row[1])
    elf_numbers = re.findall(r"\d+", split_row[2])
    return winning_numbers, elf_numbers


def count_winning_numbers(row: list) -> int:
    no_of_winning_numbers = 0
    winning_n, elf_n = get_numbers(row)

    for number in elf_n:
        if number in winning_n:
            no_of_winning_numbers += 1
    
    return no_of_winning_numbers


def get_result_ptI(input: list) -> int:
    score = 0
    for row in input:
        card_score = 0
        no_of_winning_numbers = count_winning_numbers(row)

        if no_of_winning_numbers > 0:
            # Geometric progress: 1, 2, 4, 8, 16, 32, 64 etc.
            # 2**0=1, 2**1=2, 2**2=4, 2**3=8 etc.
            card_score = 2**(no_of_winning_numbers-1)
            score += card_score
    return score


# pt2
# Scratchcards only cause you to win more scratchcards equal to the number of winning numbers you have.
# you win equivalent number of cards, copies of the cards below

def get_result_ptII(input: list) -> int:
    card_winning_no_dict = {}
    card_count = {}

    for current_row in range(0, len(input)):
        no_of_winning_numbers = count_winning_numbers(input[current_row])
        card_winning_no_dict[current_row] = no_of_winning_numbers
        card_count[current_row] = 1

    # print("DICT: ", card_winning_no_dict)
    # print("card_count:",card_count)

    for card, count in card_count.items():
        # print("CARD NO:", card)
        
        no_of_new_cards = card_winning_no_dict[card]
        # print("NO OF NEW CARDS WON:", no_of_new_cards)

        # update card count for original + copies
        for n in range(0, count):
            for next_card in range(card+1, card+no_of_new_cards+1):
                # print("UPDATE CARD:", next_card)
                if next_card in card_count.keys():
                    card_count[next_card] += 1 

        # print("NEW CARD_COUNT:",card_count)
        # print("-----") 

    return sum(card_count.values())


if __name__ == "__main__":
    result_ptI = get_result_ptI(input)
    print(result_ptI)
    
    result_ptII = get_result_ptII(input)
    print(result_ptII)

    # for dev:
    test_result_ptI = 13
    print(result_ptI == test_result_ptI)

    test_result_ptII = 30
    print(result_ptII == test_result_ptII)