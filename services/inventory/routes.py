from flask import Blueprint
from services.inventory.models import *

inventory = Blueprint("inventory", __name__)