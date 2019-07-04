##########################################################################
# Name:     Users Routes
# Purpose: File contains User request endpoints like register, login, logout etc.
#
# Author:     Siva Samudrala
#
# Created:   29/06/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2018 - Present
# Licence:   <your licence>
##########################################################################
from flask import Blueprint
from flask import Response, request
from json import dumps
from decorators import validate
from models.users import Users
from flask_jwt_extended import (create_refresh_token, jwt_refresh_token_required)


users = Blueprint('users', __name__)


@users.route('/register', methods=["POST"])
@validate.login
def register():
    request_data = request.get_json()
    if "email" in request_data:
        user = Users.get_user_by_email(request_data["email"])
        if user:
            result = {
                'status': 'success',
                'message': 'User Already exists with the email.',
                'user': user
            }
            response = Response(dumps(result), 200, mimetype='application/json')
            return response

    new_user = Users()
    if "email" in request_data:
        new_user.email = request_data["email"]
    if "password" in request_data:
        new_user.password = request_data["password"]
    if "mobile" in request_data:
        new_user.mobile = request_data["mobile"]

    # role = request_data["role"]
    # success, error = users.Users.add_user(new_user, role)
    success, error = Users.add_user(new_user)
    response = None
    if success:
        result = {
            'status': 'success',
            'message': 'Successfully registered.',
            'user': success
        }
        response = Response(dumps(result), 201, mimetype='application/json')
    if error:
        result = {
            'status': 'failure',
            'message': 'Successfully registered.',
            'user': {'msg': str(error)}
        }
        response = Response(dumps(result), 501, mimetype='application/json')

    return response


@users.route('/login', methods=["POST"])
@validate.login
def login():
    request_data = request.get_json()
    if "email" in request_data:
        user = Users.query.filter_by(email=request_data["email"]).first()
        if user and user.verify_hash(request_data['password'], user.password):
            access_token = create_refresh_token(identity=user.email)
            result = {
                'status': 'success',
                'message': 'User logged in.',
                'user': user.serialize(),
                'access_token': access_token
            }
            response = Response(dumps(result), 200, mimetype='application/json')
            return response
    result = {
        "status": "failure",
        "message": "Failed to Login"
    }
    return Response(dumps(result), 401, mimetype="application/json")


@users.route('/logout', methods=["POST"])
@jwt_refresh_token_required
def logout():
    result = {
        "status": "success",
        "message": "User logged out."
    }
    return Response(dumps(result), 201, mimetype="application/json")