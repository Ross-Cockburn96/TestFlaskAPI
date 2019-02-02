
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity
from resources.user import UserRegister
from security import authenticate, identity
from resources.item import Item, ItemList
from resources.store import Store, StoreList



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'Ross'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)

items = []
sales = []



class Sale(Resource):
    parser2 = reqparse.RequestParser()
    parser2.add_argument('item', type=str, required = True, help ="this sale field cannot be left blank")
    parser2.add_argument('price', type=int, required = True, help ="this sale field cannot be left blank")

    def get(self, name):
        print("hello this is a test")
        return{"sale" : sales}

    def post(self, name):
        request_data = Sale.parser2.parse_args()
        for key, val in request_data.items():
            print(key)
            print(val)
        sale = {"name" : name, "price" : request_data["price"], "item": request_data['item'] }
        sales.append(sale)
        return sale, 201

api.add_resource(Sale, "/sale/<string:name>")
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")
api.add_resource(Store, "/store/<string:name>")
api.add_resource(StoreList, "/stores")

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)  # important to mention debug=True
