from flask import Blueprint
from services.assignments.models import *

assignments = Blueprint("assignments", __name__)