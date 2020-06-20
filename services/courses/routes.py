from flask import Blueprint
from services.courses.models import *

courses = Blueprint("courses", __name__)