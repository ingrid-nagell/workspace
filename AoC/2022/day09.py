import numpy as np

my_path = 'C:/Users/G020772/workspace/AoC/2022/test.txt'
#my_path = 'C:/Users/G020772/data/AoC/input09.txt'

with open(my_path, 'r') as f:
    data = [l.strip().split(" ") for l in f]

print(data)
# the head (H) and tail (T) must always be touching 

# If H moves and is still in contact with T, T does not move.
# If H moves away from T, T moves to previous position of H 
tail_coor = []
tail_map = np.array([['H', 'T']])
print(tail_map)
#def move(direction):
tail_map = np.append(tail_map, "H")

print("\n------")
print(tail_map)

tail_map[tail_map=='T'] = '#'
print("\n------")
print(tail_map)