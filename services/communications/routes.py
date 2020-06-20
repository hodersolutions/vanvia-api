from flask import Blueprint
from services.communications.models import *

communications = Blueprint("communications", __name__)