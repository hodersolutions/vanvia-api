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

class Asset(db.Model):
    __tablename__ = 'asset'

    assetID = db.Column(db.Integer, primary_key=True)
    serial = db.Column(db.String(255))
    description = db.Column(db.Text, comment=u'Title')
    manufacturer = db.Column(db.String(255))
    brand = db.Column(db.String(255))
    asset_number = db.Column(db.String(255))
    status = db.Column(db.Integer)
    asset_condition = db.Column(db.Integer)
    attachment = db.Column(db.Text)
    originalfile = db.Column(db.Text)
    asset_categoryID = db.Column(db.Integer)
    asset_locationID = db.Column(db.Integer)
    create_date = db.Column(db.Date, nullable=False)
    modify_date = db.Column(db.Date, nullable=False)
    create_userID = db.Column(db.Integer, nullable=False)
    create_usertypeID = db.Column(db.Integer, nullable=False)


class AssetAssignment(db.Model):
    __tablename__ = 'asset_assignment'

    asset_assignmentID = db.Column(db.Integer, primary_key=True)
    assetID = db.Column(db.Integer, nullable=False, comment=u'Description and title')
    usertypeID = db.Column(db.Integer)
    check_out_to = db.Column(db.Integer, nullable=False)
    due_date = db.Column(db.Date)
    note = db.Column(db.Text)
    assigned_quantity = db.Column(db.Integer)
    status = db.Column(db.Integer)
    asset_locationID = db.Column(db.Integer)
    check_out_date = db.Column(db.Date)
    check_in_date = db.Column(db.Date)
    create_date = db.Column(db.Date, nullable=False)
    modify_date = db.Column(db.Date, nullable=False)
    create_userID = db.Column(db.Integer, nullable=False)
    create_usertypeID = db.Column(db.Integer, nullable=False)


class AssetCategory(db.Model):
    __tablename__ = 'asset_category'

    asset_categoryID = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255), nullable=False)
    create_date = db.Column(db.Date, nullable=False)
    modify_date = db.Column(db.Date, nullable=False)
    create_userID = db.Column(db.Integer, nullable=False)
    create_usertypeID = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Integer, nullable=False)