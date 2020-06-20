from flask import Blueprint
from services.surveys.models import *

surveys = Blueprint("surveys", __name__)