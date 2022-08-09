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
from models import db, User, Characters, Planets, Vehicles, Favorites

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
   users_serialized = list(map(lambda item: item.serialize(), users))
   return jsonify({"users": users_serialized}), 200

@app.route('/users/favorites', methods=['GET'])
def get_user_favs():
    favs = Favorites.query.all()
    favs_serialized = list(map(lambda item: item.serialize(), favs))
    return jsonify({"favorites": favs_serialized}), 200

#character routes
@app.route('/characters', methods=['GET'])
def get_characters():
    characters = Characters.query.all()
    characters_serialized = list(map(lambda item: item.serialize(), characters))
    return jsonify({"characters": characters_serialized}), 200
   
@app.route('/character/<int:character_id>', methods=['GET'])
def get_character_by_id(character_id):
    char = Characters.query.get(character_id)
    return jsonify({"character": char.serialize()}), 200

#planet routes
@app.route('/planets', methods=['GET'])
def get_planets():
    planets = Planets.query.all()
    planets_serialized = list(map(lambda item: item.serialize(), planets))
    return jsonify({"planets": planets_serialized}), 200
 
@app.route('/planet/<int:planet_id>', methods=['GET'])
def get_planet_by_id(planet_id):
    plan = Planets.query.get(planet_id)
    return jsonify({"planet": plan.serialize()}), 200

#vehicle routes
@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    vehicles = Vehicles.query.all()
    vehicles_serialized = list(map(lambda item: item.serialize(), vehicles))
    return jsonify({"vehicles": vehicles_serialized}), 200

@app.route('/vehicle/<int:vehicle_id>', methods=['GET'])
def get_vehicle_by_id(vehicle_id):
    vehi = Vehicles.query.get(vehicle_id)
    return jsonify({"vehicle": vehi.serialize()}), 200

#add favs
@app.route('/user/<int:user_id>/favorites/character/<int:character_id>', methods=['POST'])
def add_fav_character(user_id, character_id):
    favorite_characters = Favorite_characters(user_id=user_id, characters_id=character_id)
    db.session.add(favorite_characters)
    db.session.commit()
    return jsonify({"favortie characters": favorites.characters_id.serialize()}), 200

@app.route('/user/<int:user_id>/favorite/planet/<int:planet_id>', methods=['POST'])
def add_fav_planet(user_id, planet_id):
    favorite_planets = Favorite_planets(user_id=user_id, planets_id=planet_id)
    db.session.add(favorite_planets)
    db.session.commit()
    return jsonify({"favortie planets": favorites.planets_id.serialize()}), 200

@app.route('/user/<int:user_id>/favorite/vehicle/<int:vehicle_id>', methods=['POST'])
def add_fav_vehicle():
    favorite_vehicles = Favorite_vehicles(user_id=user_id, vehicles_id=vehicle_id)
    db.session.add(favorite_vehicles)
    db.session.commit()
    return jsonify({"favortie vehicles": favorites.vehicles_id.serialize()}), 200


#delete favs
@app.route('/user/<int:user_id>/favorite/character/<int:character_id>', methods=['DELETE'])
def delete_fav_character(character_id):
    char = Characters.query.get(character_id)
    db.session.delete(char)
    db.session.commit()
    return jsonify({"deleted": True}), 200

@app.route('/user/<int:user_id>/favorite/planet/<int:planet_id>', methods=['DELETE'])
def delete_fav_planet(planet_id):
    plan = Planets.query.get(planet_id)
    db.session.delete(plan)
    db.session.commit()
    return jsonify({"deleted": True}), 200

@app.route('/user/<int:user_id>/favorite/vehicle/<int:vehicle_id>', methods=['DELETE'])
def delete_fav_vehicle(vehicle_id):
    vehi = Vehicles.query.get(vehicle_id)
    db.session.delete(vehi)
    db.session.commit()
    return jsonify({"deleted": True}), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
