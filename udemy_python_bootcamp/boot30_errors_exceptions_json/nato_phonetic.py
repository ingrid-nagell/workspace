# NATO alphabet project
from pandas import read_csv

df = read_csv("C:\\Users\\G020772\\workspace\\python_bootcamp\\boot26_listcomp\\nato_phonetic_alphabet.csv")

nato = {r.letter:r.code for (i, r) in df.iterrows()}

def convert_letter():
    word = input("Type a word: ")
    try:
        phonetic = [nato[letter.upper()] for letter in word]
    except KeyError:
        print("Words only")
        convert_letter()
    else:
        print(phonetic)

convert_letter()