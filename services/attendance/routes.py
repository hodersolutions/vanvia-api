from flask import Blueprint
from services.attendance.models import *

attendance = Blueprint("attendance", __name__)