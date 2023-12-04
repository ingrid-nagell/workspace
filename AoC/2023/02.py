import re

# data_path = "AoC\\2023\\02_1_test.txt"
data_path = "AoC\\2023\\02_input.txt"
input = [re.split(":|;|,", line.strip()) for line in open(data_path, 'r')]


# ptI
def extract_string_info(input_string: str) -> str | int:
    k = re.findall("[a-zA-Z]", input_string)
    k = "".join(k)
    v = re.findall("\d", input_string)
    v = int("".join(v))
    return k, v


def find_possible_games(input: list) -> int:
    not_possible_games = []
    sum_games = 0
    game = 0
    for g in input:
        game += 1
        for s in g:
            k,v = extract_string_info(s)
            if (k == "red" and v > 12) or (k == "green" and v > 13) or (k=="blue" and v > 14):
                if game not in not_possible_games:
                    not_possible_games.append(game)
        
        sum_games += game
    
    sum_not_possible_games = sum(not_possible_games)
    sum_id_possible_games = sum_games - sum_not_possible_games

    return sum_id_possible_games


# pt II
def find_game_power(input: list) -> int:
    total_power = 0
    for game in input:
        cubes = {"red": 1, "green": 1, "blue": 1,}

        for s in game:
            k,v = extract_string_info(s)
            if k in cubes:
                if v > cubes[k]:
                    cubes[k] = v

        power = 1
        for value in cubes.values():
            power *= value

        total_power += power

    return total_power


if __name__ == "__main__":
    print(find_possible_games(input))
    print(find_game_power(input))