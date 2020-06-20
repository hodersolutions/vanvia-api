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

class Attendance(db.Model):
    __tablename__ = 'attendance'

    attendanceID = db.Column(db.Integer, primary_key=True)
    schoolyearID = db.Column(db.Integer, nullable=False)
    studentID = db.Column(db.Integer, nullable=False)
    classesID = db.Column(db.Integer, nullable=False)
    sectionID = db.Column(db.Integer, nullable=False)
    userID = db.Column(db.Integer, nullable=False)
    usertype = db.Column(db.String(60), nullable=False)
    monthyear = db.Column(db.String(10), nullable=False)
    a1 = db.Column(db.String(3))
    a2 = db.Column(db.String(3))
    a3 = db.Column(db.String(3))
    a4 = db.Column(db.String(3))
    a5 = db.Column(db.String(3))
    a6 = db.Column(db.String(3))
    a7 = db.Column(db.String(3))
    a8 = db.Column(db.String(3))
    a9 = db.Column(db.String(3))
    a10 = db.Column(db.String(3))
    a11 = db.Column(db.String(3))
    a12 = db.Column(db.String(3))
    a13 = db.Column(db.String(3))
    a14 = db.Column(db.String(3))
    a15 = db.Column(db.String(3))
    a16 = db.Column(db.String(3))
    a17 = db.Column(db.String(3))
    a18 = db.Column(db.String(3))
    a19 = db.Column(db.String(3))
    a20 = db.Column(db.String(3))
    a21 = db.Column(db.String(3))
    a22 = db.Column(db.String(3))
    a23 = db.Column(db.String(3))
    a24 = db.Column(db.String(3))
    a25 = db.Column(db.String(3))
    a26 = db.Column(db.String(3))
    a27 = db.Column(db.String(3))
    a28 = db.Column(db.String(3))
    a29 = db.Column(db.String(3))
    a30 = db.Column(db.String(3))
    a31 = db.Column(db.String(3))