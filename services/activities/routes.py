from flask import Blueprint
from services.activities.models import *

activities = Blueprint("activities", __name__)