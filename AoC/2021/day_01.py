import numpy as np
l = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
l = []

l = np.loadtxt('advent_of_code/2021/input_01.txt')

# antall ganger window øker:
def numbers(num):
    increase = 0
    for i in range(1, len(num)):
        current_num = num[i]
        previous_num = num[i-1]
        if current_num > previous_num:
            increase += 1
    return increase

first = numbers(l)
print("Total times it increased:", first)

# sliding window
l_sums = []
for i in range(2, len(l)):
    window_sum = l[i]+l[i-1]+l[i-2]
    l_sums.append(window_sum)

sliding = numbers(l_sums)
print("Total times the sum increased:", sliding)


####### NO LOOPS SOLUTION #########
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

#measurements = np.array([199,200, 208, 210, 200, 207, 240, 269, 260, 263])
measurements = np.loadtxt("advent_of_code/2021/input_01.txt")

current = measurements[1:len(measurements)]
prev = measurements[0:len(measurements)-1]
print(sum(current>prev))

current_slide_sum = np.sum(sliding_window_view(current, window_shape=3), axis=1)
prev_slide_sum = np.sum(sliding_window_view(prev, window_shape=3), axis=1)
print(sum(current_slide_sum > prev_slide_sum))