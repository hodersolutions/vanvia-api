from flask import Blueprint
from services.galleries.models import *

galleries = Blueprint("galleries", __name__)