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


class Fmenu(db.Model):
    __tablename__ = 'fmenu'

    fmenuID = db.Column(db.Integer, primary_key=True)
    menu_name = db.Column(db.String(128), nullable=False)
    status = db.Column(db.Integer, nullable=False, comment=u'Only for active')
    topbar = db.Column(db.Integer, nullable=False)
    social = db.Column(db.Integer, nullable=False)


class FmenuRelation(db.Model):
    __tablename__ = 'fmenu_relation'

    fmenu_relationID = db.Column(db.Integer, primary_key=True)
    fmenuID = db.Column(db.Integer)
    menu_typeID = db.Column(db.Integer, comment=u'1 => Pages, 2 => Post, 3 => Links')
    menu_parentID = db.Column(db.String(128))
    menu_orderID = db.Column(db.Integer)
    menu_pagesID = db.Column(db.Integer)
    menu_label = db.Column(db.String(254))
    menu_link = db.Column(db.Text, nullable=False)
    menu_rand = db.Column(db.String(128))
    menu_rand_parentID = db.Column(db.String(128))
    menu_status = db.Column(db.Integer)


class FrontendSetting(db.Model):
    __tablename__ = 'frontend_setting'

    fieldoption = db.Column(db.String(100), primary_key=True)
    value = db.Column(db.String(255), nullable=False)


class FrontendTemplate(db.Model):
    __tablename__ = 'frontend_template'

    frontend_templateID = db.Column(db.Integer, primary_key=True)
    template_name = db.Column(db.String(128), nullable=False)