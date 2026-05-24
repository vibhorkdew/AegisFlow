from flask import Flask
from flask_jwt_extended import JWTManager

from app.models.user import db
from app.routes.auth import auth
from app.routes.dashboard import dashboard

def create_app():

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aegisflow.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'super-secret-key'

    db.init_app(app)

    jwt = JWTManager(app)

    app.register_blueprint(auth)
    app.register_blueprint(dashboard)
    @app.route("/")
    def home():
        return "Welcome to AegisFlow - Secure DevSecOps Pipeline"

    with app.app_context():
        db.create_all()

    return app