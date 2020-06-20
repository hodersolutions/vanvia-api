from flask import Blueprint
from services.fees.models import *

fees = Blueprint("fees", __name__)