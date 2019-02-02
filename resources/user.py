import sqlite3

from flask_restful import Resource, reqparse

from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True, help="this field must not be blank")
    parser.add_argument("password", type=str, required=True, help="this field must not be blank")
    def post(self):
        data = UserRegister.parser.parse_args()
        
        if (UserModel.find_by_username(data['username'])==None):
            user = UserModel(**data)
            user.save_to_db()
            return {"message": "User created successfully."},201
        else:
            return {"message": "Username already exists."}, 400
