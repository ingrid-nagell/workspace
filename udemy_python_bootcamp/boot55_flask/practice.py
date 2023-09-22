from flask import Flask

app = Flask(__name__)

def bold_type(function):
    def wrapper():
        text = function()
        return f'<b>{text}</b>'
    return wrapper

def align_center(function):
    def wrapper():
        text = function()
        return f'<p style="text-align: center"]>{text}</p>'
    return wrapper


@app.route("/")
def hello():
    return "hello world"

@app.route("/decor")
@bold_type
@align_center
def decorate():
    return "decorate this page :)"

@app.route("/user/<name>/<int:number>")
def names(name, number):
    return f"YOLO {name}, this is number {number}"

if __name__ == "__main__":
    app.run(debug=True)