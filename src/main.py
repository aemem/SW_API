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

#user routes
@app.route('/users', methods=['GET'])
def get_users():
   users = User.query.all()
   return jsonify({"users": users}), 200

@app.route('/users/favorites', methods=['GET'])
def get_user_favs():
    favs = Favorites.query.all()
    return jsonify({"favorites": favorites})

#character routes
@app.route('/characters', methods=['GET'])
def get_characters():
    characters = Characters.query.all()
    return jsonify({"characters": characters}), 200
   
@app.route('/character/<int: char_id>', methods=['GET'])
def get_character_by_id(char_id):
    char = Characters.query.get(char_id)
    return jsonify({"character": char.serialize()}), 200

#planet routes
@app.route('/planets', methods=['GET'])
def get_planets():
    planets = Planets.query.all()
    return jsonify({"planets": planets}), 200
 
@app.route('/planet/<int: character_id>', methods=['GET'])
def get_planet_by_id(plan_id):
    plan = Planets.query.get(plan_id)
    return jsonify({"planet": plan.serialize()}), 200

#vehicle routes
@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    vehicles = Vehicles.query.all()
    return jsonify({"vehicles": vehicles}), 200

@app.route('/vehicle/<int: chavehicle_id>', methods=['GET'])
def get_vehicle_by_id(vehi_id):
    vehi = Vehicles.query.get(vehi_id)
    return jsonify({"vehicle": vehi.serialize()}), 200

#add favs
@app.route('/favorite/character/<int:character_id', methods=['POST'])
def add_fav_character():
    body_characters_id = request.json.get("characters_id")
    favorite_characters = Favorite_characters(characters_id=body_characters_id)
    db.session.add(favorite_characters)
    db.session.commit()
    return jsonify({"favortie characters": favorites.characters_id}), 200

@app.route('/favorite/planet/<int:planet_id', methods=['POST'])
def add_fav_planet():
    body_planets_id = request.json.get("planets_id")
    favorite_planets = Favorite_planets(planets_id=body_planets_id)
    db.session.add(favorite_planets)
    db.session.commit()
    return jsonify({"favortie planets": favorites.planets_id}, 200

@app.route('/favorite/vehicle/<int:vehicle_id', methods=['POST'])
def add_fav_vehicle():
    body_vehicles_id = request.json.get("vehicles_id")
    favorite_vehicles = Favorite_cvehicles(vehicles_id=body_vehicles_id)
    db.session.add(favorite_vehicles)
    db.session.commit()
    return jsonify({"favortie vehicles": favorites.vehicles_id}, 200

#delete favs
@app.route('/favorite/character/<int:character_id', methods=['DELETE'])
def delete_fav_character(char_id):
    char = Characters.query.get(char_id)
    db.session.delete(char)
    db.session.commit()
    return jsonify({"deleted": True}), 200

@app.route('/favorite/planet/<int:planet_id', methods=['DELETE'])
def delete_fav_planet(plan_id):
    plan = Planets.query.get(plan_id)
    db.session.delete(plan)
    db.session.commit()
    return jsonify({"deleted": True}), 200

@app.route('/favorite/vehicle/<int:vehicle_id', methods=['DELETE'])
def delete_fav_planet(vehi_id):
    vehi = Vehicles.query.get(vehi_id)
    db.session.delete(vehi)
    db.session.commit()
    return jsonify({"deleted": True}), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
