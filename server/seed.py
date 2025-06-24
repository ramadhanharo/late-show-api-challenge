from datetime import date
from server.models import db, User, Guest, Episode, Appearance
from server.app import app


with app.app_context():
    print(" Seeding data...")

    # Clear existing data
    Appearance.query.delete()
    Guest.query.delete()
    Episode.query.delete()
    User.query.delete()

    #  Create user
    user = User(username="admin")
    user.set_password("password123")
    db.session.add(user)

    #  Guests
    g1 = Guest(name="Rihanna", occupation="Musician")
    g2 = Guest(name="Elon Musk", occupation="Entrepreneur")
    g3 = Guest(name="Zendaya", occupation="Actress")
    db.session.add_all([g1, g2, g3])

    #  Episodes
    e1 = Episode(date=date(2024, 6, 1), number=101)
    e2 = Episode(date=date(2024, 6, 2), number=102)
    db.session.add_all([e1, e2])

    #  Appearances
    a1 = Appearance(guest=g1, episode=e1, rating=5)
    a2 = Appearance(guest=g2, episode=e1, rating=4)
    a3 = Appearance(guest=g3, episode=e2, rating=5)
    db.session.add_all([a1, a2, a3])

    db.session.commit()
    print(" Done seeding!")
