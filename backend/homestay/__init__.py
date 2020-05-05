from os.path import join, dirname
from dotenv import load_dotenv

import os

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path, override=True)

# applications 
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_marshmallow  import Marshmallow

app = Flask(__name__)
# setting for cors 
from flask_cors import CORS

CORS(app)

ma = Marshmallow(app)
app.debug = True
app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
jwt = JWTManager(app)

# database 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
server = os.getenv('SERVER')
database_name = os.getenv('DATABASE_NAME')
secret_key = os.getenv('SECRET_KEY')

DATABSE_URI = 'mysql://{user}:{password}@{server}/{database}'.format(
    user=username, password=password, server='127.0.0.1', database=database_name)


app.config['SQLALCHEMY_DATABASE_URI'] = DATABSE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = secret_key

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# setting for pagination 
from flask_rest_paginate import Pagination

app.config['PAGINATE_PAGE_SIZE'] = 30
pagination = Pagination(app, db)

from homestay.models.models import RevokedTokenModel

# setting for api
# setting for enter access token in swagger UI
authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    },
}

from flask_restplus import Api
api = Api(app, version=1.0, title="Homestay Booking API",
          authorizations=authorizations, description="Manage all activity in website")

# run every time client try to access to secured endpoint
@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return RevokedTokenModel.is_jti_blacklisted(jti)

# this method to assign extra data to jwt token. Get by get_jwt_claims() method
# called whenever create_access_token() was used
@jwt.user_claims_loader
def add_claims_to_access_token(identity):
    return {
        'role': identity.role
    }

# this method to get back the id when use get_jwt_identity() method
# called whenever create_access_token() was used
@jwt.user_identity_loader
def identity_lookup(identity):
    return identity.id

from homestay import routes
# from api.rooms.rooms import app
# from api.comment import app
# from api.like import app
# from api.rooms.price import app
