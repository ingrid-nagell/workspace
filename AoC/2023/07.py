import re

data_path = "AoC\\2023\\07_1_test.txt"
data_path = "AoC\\2023\\07_input.txt"
input = [line.strip().split() for line in open(data_path, 'r')]

# pt1
# CARD_RANK = {"2":1, "3":2, "4":3, "5":4, "6":5, "7":6, "8":7, "9":8, "T":9, "J":10, "Q":11, "K":12, "A":13}

# pt2
CARD_RANK = {"J":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "Q":11, "K":12, "A":13}

# pt1
def get_character_count(hand) -> dict:
    unique_characters = ''.join(set(hand))
    character_count = {}
    for l in unique_characters:
        counter = hand.count(l)
        character_count[l] = counter
    return character_count, hand

# pt2
def get_character_count_modified(hand) -> dict:
    unique_characters = ''.join(set(hand))
    character_count = {}

    if "J" in unique_characters and len(unique_characters) == 1:
        character_count = {"A": 5}

    else:
        for l in unique_characters:
            if l != "J":
                counter = hand.count(l)
                character_count[l] = counter
        # print(character_count)
    
        if "J" in unique_characters:
            j_count = hand.count("J")
            # print("Js: ", hand.count("J"))

            max_count =  max(character_count.values())
            # print("MAX: ", max_count)

            cards_with_max_count = []
            for k, v in character_count.items():
                if v == max_count:
                    cards_with_max_count.append(k)

            # print("CARDS WITH MAX COUNT: ", cards_with_max_count)
            count_sorted_by_rank = sorted(cards_with_max_count, key=lambda val: -CARD_RANK[val])
            # print("CARD WITH MAX COUNT SORTED BY RANK (DESC): ", count_sorted_by_rank)
            add_j_count_to_character = count_sorted_by_rank[0]
            character_count[add_j_count_to_character] = character_count[add_j_count_to_character] + j_count
        # print("ADJUSTED COUNT:", character_count)
        # new_hand = hand.replace("J", add_j_count_to_character)
    # else:
    #     new_hand = hand
        # print("NEW HAND: ", new_hand)
        # print("")
    return character_count


def get_type(input: list) -> list:
    five_of_a_kind=[]
    four_of_a_kind= []
    full_house = []
    three_of_a_kind=[]
    two_pairs=[]
    one_pair=[]
    high_card=[]
    
    for e in input:
        hand = e[0]
        bet = e[1]
        character_count = get_character_count_modified(hand)
        # print(character_count, hand, bet)
        # print(hand, character_count.values(), 3 in character_count.values())

        if 5 in character_count.values():
            five_of_a_kind.append([hand, bet])
            continue
        elif 4 in character_count.values():
            four_of_a_kind.append([hand, bet])
            continue
        elif set([3, 2]).issubset(character_count.values()):
            full_house.append([hand, bet])
            continue
        elif 3 in character_count.values():
            three_of_a_kind.append([hand, bet])
            continue
        elif list(character_count.values()).count(2) == 2:
            two_pairs.append([hand, bet])
            continue
        elif 2 in character_count.values():
            one_pair.append([hand, bet])
            continue
        else:
            high_card.append([hand, bet])
            continue
    
    # print("5 ", five_of_a_kind)
    # print("4 ", four_of_a_kind)
    # print("FH ", full_house)
    # print("3 ", three_of_a_kind)
    # print("2p ", two_pairs)
    # print("1p ", one_pair)
    # print("hc ",high_card)

    hands_as_types=[high_card, one_pair, two_pairs, three_of_a_kind, full_house, four_of_a_kind, five_of_a_kind]
    return hands_as_types


def sort_inp(input: list[list]):
    input_sorted = sorted(
        input, key=lambda val: (
            CARD_RANK[val[0][0]], CARD_RANK[val[0][1]], CARD_RANK[val[0][2]], CARD_RANK[val[0][3]], CARD_RANK[val[0][4]]
        )
    )
    return input_sorted


def get_result(input: list) -> int:
    # print(input)
    # print(input_sorted)
    # input_sorted = sort_inp(input)
    type_lists = get_type(input)
    # print(type_lists)
    rank = 1
    winnings = 0
    for li in type_lists:
        print(li)
        # print("ORIG: ", li)

        li_sorted = sort_inp(li)
        # print("SORTED:", li_sorted)
        # print(li)
        # list_sorted = sort_inp(li)
        # print(list_sorted)
        # print("----")
        # break
        for hand, bid in li_sorted:
            # print(hand, rank)
            winnings += int(bid)*rank
            # print(rank, winnings)
            # print(hand, bid)
            rank += 1
        print("--------")
    return winnings


if __name__ == "__main__":
    # result_ptI = get_result_ptI(input)
    # print(result_ptI)
    
    # print(get_character_count_modified("JJJJJ"))
    result_ptII = get_result(input)
    print(result_ptII)
    # 249459440 too high


    # for dev:
    # test_result_ptI = 6440
    # print("Correct result pt 1:", result_ptI == test_result_ptI)

    test_result_ptII = 5905
    # print("Correct result pt 2:", result_ptII == test_result_ptII)