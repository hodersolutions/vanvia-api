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

class Feetype(db.Model):
    __tablename__ = 'feetypes'

    feetypesID = db.Column(db.Integer, primary_key=True)
    feetypes = db.Column(db.String(60), nullable=False)
    note = db.Column(db.Text)