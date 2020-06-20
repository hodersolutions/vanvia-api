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

class Mailandsm(db.Model):
    __tablename__ = 'mailandsms'

    mailandsmsID = db.Column(db.Integer, primary_key=True)
    usertypeID = db.Column(db.Integer, nullable=False)
    users = db.Column(db.Text, nullable=False)
    type = db.Column(db.String(16), nullable=False)
    senderusertypeID = db.Column(db.Integer, nullable=False)
    senderID = db.Column(db.Integer, nullable=False)
    message = db.Column(db.Text, nullable=False)
    create_date = db.Column(db.TIMESTAMP, nullable=False, default=datetime.now())
    year = db.Column(db.String(4), nullable=False)


class Mailandsmstemplate(db.Model):
    __tablename__ = 'mailandsmstemplate'

    mailandsmstemplateID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    usertypeID = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(10), nullable=False)
    template = db.Column(db.Text, nullable=False)
    create_date = db.Column(db.TIMESTAMP, nullable=False, default=datetime.now())


class Mailandsmstemplatetag(db.Model):
    __tablename__ = 'mailandsmstemplatetag'

    mailandsmstemplatetagID = db.Column(db.Integer, primary_key=True)
    usertypeID = db.Column(db.Integer, nullable=False)
    tagname = db.Column(db.String(128), nullable=False)
    mailandsmstemplatetag_extra = db.Column(db.String(255))
    create_date = db.Column(db.TIMESTAMP, nullable=False, default=datetime.now())

class Smssetting(db.Model):
    __tablename__ = 'smssettings'

    smssettingsID = db.Column(db.Integer, primary_key=True)
    types = db.Column(db.String(255))
    field_names = db.Column(db.String(255))
    field_values = db.Column(db.String(255))
    smssettings_extra = db.Column(db.String(255))