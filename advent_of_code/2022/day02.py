# DAY 02

# rock: X, A (1p)
# paper: Y, B (2p)
# scissors: Z, C (3p)
# + outcome: loose 0, draw 3, winning 6

#my_path = 'test.txt'
my_path = 'C:/Users/G020772/data/AoC/input02.txt'

with open(my_path, 'r') as f:
    data = [l.strip().split(" ") for l in f]

points = {"X": 1, "Y": 2, "Z": 3}
winning = [["C","X"], ["A","Y",], ["B","Z"]] 
draw = [["A","X"], ["B","Y"], ["C","Z"]]
loosing = [["B","X"], ["C","Y"], ["A","Z"]]

#part I
score = 0
for elem in data:
    score += points[elem[1]]
    if elem in winning:
        score += 6
    elif elem in draw:
        score += 3

print(score)

#part2
score = 0
for elem in data:
    # loose:
    if elem[1] == "X":
        play = [l[1] for l in loosing if elem[0] in l][0]
    #draw:
    elif elem[1] == "Y":
        score += 3
        play = [d[1] for d in draw if elem[0] in d][0]
    #win:
    elif elem[1] == "Z":
        score += 6
        play = [w[1] for w in winning if elem[0] in w][0]
    score += points[play]

print(score)