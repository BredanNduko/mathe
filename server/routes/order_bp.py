from flask import Blueprint, jsonify
from flask_restful import Api, reqparse, Resource, abort
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt

from models import User, db

from serializers import OrderSchema

order_bp = Blueprint('order_bp', __name__)
ma = Marshmallow(order_bp)
bcrypt = Bcrypt()
api = Api(order_bp)