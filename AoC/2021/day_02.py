#### part I ####
# 1 forward - increases horizontal pos
# 2 down - increases depth
# 3 up - decreases depth
horizontal = 0
depth = 0

my_path = 'advent_of_code/2021/test_02.txt'
my_path = 'advent_of_code/2021/input_02.txt'

# nested list by list comprehension:
# data = [line.split() for line in open(my_path, 'r')]
# print(data)

with open(my_path) as f:
    for line in f:
        (key, val) = line.split()
        if key == "forward":
            horizontal += int(val)
        elif key == "down":
            depth += int(val)
        elif key == "up":
            depth -= int(val)

print("New position:", horizontal*depth)


#### part II ####
# down x increases aim by x units
# up x decreases aim by x units
# forward x increases horizontal by x units
# forward x increases depth by aim * x units
aim = 0
horizontal = 0
depth = 0

with open(my_path) as f:
    for line in f:
        (key, val) = line.split()
        if key == "forward":
            horizontal += int(val)
            depth += aim*int(val)
        elif key == "down":
            aim += int(val)
        elif key == "up":
            aim -= int(val)

print("New position:", horizontal*depth)
