from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=False, unique=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    favorites = db.relationship('Favorites', backref="user")

    def __repr__(self):
        return self.username

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "name": self.name,
            "email": self.email,
            "favorites": self.favorites
        }

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    hair_color = db.Column(db.String(250), nullable=False)
    eye_color = db.Column(db.String(250), nullable=False)
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    population = db.Column(db.Integer, nullable=False)
    climate = db.Column(db.String(250), nullable=False)
    terrain = db.Column(db.String(250), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
        }

class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(250), nullable=False)
    cargo_capacity = db.Column(db.Integer, nullable=False)
    crew = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "cargo_capacity": self.cargo_capacity,
            "crew": self.crew,
        }

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    characters_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    characters = db.relationship('Characters')
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    planets = db.relationship('Planets')
    vehicles_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
    vehicles = db.relationship('Vehicles')

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "characters_id": self.characters_id,
            "planets_id": self.planets_id,
            "vehicles_id": self.vehicles_id,
        }


