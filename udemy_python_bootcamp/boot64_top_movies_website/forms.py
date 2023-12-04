from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired, NumberRange


class EditMovieForm(FlaskForm):
    rating = StringField(label="New Movie Rating Out of 10 :", validators=[DataRequired()])
    review = StringField(label="Edit Movie Review:")
    submit = SubmitField(label="Submit changes")


class SearchMovieForm(FlaskForm):
    title = StringField(label="Movie Title:", validators=[DataRequired()])
    submit = SubmitField(label="Search for movie")