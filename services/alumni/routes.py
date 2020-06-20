from flask import Blueprint
from services.alumni.models import *

alumni = Blueprint("alumni", __name__)