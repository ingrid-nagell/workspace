import re

data_path = "AoC\\2023\\06_1_test.txt"
data_path = "AoC\\2023\\06_input.txt"
input = [line.strip() for line in open(data_path, 'r')]

# pt1
def get_numbers(row: list) -> list[tuple, tuple]:
    time = re.findall(r"\d+", input[0])
    records = re.findall(r"\d+", input[1])
    races = [(int(t), int(r)) for t, r in zip(time, records)]
    return races

def winning_times(race: tuple) -> int:
    race_time = race[0]
    record = race[1]
    winning = 0
    for button_time in range(0, race_time):
        moving_time = race_time-button_time
        distance = button_time*moving_time
        if distance > record:
            winning += 1
    return winning



def get_result_ptI(input: list) -> int:
    races = get_numbers(input)
    winning_chances_pr_race = 1
    for race in races:
        winning = winning_times(race)
        if winning != 0:
            winning_chances_pr_race *= winning_times(race)
    return winning_chances_pr_race



# pt2
def get_numbers_ptII(input: list) -> tuple[int, int]:
    race = (int(re.findall(r"\d+", input[0].replace(" ", ""))[0]), int(re.findall(r"\d+", input[1].replace(" ", ""))[0]))
    return race

def get_result_ptII(input: list) -> int:
    race_stats = get_numbers_ptII(input)
    winning = winning_times(race_stats)
    return winning


if __name__ == "__main__":
    result_ptI = get_result_ptI(input)
    print(result_ptI)
    
    result_ptII = get_result_ptII(input)
    print(result_ptII)

    # for dev:
    test_result_ptI = 288
    # print("Correct result pt 1:", result_ptI == test_result_ptI)

    test_result_ptII = 71503
    # print("Correct result pt 2:", result_ptII == test_result_ptII)