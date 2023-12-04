from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from forms import SearchMovieForm, EditMovieForm
from tmdb_api import search_movies_from_tmdb, get_movie_info, get_movie_image


app = Flask(__name__)

# Config and extensions:
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top_ten_movies.db"

Bootstrap5(app)
db = SQLAlchemy()
db.init_app(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Float, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    # Optional
    def __repr__(self):
        return f'<Movie {self.title}>'

with app.app_context():
    db.create_all()


#### app routes ####
@app.route("/")
def home():
    # Get records:
    all_movies = db.session.execute(db.select(Movie).order_by(Movie.rating.desc())).scalars().fetchall()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=['GET', 'POST'] )
def edit():
    """
    Page for editing user ranking and review.

    Renders a quick form and updates sqlite db with user input.
    """
    movie_id_as_int = int(request.args.get('id'))
    movie = db.session.execute(db.select(Movie).where(Movie.id==movie_id_as_int)).scalar()

    edit_movie_form = EditMovieForm()

    if edit_movie_form.validate_on_submit():
        movie.rating =  float(request.form["rating"])
        movie.review =  request.form["review"]
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", form=edit_movie_form, movie=movie)


@app.route("/delete", methods=['GET', 'POST'] )
def delete():
    movie_id_as_int = int(request.args.get('id'))
    movie = db.session.execute(db.select(Movie).where(Movie.id==movie_id_as_int)).scalar()

    db.session.delete(movie)
    db.session.commit()
    
    return redirect(url_for('home'))


@app.route("/search", methods=['GET', 'POST'] )
def search():
    search_result = None
    search_movie_form = SearchMovieForm()
    if search_movie_form.validate_on_submit():
        search_title = request.form["title"]
        search_result = search_movies_from_tmdb(search_title)
        # return redirect(url_for('home'))
    return render_template("search.html", form=search_movie_form, search_result=search_result)


@app.route("/movie", methods=['GET', 'POST'] )
def movie():
    id = request.args.get('id')
    movie_info = get_movie_info(id)
    img_path = get_movie_image(movie_info['poster_path'])
    return render_template("movie.html", movie=movie_info, img_path=img_path)


@app.route("/add", methods=['GET', 'POST'])
def add_movie():
    id = request.args.get('id')
    movie_info = get_movie_info(id)
    release_year = int(movie_info['release_date'][0:4])
    img_path = get_movie_image(movie_info['poster_path'])

    new_movie = Movie(
        title = movie_info['title'],
        year = release_year,
        description = movie_info['overview'],
        rating = 0,
        ranking = round(movie_info['vote_average'], 2),
        review = "",
        img_url = img_path,
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
