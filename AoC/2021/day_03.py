#### Part I ####
# power consumption = gamma * epsilon
# gamma = Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report.
#


my_path = 'advent_of_code/2021/test_03.txt'
my_path = 'advent_of_code/2021/input_03.txt'

data = [line.split()[0] for line in open(my_path, 'r')]

gamma = ""
epsilon = ""

for i in range(0, len(data[0])):
    zeroes = 0
    ones = 0
    for e in range(0, len(data)):
        if data[e][i] == '0':
            zeroes += 1
        elif data[e][i] == '1':
            ones += 1
    if zeroes > ones:
        gamma += "0"
        epsilon += "1"
    elif zeroes < ones:
        gamma += "1"
        epsilon += "0"

print("Part I:",int(gamma, 2)*int(epsilon, 2))


#### Part II ####
# life support rating = oxygen generator rating * CO2 scrubber rating

# O2
keep = data

for i in range(0, len(keep[0])):
    zeroes = []
    ones = []
    if len(keep) > 1:
        for e in keep:
            if e[i] == '0':
                zeroes.append(e)
            elif e[i] == '1':
                ones.append(e)

        if bool(len(zeroes) > len(ones)):
            keep = zeroes
        else:
            keep = ones
o2 = keep[0]

# CO2
keep = data

for i in range(0, len(keep[0])):
    zeroes = []
    ones = []
    if len(keep) > 1:
        for e in keep:
            if e[i] == '0':
                zeroes.append(e)
            elif e[i] == '1':
                ones.append(e)
        if bool(len(ones) < len(zeroes)):
            keep = ones
        else:
            keep = zeroes
co2 = keep[0]

print("Part II:", int(o2, 2) * int(co2, 2))