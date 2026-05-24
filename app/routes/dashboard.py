from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

dashboard = Blueprint('dashboard', __name__)

@dashboard.route("/dashboard", methods=["GET"])
@jwt_required()
def protected_dashboard():

    current_user = get_jwt_identity()

    return jsonify({
        "message": f"Welcome {current_user} to AegisFlow Dashboard"
    }), 200
