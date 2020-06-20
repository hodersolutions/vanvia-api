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

class QuestionAnswer(db.Model):
    __tablename__ = 'question_answer'

    answerID = db.Column(db.Integer, primary_key=True)
    questionID = db.Column(db.Integer, nullable=False)
    optionID = db.Column(db.Integer)
    typeNumber = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text)


class QuestionBank(db.Model):
    __tablename__ = 'question_bank'

    questionBankID = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    explanation = db.Column(db.Text)
    levelID = db.Column(db.Integer)
    groupID = db.Column(db.Integer)
    totalQuestion = db.Column(db.Integer)
    totalOption = db.Column(db.Integer)
    typeNumber = db.Column(db.Integer)
    parentID = db.Column(db.Integer)
    time = db.Column(db.Integer)
    mark = db.Column(db.Integer)
    hints = db.Column(db.Text)
    upload = db.Column(db.String(512))
    subjectID = db.Column(db.Integer)
    create_date = db.Column(db.DateTime, nullable=False)
    modify_date = db.Column(db.DateTime, nullable=False)
    create_userID = db.Column(db.Integer, nullable=False)
    create_usertypeID = db.Column(db.Integer, nullable=False)


class QuestionGroup(db.Model):
    __tablename__ = 'question_group'

    questionGroupID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)


class QuestionLevel(db.Model):
    __tablename__ = 'question_level'

    questionLevelID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)


class QuestionOption(db.Model):
    __tablename__ = 'question_option'

    optionID = db.Column(db.Integer, primary_key=True)
    questionID = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(512), nullable=False)
    img = db.Column(db.String(512))


class QuestionType(db.Model):
    __tablename__ = 'question_type'

    questionTypeID = db.Column(db.Integer, primary_key=True)
    typeNumber = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(512), nullable=False)
