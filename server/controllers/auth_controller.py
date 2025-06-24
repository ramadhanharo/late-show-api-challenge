from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

from server.models import db
from server.models.user import User

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        abort(400, description="Username and password required")

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        abort(409, description="Username already exists")

    hashed_password = generate_password_hash(password)

    new_user = User(username=username, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        abort(400, description="Username and password required")

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password_hash, password):
        abort(401, description="Invalid credentials")

    access_token = create_access_token(identity=user.id)
    return jsonify({"access_token": access_token}), 200
