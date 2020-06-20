from flask import Blueprint
from services.moms.models import *

moms = Blueprint("moms", __name__)