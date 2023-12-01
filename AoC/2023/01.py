#calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
# a1b2c3d4e5f -> l5
import re
from word2number import w2n

data_path = "AoC\\2023\\01_1_test.txt"
data_path = "AoC\\2023\\01_input.txt"
calibration_data = [line.strip() for line in open(data_path, 'r')]


# pt I
sum = 0
for data in calibration_data:
    matches = re.findall(f"\d", data)
    if matches:
        first_digit =  matches[0]
        last_digit =  matches[-1]
        add = int(first_digit+last_digit)
        sum += add

print("ptI:", sum)


# pt II
data_path = "AoC\\2023\\01_2_test.txt"
data_path = "AoC\\2023\\01_input.txt"
calibration_data = [line.strip() for line in open(data_path, 'r')]

sum = 0

for s in calibration_data:
    matches = re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|[0-9]))", s)
    print(matches)
    if matches:
        first_digit =  w2n.word_to_num(matches[0])
        last_digit =  w2n.word_to_num(matches[-1])
        add = int(f"{first_digit}{last_digit}")
        sum += add
        
print("ptII:", sum)
