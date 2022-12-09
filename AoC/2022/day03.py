#DAY03

import string

#my_path = 'C:/Users/G020772/workspace/AoC/2022/test.txt'
my_path = 'C:/Users/G020772/data/AoC/input03.txt'

with open(my_path, 'r') as f:
    data = [[c for c in l.strip()] for l in f]

alphabets = list(string.ascii_lowercase) + list(string.ascii_uppercase)

#part I
points = 0
for rucksack in data:
    half = int(len(rucksack)/2)
    rucksack = [rucksack[0:half], rucksack[half:]]
    for item in rucksack[0]:
        if item in rucksack[1]:
            item_points = alphabets.index(item) +1
    points += item_points

print(points)

#part II
points = 0
x = iter(data)
for a, b, c in zip(*[x, x, x]):
    badge_items = 0
    for item in a:
        if item in b and item in c:
            badge_item = item
    points += alphabets.index(badge_item) +1

print(points)