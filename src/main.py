"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/users', methods=['GET'])
def get_users():
    body_username = request.json.get("username")
    body_name = request.json.get("name")
    body_email = request.json.get("email")
    body_favorites_id = request.json.get("favorites_id")
    users = Users(username=body_username, name=body_name, email=body_email, favorites_id=body_favorites_id)
    db.session.add(users)
    db.session.commit()
    return jsonify({"users": users.username})

@app.route('/users/favorites', methods=['GET'])
def get_users():
    return 

@app.route('/characters', methods=['GET'])
def get_characters():
    body_name = request.json.get("name")
    body_age = request.json.get("age")
    body_hair_color = request.json.get("hair_color")
    body_eye_color = request.json.get("eye_color")
    characterss = Characters(name=body_name, age=body_age, hair_color=body_hair_color, eye_color=body_eye_color)
    db.session.add(characters)
    db.session.commit()
    return jsonify({"characters": characters.name})

@app.route('/characters/<int: character_id>', methods=['GET'])
def get_character_by_id():

    return

@app.route('/planets', methods=['GET'])
def get_planets():

    return

@app.route('/planets/<int: character_id>', methods=['GET'])
def get_planet_by_id():

    return

@app.route('/vehicles', methods=['GET'])
def get_vehicles():

    return

@app.route('/vehicles/<int: chavehicle_id>', methods=['GET'])
def get_vehicle_by_id():

    return

@app.route('/favorite/character/<int:character_id', methods=['POST', 'DELETE'])
def get_fav_character():
    if request.method == "POST"

    return
    elif request.method == "DELETE" 
    
    return

@app.route('/favorite/planet/<int:planet_id', methods=['POST', 'DELETE'])
def get_fav_planet():
    if request.method == "POST"

    return
    elif request.method == "DELETE" 
    
    return

@app.route('/favorite/vehicle/<int:vehicle_id', methods=['POST', 'DELETE'])
def get_fav_vehicle():
    if request.method == "POST"

    return
    elif request.method == "DELETE" 
    
    return

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
