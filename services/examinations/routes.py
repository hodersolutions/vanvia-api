from flask import Blueprint
from services.examinations.models import *

examinations = Blueprint("examinations", __name__)