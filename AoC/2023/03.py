import re

data_path = "AoC\\2023\\03_1_test.txt"
data_path = "AoC\\2023\\03_2_test.txt"
data_path = "AoC\\2023\\03_input.txt"
input = [line.strip() for line in open(data_path, 'r')]

# pt I
# but apparently any number adjacent to a symbol, even diagonally, is a "part number" 
# and should be included in your sum. (Periods (.) do not count as a symbol.)

def find_all_number_in_row(row: str) -> tuple[list, list]:
    indices = []
    numbers = []
    matches = re.finditer(r"\d+", row)
    for m in matches:
        indices.append(m.span()) 
        numbers.append(int(m.group(0)))
    return indices, numbers


def check_numbers_in_row(row_number: int, input: list) -> int:
    indices, numbers = find_all_number_in_row(input[row_number])
    accepted_numbers = []
    all_adjacent_rows = [row_number - 1, row_number, row_number + 1]

    for number_indices, number in zip(indices, numbers):
        placement_interval = range(number_indices[0]-1, number_indices[1]+1)
        # print(number_indices, number, placement_interval)

        for row in all_adjacent_rows:
            if row in range(0, len(input)):
                adjacent_row = input[row]
                # print(adjacent_row)
                for i in range(0, len(adjacent_row)):
                    if i in placement_interval and re.match(r"[^a-zA-Z0-9.]", adjacent_row[i]):
                        accepted_numbers.append(number)
    # print(accepted_numbers)
    return sum(accepted_numbers)


def get_result_ptI(input: list) -> int:
    all_numbers = []
    for row in range(0, len(input)):
        numbers = check_numbers_in_row(row, input)
        all_numbers.append(numbers)
    # print(all_numbers)
    return sum(all_numbers)


# pt II
# A gear is any * symbol that is adjacent to exactly two part numbers. 
# Its gear ratio is the result of multiplying those two numbers together.
# 55* or *67 

# This time, you need to find the gear ratio of every gear 
# and add them all up so that the engineer can figure out which gear needs to be replaced.
def find_all_symbols_in_row(row: str) -> tuple[list, list]:
    indices = []
    matches = re.finditer(r"\*", row)
    for m in matches:
        indices.append(m.span()[0]) 
    return indices
    

def check_symbols(row_number: int, input: list) -> int:
    indices = find_all_symbols_in_row(input[row_number])
    all_adjacent_rows = [row_number - 1, row_number, row_number + 1]
    row_sum = 0

    for symbol_index in indices:

        adjacent_numbers = []
        placement_interval =  [symbol_index-1, symbol_index, symbol_index + 1]

        for row in all_adjacent_rows:
            adjacent_number_indices = []
            if row in range(0, len(input)):
                # print("FOR * IN POSITION: ", symbol_index, "CHECKING ADJECTENT ROW: ", row, )
                adjacent_row = input[row]
                numbers_indices, numbers = find_all_number_in_row(adjacent_row)

                for i, n in zip(numbers_indices, numbers):
                    for p in placement_interval:
                        if bool(p in list(range(i[0], i[1]))):
                            if i not in adjacent_number_indices:
                                adjacent_number_indices.append(i)
                                adjacent_numbers.append(n)

        # print("-- LIST: ", adjacent_numbers)

        if len(adjacent_numbers) == 2:
            total = 1
            for n in adjacent_numbers:
                total *= n
            row_sum += total
    return row_sum


def get_result_ptII(input: list) -> int:
    all_numbers = []
    for row in range(0, len(input)):
        total = check_symbols(row, input)
        if total:
            all_numbers.append(total)
    return sum(all_numbers)



if __name__ == "__main__":
    result_ptI = get_result_ptI(input)
    
    result_ptII = get_result_ptII(input)
    print(result_ptII)

    # for dev:
    test_result_ptI = 4361
    # print(result_ptI == test_result_ptI)

    test_result_ptII = 467835
    # print(result_ptII == test_result_ptII)