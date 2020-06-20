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

class Income(db.Model):
    __tablename__ = 'income'

    incomeID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    date = db.Column(db.Date, nullable=False)
    incomeday = db.Column(db.String(11), nullable=False)
    incomemonth = db.Column(db.String(11), nullable=False)
    incomeyear = db.Column(db.String(4), nullable=False)
    amount = db.Column(db.Float(asdecimal=True), nullable=False)
    file = db.Column(db.String(200), nullable=False)
    note = db.Column(db.Text, nullable=False)
    schoolyearID = db.Column(db.Integer, nullable=False)
    create_date = db.Column(db.Date, nullable=False)
    userID = db.Column(db.Integer, nullable=False)
    usertypeID = db.Column(db.Integer, nullable=False)


class ManageSalary(db.Model):
    __tablename__ = 'manage_salary'

    manage_salaryID = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, nullable=False)
    usertypeID = db.Column(db.Integer, nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    template = db.Column(db.Integer, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    modify_date = db.Column(db.DateTime, nullable=False)
    create_userID = db.Column(db.Integer, nullable=False)
    create_username = db.Column(db.String(60), nullable=False)
    create_usertype = db.Column(db.String(60), nullable=False)

class SalaryOption(db.Model):
    __tablename__ = 'salary_option'

    salary_optionID = db.Column(db.Integer, primary_key=True)
    salary_templateID = db.Column(db.Integer, nullable=False)
    option_type = db.Column(db.Integer, nullable=False, comment=u'Allowances =1, Dllowances = 2, Increment = 3')
    label_name = db.Column(db.String(128))
    label_amount = db.Column(db.Float(asdecimal=True), nullable=False)


class SalaryTemplate(db.Model):
    __tablename__ = 'salary_template'

    salary_templateID = db.Column(db.Integer, primary_key=True)
    salary_grades = db.Column(db.String(128), nullable=False)
    basic_salary = db.Column(db.Text, nullable=False)
    overtime_rate = db.Column(db.Text, nullable=False)