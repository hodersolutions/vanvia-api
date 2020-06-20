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

class Mark(db.Model):
    __tablename__ = 'mark'

    markID = db.Column(db.Integer, primary_key=True)
    schoolyearID = db.Column(db.Integer, nullable=False)
    examID = db.Column(db.Integer, nullable=False)
    exam = db.Column(db.String(60), nullable=False)
    studentID = db.Column(db.Integer, nullable=False)
    classesID = db.Column(db.Integer, nullable=False)
    subjectID = db.Column(db.Integer, nullable=False)
    subject = db.Column(db.String(60), nullable=False)
    year = db.Column(db.String(4), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    create_userID = db.Column(db.Integer, nullable=False)
    create_usertypeID = db.Column(db.Integer, nullable=False)


class Markpercentage(db.Model):
    __tablename__ = 'markpercentage'

    markpercentageID = db.Column(db.Integer, primary_key=True)
    markpercentagetype = db.Column(db.String(100), nullable=False)
    percentage = db.Column(db.Float(asdecimal=True), nullable=False)
    examID = db.Column(db.Integer)
    classesID = db.Column(db.Integer)
    subjectID = db.Column(db.Integer)
    create_date = db.Column(db.DateTime, nullable=False)
    modify_date = db.Column(db.DateTime, nullable=False)
    create_userID = db.Column(db.Integer, nullable=False)
    create_username = db.Column(db.String(60), nullable=False)
    create_usertype = db.Column(db.String(60), nullable=False)


class Markrelation(db.Model):
    __tablename__ = 'markrelation'

    markrelationID = db.Column(db.Integer, primary_key=True)
    markID = db.Column(db.Integer, nullable=False)
    markpercentageID = db.Column(db.Integer, nullable=False)
    mark = db.Column(db.String(128))