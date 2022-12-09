#DAY05
import numpy as np
import re

#my_path_crates = 'C:/Users/G020772/workspace/AoC/2022/test.txt'
#my_path_instructions = 'C:/Users/G020772/workspace/AoC/2022/test02.txt'
my_path_crates = 'C:/Users/G020772/data/AoC/input05_crates.txt'
my_path_instructions = 'C:/Users/G020772/data/AoC/input05_instructions.txt'

with open(my_path_crates, 'r') as f:
    crates = np.array([[l.strip('\n')] for l in f])

with open(my_path_instructions, 'r') as f:
    instructions =  [re.findall(r"\d+", elem) for elem in [l.strip() for l in f]]

no_of_piles = int((len(crates[0][0])+1)/4)
crates = np.flip(crates, axis=0)

crates_ordered = []
for row in crates:
    for l in row:
        l = re.sub("    ", " - ", l)
        l = re.sub("[\[\]]", "", l).split()
    crates_ordered.append(l)

pile = []
for n in range(0, no_of_piles):
    p = ""
    for c in crates_ordered: 
       if c[n] != '-':
           p += c[n]
    pile.append(p)

for s in instructions:
    for i in range(0, int(s[0])):
        crate = pile[int(s[1])-1][-1]
        pile[int(s[2])-1] = pile[int(s[2])-1] + crate
        pile[int(s[1])-1] = pile[int(s[1])-1][:-1]

top_crates = ""
for c in pile:
    top_crates += c[-1]
print(top_crates)

# part II ------------------------------------------------------------------
pile = []
for n in range(0, no_of_piles):
    p = ""
    for c in crates_ordered: 
       if c[n] != '-':
           p += c[n]
    pile.append(p)

for s in instructions:
    crate = pile[int(s[1])-1][-int(s[0]):]
    pile[int(s[2])-1] = pile[int(s[2])-1] + crate
    pile[int(s[1])-1] = pile[int(s[1])-1][: -int(s[0])]

top_crates = ""
for c in pile:
    top_crates += c[-1]
print(top_crates)