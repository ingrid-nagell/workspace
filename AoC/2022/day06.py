# DAY06 2022

#my_path = 'C:/Users/G020772/workspace/AoC/2022/test.txt'
my_path = 'C:/Users/G020772/data/AoC/input06.txt'

with open(my_path, 'r') as f:
    data = f.read()

def find_marker(data, no_of_char):
    for i in range(0, len(data)):
        if len(set(data[i:i+no_of_char])) == no_of_char:
            return i + len(set(data[i:i+no_of_char]))

result = find_marker(data, 14)
print(result)