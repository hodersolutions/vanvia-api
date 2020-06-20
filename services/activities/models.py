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

class Activity(db.Model):
    __tablename__ = 'activities'

    activitiesID = db.Column(db.Integer, primary_key=True)
    activitiescategoryID = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    modify_date = db.Column(db.DateTime, nullable=False)
    time_to = db.Column(db.String(40))
    time_from = db.Column(db.String(40))
    time_at = db.Column(db.String(40))
    usertypeID = db.Column(db.Integer, nullable=False)
    userID = db.Column(db.Integer, nullable=False)
    schoolyearID = db.Column(db.Integer, nullable=False)


class Activitiescategory(db.Model):
    __tablename__ = 'activitiescategory'

    activitiescategoryID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    fa_icon = db.Column(db.String(40))
    schoolyearID = db.Column(db.Integer, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    modify_date = db.Column(db.DateTime, nullable=False)
    userID = db.Column(db.Integer, nullable=False)
    usertypeID = db.Column(db.Integer, nullable=False)


class Activitiescomment(db.Model):
    __tablename__ = 'activitiescomment'

    activitiescommentID = db.Column(db.Integer, primary_key=True)
    activitiesID = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=False)
    schoolyearID = db.Column(db.Integer, nullable=False)
    userID = db.Column(db.Integer, nullable=False)
    usertypeID = db.Column(db.Integer, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)


class Activitiesmedia(db.Model):
    __tablename__ = 'activitiesmedia'

    activitiesmediaID = db.Column(db.Integer, primary_key=True)
    activitiesID = db.Column(db.Integer, nullable=False)
    attachment = db.Column(db.Text, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)


class Activitiesstudent(db.Model):
    __tablename__ = 'activitiesstudent'

    activitiesstudentID = db.Column(db.Integer, primary_key=True)
    activitiesID = db.Column(db.Integer, nullable=False)
    studentID = db.Column(db.Integer, nullable=False)
    classesID = db.Column(db.Integer, nullable=False)