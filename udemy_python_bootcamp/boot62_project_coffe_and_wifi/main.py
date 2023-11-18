from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Regexp, URL
import csv
from loguru import logger

DATA_PATH = "udemy_python_bootcamp\\boot62_project_coffe_and_wifi\\cafe-data.csv"


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    coffe_choices = ["✘"]+["☕️" * i for i in range(1, 6)]
    wifi_choices = ["✘"]+["💪" * i for i in range(1, 6)]
    power_choices = ["✘"]+["🔌" * i for i in range(1, 6)]

    cafe = StringField('Cafe name', validators=[DataRequired()])
    maps_link = StringField('Cafe location on Google maps (URL)', validators=[URL()])
    open = StringField('Opening Time (e.g. 8:30AM)', validators=[Regexp(regex ='^(\d{1,2}:\d{2}(?:AM|PM))$', message="Must contain 'd:dd' with an AM or PM suffix.")])
    close = StringField('Closing Time (e.g. 15:00PM)', validators=[Regexp(regex ='^(\d{1,2}:\d{2}(?:AM|PM))$', message="Must contain 'd:dd' with an AM or PM suffix.")])
    coffee_rating = SelectField('Coffee Rating', choices = coffe_choices)
    wifi_rating = SelectField('Wifi Strength', choices = wifi_choices)
    power_rating = SelectField('Power access', choices = power_choices)

    submit = SubmitField('Submit')


# all Flask routes below
@app.route('/')
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    request_made = False

    if form.validate_on_submit():
        data_ingest = [
            form.cafe.data,
            form.maps_link.data,
            form.open.data,
            form.close.data,
            form.coffee_rating.data,
            form.wifi_rating.data,
            form.power_rating.data
        ]
        with open(DATA_PATH, 'a', newline='', encoding='utf-8') as csv_file:
            csv_data = csv.writer(csv_file, delimiter=',')
            csv_data.writerow(data_ingest)

        logger.info(f"The following data was successfully added: {data_ingest}.")
        
        request_made = True

    return render_template('add.html', form=form, request_made=request_made)


@app.route('/cafes')
def cafes():
    with open(DATA_PATH, newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)

    header = list_of_rows[0]
    data = list_of_rows[1:]
    
    return render_template('cafes.html', cafes=data, header=header)


if __name__ == '__main__':
    app.run(debug=True)