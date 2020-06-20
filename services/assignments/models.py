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

class Assignment(db.Model):
    __tablename__ = 'assignment'

    assignmentID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)
    deadlinedate = db.Column(db.Date, nullable=False)
    usertypeID = db.Column(db.Integer, nullable=False)
    userID = db.Column(db.Integer, nullable=False)
    originalfile = db.Column(db.Text, nullable=False)
    file = db.Column(db.Text, nullable=False)
    classesID = db.Column(db.Text, nullable=False)
    schoolyearID = db.Column(db.Integer, nullable=False)
    sectionID = db.Column(db.Text)
    subjectID = db.Column(db.Text)
    assignusertypeID = db.Column(db.Integer)
    assignuserID = db.Column(db.Integer)


class Assignmentanswer(db.Model):
    __tablename__ = 'assignmentanswer'

    assignmentanswerID = db.Column(db.Integer, primary_key=True)
    assignmentID = db.Column(db.Integer, nullable=False)
    schoolyearID = db.Column(db.Integer, nullable=False)
    uploaderID = db.Column(db.Integer, nullable=False)
    uploadertypeID = db.Column(db.Integer, nullable=False)
    answerfile = db.Column(db.Text, nullable=False)
    answerfileoriginal = db.Column(db.Text, nullable=False)
    answerdate = db.Column(db.Date, nullable=False)