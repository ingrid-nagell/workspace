from flask import Flask

app = Flask(__name__) # flask checks if this is the current file where the app code is located, and we are not using an imported module or something.
# __name__ denotes the file that is currently being run.

@app.route('/') # home route, is a python decorator, only trigger function if app.route is '/'
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":     # executes program only if it is run as a script
    app.run()                  # does the same as flask run


# To run in terminal:
# set FLASK_APP=<path> | export on mac - export to environment variables
# flask run

# if "set FLASK_APP=<path>" does not work:
    # one can name the file app.py instead.
    # Create a ".flaskenv" in your project's root directory and write FLASK_APP=<name.py>