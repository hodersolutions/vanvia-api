from flask import Blueprint
from services.leaves.models import *

leaves = Blueprint("leaves", __name__)