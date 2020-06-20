##########################################################################
# Name:     Users
# Purpose: File contains User details of all the members in the Org
#
# Author:     Siva Samudrala
#
# Created:   29/06/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2018 - Present
# Licence:   <your licence>
##########################################################################
from main import db
from datetime import datetime

class Alert(db.Model):
    __tablename__ = 'alert'

    alertID = db.Column(db.Integer, primary_key=True)
    itemID = db.Column(db.Integer, nullable=False)
    userID = db.Column(db.Integer, nullable=False)
    usertypeID = db.Column(db.Integer, nullable=False)
    itemname = db.Column(db.String(128), nullable=False)