#### List Comprehension ####
# new_list = [new_item for item in list if test]

#### 1 ####
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# even = [n for n in numbers if n % 2 == 0]
# print(even)

#### 2 ####
# file1 = [3, 6, 5, 8, 33, 12, 7, 4, 72, 2, 42, 13]
# file2 = [3, 6, 13, 5, 7, 89, 12, 3, 33, 34, 1, 344, 42]
# result = [n for n in file1 if n in file2]
# print(result)


#### Dictionary comprehension: ####
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dict.items()}

#### 3 ####
# from random import randint
# names = ["Ida", "Alex", "Caroline"]
# scores = {name:randint(1,100) for name in names}
# print(scores)

#### 4 ####
# passed = {name:score for (name, score) in scores.items() if score > 70}
# print(passed)

#### 5 ####
# sentence = "What is the Airspeed Velocity on an Unladen Swallow?"
# result = {word:len(word) for word in sentence.split()}
# print(result)

#### 6 ####
# weather = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24
# }

# def celcius_to_farenheight(degrees):
#     return (degrees * 9 / 5) + 32

# weather_f = {day:celcius_to_farenheight(temp) for (day, temp) in weather.items()}
# print(weather_f)

#### Pandas dataframes: ####
#### 7 ####
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas as pd
df = pd.DataFrame(student_dict)
print(df)

# loop through each column:
for (key, value) in df.items():
    print(value)

# loop through rows:
for (index, row) in df.iterrows():
    print(row) # pandas series object
    print(row.score)