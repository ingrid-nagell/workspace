import re
from datetime import datetime
from loguru import logger

# data_path = "AoC\\2023\\08_1_test.txt"
# data_path = "AoC\\2023\\08_2_test.txt"
data_path = "AoC\\2023\\08_input.txt"
input = [line.strip().split() for line in open(data_path, 'r')]

# pt1
# instructions_test1 = "LLR"
# instructions_test2 = "LR"
instructions = "LRRLLRLLRRLRRLLRRLLRLRRRLLRRLRRRLRRLRRRLLRRLLRLLRRLRLRRRLRRLLRRRLRLRRLRRLRLRLRLLRLRRRLLRLLRRLRRRLRLRLRRRLRRLLRRRLRLRRLRRLLRRLRRRLRRLRRLRRLLRLRLRRLLRLLRRRLRRLRRLRRRLRLLRRRLRRRLRRLLRRRLRRRLRLLRLRRLRLLRRLLLRRLRRLRRLRLRRRLRRLLRLRRRLRRLRLLLRRLRRLRRRLLLRLLLLRRLRLLLRLRRRLRRRLRLRRRLLLLRLRRRLRLLLRRLRLRRLRRLRRRLRRRR"

nodes = {}
for l in input:
    nodes[l[0]] = [re.sub("[\(,]", "", l[2]), l[3].replace(")", "")]

def get_result_ptI(nodes: dict, instructions: str) -> int:
    logger.info("Start running result function.")
    time_start = datetime.now()
    counter = 0
    go_further = True
    element = "AAA"
    while go_further:
        for i in instructions:
            counter += 1
            if i == "L":
                element = nodes[element][0]
            elif i == "R":
                element = nodes[element][1]

            if element == "ZZZ":
                go_further = False
                break

    time_end = datetime.now()
    logger.info(f"total time seconds {time_end-time_start}")
    return counter


# pt2
def get_starting_points(nodes) -> list:
    pattern = re.compile(".*A$")
    elements = [n for n in nodes if re.match(pattern, n)]
    return elements

def get_z_points(nodes) -> list:
    pattern = re.compile(".*Z$")
    elements = [n for n in nodes if re.match(pattern, n)]
    return elements

print(get_starting_points(nodes))

# start: ['BXA', 'KBA', 'VTA', 'AAA', 'HMA', 'HLA']
# between: follow instructions L/R at what point do each arrive at one of the ends?
# end point are all at the right side
# end: ['CHZ', 'XQZ', 'ZZZ', 'LSZ', 'KMZ', 'KRZ']

def get_end_points(elements: list) -> bool:
    pattern = re.compile(".*Z$")
    for e in elements:
        if not re.match(pattern, e):
            return False
    return True



# the brute force, while loop does not work. 
# think opposite way, check possible combos for it to end?
# All AAA goes to ZZZ, at every 18113
# HMA goes to ....
# HLA

def test_f(nodes: dict, instructions: str) -> int:
    logger.info("Start running test function.")
    counter = 0
    elements = 'HMA'
    go_further = True
    # print(elements)
    while go_further:
        for i in instructions:
            # print(elements, i, nodes[elements])
            counter += 1
            if i == "L":
                elements = nodes[elements][0]
            elif i == "R":
                elements = nodes[elements][1]
            if get_end_points(elements):
                print(elements, counter)

test_f(nodes, instructions)
# def get_result_ptII(nodes: dict, instructions: str) -> int:
#     logger.info("Start running result function.")
#     time_start = datetime.now()
#     counter = 0
#     go_further = True
#     elements = get_starting_points(nodes)
#     # print(elements)
#     while go_further:
#         for i in instructions:
#             # print("INSTRUCTION", i)
#             counter += 1
#             # print(counter)
#             # logger.info(f"Round no: {counter}")
#             elements_replacement = []
#             for elem in elements:
#                 if i == "L":
#                     elements_replacement.append(nodes[elem][0])
#                 elif i == "R":
#                     elements_replacement.append(nodes[elem][1])
#             elements = elements_replacement
#             # print(elements)
#             # print(get_end_points(elements))
            
#             if get_end_points(elements):
#                 go_further = False
#                 break

#     time_end = datetime.now()
#     logger.info(f"Total time in seconds {time_end-time_start}")
#     return counter

# get_result_ptII(nodes, instructions)


# if __name__ == "__main__":
#     print("---")
#     # print(nodes)
#     # result_ptI = get_result_ptI(nodes, instructions)
#     # print(result_ptI)
    
#     result_ptII = get_result_ptII(nodes, instructions)
#     print(result_ptII)