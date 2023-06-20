# NATO alphabet project
from pandas import read_csv

df = read_csv("C:\\Users\\G020772\\workspace\\python_bootcamp\\boot26_listcomp\\nato_phonetic_alphabet.csv")

nato = {r.letter:r.code for (i, r) in df.iterrows()}

def convert_letter(user_input):
    return [nato[letter.upper()] for letter in user_input]

word = input("Type a word:")
print(convert_letter(word))