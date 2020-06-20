from flask import Blueprint
from services.salaries.models import *

salaries = Blueprint("salaries", __name__)