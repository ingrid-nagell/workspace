import re
from datetime import datetime
from loguru import logger

data_path = "AoC\\2023\\09_1_test.txt"
# data_path = "AoC\\2023\\09_2_test.txt"
# data_path = "AoC\\2023\\09_input.txt"
input = [line.strip().split() for line in open(data_path, 'r')]

# pt1

def get_result_ptI(nodes: dict, instructions: str) -> int:
    pass

# pt2

if __name__ == "__main__":
#     print("---")
#     # print(nodes)
    result_ptI = get_result_ptI(input)
    print(result_ptI)
    
#     result_ptII = get_result_ptII(nodes, instructions)
#     print(result_ptII)