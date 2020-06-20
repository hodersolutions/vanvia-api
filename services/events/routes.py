from flask import Blueprint
from services.events.models import *

events = Blueprint("events", __name__)