from flask import Blueprint
from services.newsletters.models import *

newsletters = Blueprint("newsletters", __name__)