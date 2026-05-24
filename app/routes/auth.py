from flask import Blueprint, request, jsonify, render_template

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from flask_jwt_extended import create_access_token

from app.models.user import db, User


auth = Blueprint('auth', __name__)


# =========================
# REGISTER PAGE
# =========================

@auth.route("/register", methods=["GET"])
def register_page():

    return render_template("register.html")


# =========================
# LOGIN PAGE
# =========================

@auth.route("/login", methods=["GET"])
def login_page():

    return render_template("login.html")


# =========================
# REGISTER API
# =========================

@auth.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    # Validation
    if not username or not password:

        return jsonify({
            "error": "Username and password required"
        }), 400

    # Check existing user
    existing_user = User.query.filter_by(
        username=username
    ).first()

    if existing_user:

        return jsonify({
            "error": "Username already exists"
        }), 409

    # Hash password
    hashed_password = generate_password_hash(password)

    # Create user object
    new_user = User(
        username=username,
        password=hashed_password
    )

    # Save to database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "message": "User registered successfully"
    }), 201


# =========================
# LOGIN API
# =========================

@auth.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    # Find user
    user = User.query.filter_by(
        username=username
    ).first()

    if not user:

        return jsonify({
            "error": "User not found"
        }), 404

    # Verify password
    if not check_password_hash(
        user.password,
        password
    ):

        return jsonify({
            "error": "Invalid password"
        }), 401

    # Generate JWT token
    access_token = create_access_token(
        identity=username
    )

    return jsonify({
        "message": "Login successful",
        "access_token": access_token
    }), 200