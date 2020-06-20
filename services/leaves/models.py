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

class Leaveapplication(db.Model):
    __tablename__ = 'leaveapplications'

    leaveapplicationID = db.Column(db.Integer, primary_key=True)
    leavecategoryID = db.Column(db.Integer, nullable=False, index=True)
    apply_date = db.Column(db.TIMESTAMP, nullable=False, default=datetime.now())
    od_status = db.Column(db.Integer, nullable=False)
    from_date = db.Column(db.Date, nullable=False, index=True)
    from_time = db.Column(db.Time)
    to_date = db.Column(db.Date, nullable=False, index=True)
    to_time = db.Column(db.Time)
    leave_days = db.Column(db.Integer, nullable=False)
    reason = db.Column(db.Text)
    attachment = db.Column(db.String(200))
    attachmentorginalname = db.Column(db.String(200))
    create_date = db.Column(db.DateTime, nullable=False)
    modify_date = db.Column(db.DateTime, nullable=False)
    create_userID = db.Column(db.Integer, nullable=False)
    create_usertypeID = db.Column(db.Integer, nullable=False)
    applicationto_userID = db.Column(db.Integer, index=True)
    applicationto_usertypeID = db.Column(db.Integer, index=True)
    approver_userID = db.Column(db.Integer, index=True)
    approver_usertypeID = db.Column(db.Integer, index=True)
    status = db.Column(db.Integer)
    schoolyearID = db.Column(db.Integer, nullable=False)


class Leaveassign(db.Model):
    __tablename__ = 'leaveassign'

    leaveassignID = db.Column(db.Integer, primary_key=True)
    leavecategoryID = db.Column(db.Integer, nullable=False, index=True)
    usertypeID = db.Column(db.Integer, nullable=False, index=True)
    leaveassignday = db.Column(db.Integer, nullable=False)
    schoolyearID = db.Column(db.Integer, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    modify_date = db.Column(db.DateTime, nullable=False)
    create_userID = db.Column(db.Integer, nullable=False)
    create_usertypeID = db.Column(db.Integer, nullable=False)


class Leavecategory(db.Model):
    __tablename__ = 'leavecategory'

    leavecategoryID = db.Column(db.Integer, primary_key=True)
    leavecategory = db.Column(db.String(255), nullable=False)
    leavegender = db.Column(db.Integer, comment=u'1 = General, 2 = Male, 3 = Femele')
    create_date = db.Column(db.DateTime, nullable=False)
    modify_date = db.Column(db.DateTime, nullable=False)
    create_userID = db.Column(db.Integer, nullable=False)
    create_usertypeID = db.Column(db.Integer, nullable=False)