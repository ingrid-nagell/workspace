from flask import Flask

from random import randint
random_number = randint(0,9)


app = Flask(__name__)

def html_header(f):
    def wrapper():
        text = f()
        return f"<h1>{text}</h1>"
    return wrapper


@html_header
def home_title():
    return "Guess a number between 0 and 9"

@app.route("/")
def home():
    header = home_title()
    return f'{header} \
        <iframe src="https://giphy.com/embed/B0vFTrb0ZGDf2" \
        width="480" height="253" frameBorder="0" class="giphy-embed" allowFullScreen></iframe> \
        <p><a href="https://giphy.com/gifs/city-bus-doll-B0vFTrb0ZGDf2">via GIPHY</a></p>'


@app.route("/<int:number>")
def number_page(number):
    if number == random_number: 
        return f"You guessed the number {number}, its the same as random number!"
    elif number < random_number:
        return "You guessed a too low number"
    else:
        return "You guessed a too high number"


if __name__ == "__main__":
    print(random_number)
    app.run(debug=True)