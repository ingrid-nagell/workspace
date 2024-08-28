from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlite3 import IntegrityError

APIKEY = "TopSecretAPIKey"

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def get_random_cafe():
    query = db.session.execute(db.select(Cafe).order_by(db.sql.func.random()).limit(1))
    random_cafe = query.scalar()
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def get_all_cafes():
    query = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = query.scalars().all()
    return jsonify(cafes = [cafe.to_dict() for cafe in all_cafes])


@app.route("/search")
def get_specific_cafe():
    search_str = request.args.get("loc") #/search?loc=some_str
    query = db.session.execute(db.select(Cafe).filter(Cafe.location.contains(search_str)).order_by(Cafe.location))
    all_cafes = query.scalars().all()
    if all_cafes:
        return jsonify(cafes = [cafe.to_dict() for cafe in all_cafes])
    else:
        return jsonify(error = {"Not found": "No cafes registered at this loaction."})


@app.route("/add", methods=["POST"])
def add_cafe():
    try:
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("loc"),
            has_sockets=bool(request.form.get("sockets")),
            has_toilet=bool(request.form.get("toilet")),
            has_wifi=bool(request.form.get("wifi")),
            can_take_calls=bool(request.form.get("calls")),
            seats=request.form.get("seats"),
            coffee_price=request.form.get("coffee_price"),
        )
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response = {"success": "Successfully added the new cafe."})
    except IntegrityError:
        db.session.rollback()
        print("cafe already in the database")
        return jsonify(response={"fail": "This cafe already existed in the database."})


@app.route("/update-price/<int:id>", methods=["GET", "PATCH"])
def update_price(id):
    new_price = request.args.get("new_price") #/update-price/<id>?new_price=some_str
    cafe = db.get_or_404(Cafe, id)

    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()

        query = db.session.execute(db.select(Cafe).where(Cafe.id==id).order_by(Cafe.name))
        all_cafes = query.scalars().all()
        return jsonify(cafes = [cafe.to_dict() for cafe in all_cafes]), 200
    

@app.errorhandler(404) # Handles error from above (but adjust to adapt to other views?)
def invalid_route(e):
    return jsonify(error={'Not found': 'Sorry a cafe with that id was not found in the database.'}), 404

@app.route("/delete-cafe/<int:id>", methods=["GET","DELETE"])
def delete_cafe(id):
    api_key = request.args.get("api-key")

    if api_key == APIKEY:
        cafe = db.get_or_404(Cafe, id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()

        return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200

    else:
        return jsonify(error={"error": "Invalid API KEY"}), 403

if __name__ == '__main__':
    app.run(debug=True)
