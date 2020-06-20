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

class Ebook(db.Model):
    __tablename__ = 'ebooks'

    ebooksID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(255), nullable=False)
    author = db.Column(db.VARCHAR(255), nullable=False)
    classesID = db.Column(db.Integer, nullable=False)
    authority = db.Column(db.Integer, nullable=False)
    cover_photo = db.Column(db.VARCHAR(200), nullable=False)
    file = db.Column(db.VARCHAR(200), nullable=False)



class Document(db.Model):
    __tablename__ = 'document'

    documentID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.VARCHAR(128), nullable=False)
    file = db.Column(db.VARCHAR(200), nullable=False)
    userID = db.Column(db.Integer, nullable=False)
    usertypeID = db.Column(db.Integer, nullable=False)
    create_date = db.Column(db.TIMESTAMP, nullable=False, default=datetime.now())
    create_userID = db.Column(db.Integer, nullable=False)
    create_usertypeID = db.Column(db.Integer, nullable=False)
