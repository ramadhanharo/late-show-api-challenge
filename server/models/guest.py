from server.models import db
from sqlalchemy.orm import validates

class Guest(db.Model):
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    occupation = db.Column(db.String)

    appearances = db.relationship('Appearance', backref='guest', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "occupation": self.occupation
        }

    def to_dict_with_appearances(self):
        return {
            "id": self.id,
            "name": self.name,
            "occupation": self.occupation,
            "appearances": [a.to_dict_with_episode() for a in self.appearances]
        }
