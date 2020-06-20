from flask import Blueprint
from services.conversations.models import *

conversations = Blueprint("conversations", __name__)