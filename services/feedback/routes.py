from flask import Blueprint
from services.feedback.models import *

feedback = Blueprint("feedback", __name__)