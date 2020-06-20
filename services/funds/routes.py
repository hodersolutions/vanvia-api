from flask import Blueprint
from services.funds.models import *

funds = Blueprint("funds", __name__)