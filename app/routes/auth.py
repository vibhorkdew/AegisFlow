from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user import db, User
from flask_jwt_extended import create_access_token

auth = Blueprint('auth', __name__)


@auth.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({
            "error": "Username and password required"
        }), 400

    existing_user = User.query.filter_by(username=username).first()

    if existing_user:
        return jsonify({
            "error": "Username already exists"
        }), 409

    hashed_password = generate_password_hash(password)

    new_user = User(
        username=username,
        password=hashed_password
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "message": "User registered successfully"
    }), 201


@auth.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()

    if not user:
        return jsonify({
            "error": "User not found"
        }), 404

    if not check_password_hash(user.password, password):
        return jsonify({
            "error": "Invalid password"
        }), 401

    access_token = create_access_token(identity=username)

    return jsonify({
        "message": "Login successful",
        "access_token": access_token
    }), 200