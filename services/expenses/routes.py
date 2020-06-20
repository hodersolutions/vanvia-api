from flask import Blueprint
from services.expenses.models import *

expenses = Blueprint("expenses", __name__)