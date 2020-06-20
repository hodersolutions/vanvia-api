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

class ConversationMessageInfo(db.Model):
    __tablename__ = 'conversation_message_info'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Integer)
    draft = db.Column(db.Integer)
    fav_status = db.Column(db.Integer)
    create_date = db.Column(db.DateTime, nullable=False)
    modify_date = db.Column(db.DateTime, nullable=False)


class ConversationMsg(db.Model):
    __tablename__ = 'conversation_msg'

    msg_id = db.Column(db.Integer, primary_key=True)
    conversation_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    subject = db.Column(db.String(255))
    msg = db.Column(db.Text, nullable=False)
    attach = db.Column(db.Text)
    attach_file_name = db.Column(db.Text)
    usertypeID = db.Column(db.Integer, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    modify_date = db.Column(db.DateTime, nullable=False)
    start = db.Column(db.Integer)




class Complain(db.Model):
    __tablename__ = 'complain'

    complainID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    usertypeID = db.Column(db.Integer, nullable=False)
    userID = db.Column(db.Integer)
    schoolyearID = db.Column(db.Integer)
    description = db.Column(db.Text)
    attachment = db.Column(db.Text)
    originalfile = db.Column(db.Text)
    create_userID = db.Column(db.Integer, nullable=False)
    create_usertypeID = db.Column(db.Integer, nullable=False)
    create_date = db.Column(db.DateTime)
    modify_date = db.Column(db.DateTime)