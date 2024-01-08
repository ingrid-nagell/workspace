import re

data_path = "AoC\\2023\\05_1_test.txt"
# data_path = "AoC\\2023\\05_input.txt"
with open(data_path, 'r') as f:
    input = f.read()
    maps = re.findall(r"[ a-zA-Z\-\:]+[ a-zA-Z\:]+", input)
    for map in maps:
        map_range = maps.split(map,1)
        print(map)
        print(map_range)
        print("---")

# pt1
def get_maps(input):
    print(input)

def get_result_ptI(input: list) -> int:
    pass


# pt2
def get_result_ptII(input: list) -> int:
    pass


if __name__ == "__main__":
    # get_maps(input)
    result_ptI = get_result_ptI(input)
    # print(result_ptI)
    
    result_ptII = get_result_ptII(input)
    # print(result_ptII)

    # for dev:
    test_result_ptI = 13
    print(result_ptI == test_result_ptI)

    test_result_ptII = 30
    print(result_ptII == test_result_ptII)