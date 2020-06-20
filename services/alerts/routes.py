from flask import Blueprint
from services.alerts.models import *

alerts = Blueprint("alerts", __name__)