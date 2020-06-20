from flask import Blueprint
from services.questionbank.models import *

questionbank = Blueprint("questionbank", __name__)