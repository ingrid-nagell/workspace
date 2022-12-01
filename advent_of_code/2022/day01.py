#AoC Day 1 2022

#my_path = 'input01_test.txt'
my_path = 'C:/Users/G020772/data/AoC/input01_2022.txt'

#Part I
calories_data = [line.strip() for line in open(my_path, 'r')]
elf_total = 0
elves_totals = []

for i in calories_data:
    if i != '':
        elf_total += int(i)
    else:
        #if elf_total > highest_total:
        #    highest_total = elf_total
        elves_totals.append(elf_total)
        elf_total = 0

print("Highest carrying amount: ", max(elves_totals))

#Part II
top_three = []
for i in range(0, 3):
    top_three.append(max(elves_totals))
    elves_totals.remove(max(elves_totals))

print("The sum of the top three crarrying elves: ", sum(top_three))