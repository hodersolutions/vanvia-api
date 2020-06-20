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

class Event(db.Model):
    __tablename__ = 'event'

    eventID = db.Column(db.Integer, primary_key=True)
    fdate = db.Column(db.Date, nullable=False)
    ftime = db.Column(db.Time, nullable=False)
    tdate = db.Column(db.Date, nullable=False)
    ttime = db.Column(db.Time, nullable=False)
    title = db.Column(db.String(128), nullable=False)
    details = db.Column(db.Text, nullable=False)
    photo = db.Column(db.String(200))
    create_date = db.Column(db.DateTime, nullable=False)
    schoolyearID = db.Column(db.Integer, nullable=False)
    create_userID = db.Column(db.Integer, nullable=False)
    create_usertypeID = db.Column(db.Integer, nullable=False)


class Eventcounter(db.Model):
    __tablename__ = 'eventcounter'

    eventcounterID = db.Column(db.Integer, primary_key=True)
    eventID = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(40), nullable=False)
    type = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    photo = db.Column(db.String(200))
    status = db.Column(db.Integer, nullable=False)
    create_date = db.Column(db.TIMESTAMP, nullable=False, default=datetime.now())