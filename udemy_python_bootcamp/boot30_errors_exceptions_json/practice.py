# Exceptions

#try: Something that might cause an exception
#except <ErrorType>: Do this if there was an exception
#else: Do this if there were no exception
#finally: Do this no matter what happens

# FileNotFoundError, KeyError, TypeError, IndexError

# try:
#     file = open("a_file.txt")
#     a_dict={"key":"value"}
#     print(a_dict["key"])
#     print(a_dict)
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("First line of file")
# except KeyError as error_message: # Keep the message in a variable
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError("This is a made up error")

################
## Raise exeptions:
# height = float(input("Height: "))
# weight = int(input("Weight: "))

# if height > 3:
#     raise ValueError("Unrealistic height")

################
# IndexError
fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruitpie")
    else:
        print(fruit + "pie")


make_pie(2)

################
# KeyError
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3},
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes += post['Likes']
    except KeyError:
        pass

print(total_likes)