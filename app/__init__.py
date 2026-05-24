from flask import Flask, render_template
from flask_jwt_extended import JWTManager

from app.models.user import db
from app.routes.auth import auth
from app.routes.dashboard import dashboard


def create_app():

    app = Flask(__name__)

    # =========================
    # DATABASE CONFIG
    # =========================

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aegisflow.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # =========================
    # JWT CONFIG
    # =========================

    app.config['JWT_SECRET_KEY'] = 'super-secret-key'

    # =========================
    # INITIALIZE EXTENSIONS
    # =========================

    db.init_app(app)

    jwt = JWTManager(app)

    # =========================
    # REGISTER BLUEPRINTS
    # =========================

    app.register_blueprint(auth)
    app.register_blueprint(dashboard)

    # =========================
    # HOME ROUTE
    # =========================

    @app.route("/")
    def home():

        return render_template("index.html")

    # =========================
    # CREATE DATABASE TABLES
    # =========================

    with app.app_context():
        db.create_all()

    return app