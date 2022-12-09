# DAY 07 2022
import re

#my_path = 'C:/Users/G020772/workspace/AoC/2022/test.txt'
my_path = 'C:/Users/G020772/data/AoC/input07.txt'

with open(my_path, 'r') as f:
    data = [l.strip() for l in f]

def navigate_sys(data, path):
    if re.search(r"\$ cd", data):
        input = re.sub(r"\$ cd ","", data)
        if input == '/':
            path = path + input
        elif input == '..':
            path = re.sub(r'([a-z]*/)$', '', path)
        else:
            path = path + input + '/'
    return path

# Loop through lines:
path_to_file = ""
paths = {}
for e in range(0, len(data)):
    path_to_file = navigate_sys(data[e], path_to_file)
    
    if path_to_file not in paths:
        paths[path_to_file] = 0

    if re.search(r"\d+", data[e]):
        paths[path_to_file] += int(re.search(r"\d+", data[e]).group(0))

# Calculate sum 
total_sum = 0

dir_delete = []
for k1, v1 in paths.items():
    total = v1
    for k2, v2 in paths.items():
        if k1 != k2 and re.match(k1, k2):
            total += v2
    if total <= 100000:
        total_sum += total
    # for part II:
    dir_delete.append(total)

print(total_sum)

# part II
unused_space = 70000000 - max(dir_delete)
space_needed = 30000000 - unused_space
large_enough_dir = [x for x in dir_delete if x >= space_needed]
print(min(large_enough_dir))