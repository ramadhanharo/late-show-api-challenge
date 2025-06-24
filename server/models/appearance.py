from server.models import db

class Appearance(db.Model):
    __tablename__ = 'appearances'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)

    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "rating": self.rating,
            "guest_id": self.guest_id,
            "episode_id": self.episode_id
        }

    def to_dict_with_guest(self):
        return {
            "id": self.id,
            "rating": self.rating,
            "guest": self.guest.to_dict()
        }

    def to_dict_with_episode(self):
        return {
            "id": self.id,
            "rating": self.rating,
            "episode": self.episode.to_dict()
        }
