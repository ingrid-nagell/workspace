#DAY04
import re

my_path = 'C:/Users/G020772/workspace/AoC/2022/test.txt'
my_path = 'C:/Users/G020772/data/AoC/input04.txt'

with open(my_path, 'r') as f:
    data = [re.split(',|-', i) for i in [l.strip() for l in f]]

# part I
overlap_full = 0
for pair in data:
    pair = [int(elem) for elem in pair]
    if  (pair[0] >= pair[2] and pair[1] <= pair[3]) or (pair[2] >= pair[0] and pair[3] <= pair[1]) :
        overlap_full += 1
print(overlap_full)

# can it be done with range (typ range in range?)?

# part II
overlap_all = 0
for pair in data:
    pair = [int(elem) for elem in pair]
    match = False
    for id in range(pair[0], pair[1]+1):
        if id in range(pair[2], pair[3]+1):
            match = True
    if match:
        overlap_all += 1
print(overlap_all)