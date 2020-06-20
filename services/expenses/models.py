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

class Expense(db.Model):
    __tablename__ = 'expense'

    expenseID = db.Column(db.Integer, primary_key=True)
    create_date = db.Column(db.Date, nullable=False)
    date = db.Column(db.Date, nullable=False)
    expenseday = db.Column(db.String(11), nullable=False)
    expensemonth = db.Column(db.String(11), nullable=False)
    expenseyear = db.Column(db.String(4), nullable=False)
    expense = db.Column(db.String(128), nullable=False)
    amount = db.Column(db.Float(asdecimal=True), nullable=False)
    file = db.Column(db.String(200))
    userID = db.Column(db.Integer, nullable=False)
    usertypeID = db.Column(db.Integer, nullable=False)
    uname = db.Column(db.String(60), nullable=False)
    schoolyearID = db.Column(db.Integer, nullable=False)
    note = db.Column(db.Text)