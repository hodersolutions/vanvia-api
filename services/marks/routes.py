from flask import Blueprint
from services.marks.models import *

marks = Blueprint("marks", __name__)