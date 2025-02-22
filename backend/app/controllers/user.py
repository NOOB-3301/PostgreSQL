from flask import jsonify, request  # Import request to access headers
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.user import User
from . import api_bp

@api_bp.route('/user/profile', methods=['GET'])
@jwt_required()
def profile():
    print("profile hit")
    # Print incoming headers to the console
    print("Incoming Headers:", request.headers)

    # You can also return the headers in the response for testing
    incoming_headers = dict(request.headers)

    # Continue with your usual logic
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    return jsonify({
        'headers': incoming_headers,  # This will show all headers sent
        'username': user.username,
        'email': user.email
    })
