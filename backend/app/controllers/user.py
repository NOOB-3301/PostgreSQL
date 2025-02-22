from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.user import User
from . import api_bp

@api_bp.route('/user/profile', methods=['GET'])
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return jsonify({
        'username': user.username,
        'email': user.email
    })
