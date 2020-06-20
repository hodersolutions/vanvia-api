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

class Exam(db.Model):
    __tablename__ = 'exam'

    examID = db.Column(db.Integer, primary_key=True)
    exam = db.Column(db.String(60), nullable=False)
    date = db.Column(db.Date, nullable=False)
    note = db.Column(db.Text)


class Examschedule(db.Model):
    __tablename__ = 'examschedule'

    examscheduleID = db.Column(db.Integer, primary_key=True)
    examID = db.Column(db.Integer, nullable=False)
    classesID = db.Column(db.Integer, nullable=False)
    sectionID = db.Column(db.Integer, nullable=False)
    subjectID = db.Column(db.Integer, nullable=False)
    edate = db.Column(db.Date, nullable=False)
    examfrom = db.Column(db.String(10), nullable=False)
    examto = db.Column(db.String(10), nullable=False)
    room = db.Column(db.Text)
    schoolyearID = db.Column(db.Integer, nullable=False)


class OnlineExam(db.Model):
    __tablename__ = 'online_exam'

    onlineExamID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(512), nullable=False)
    description = db.Column(db.Text)
    classID = db.Column(db.Integer)
    sectionID = db.Column(db.Integer)
    studentGroupID = db.Column(db.Integer)
    subjectID = db.Column(db.Integer)
    userTypeID = db.Column(db.Integer)
    instructionID = db.Column(db.Integer)
    examStatus = db.Column(db.String(11), nullable=False)
    schoolYearID = db.Column(db.Integer, nullable=False)
    examTypeNumber = db.Column(db.Integer)
    startDateTime = db.Column(db.DateTime)
    endDateTime = db.Column(db.DateTime)
    duration = db.Column(db.Integer)
    random = db.Column(db.Integer)
    public = db.Column(db.Integer)
    status = db.Column(db.Integer, default="1")
    markType = db.Column(db.Integer, nullable=False)
    negativeMark = db.Column(db.Integer)
    bonusMark = db.Column(db.Integer)
    point = db.Column(db.Integer)
    percentage = db.Column(db.Integer)
    showMarkAfterExam = db.Column(db.Integer)
    judge = db.Column(db.Integer, default="1", comment=u'Auto Judge = 1, Manually Judge = 0')
    paid = db.Column(db.Integer, comment=u'0 = Unpaid, 1 = Paid')
    validDays = db.Column(db.Integer)
    cost = db.Column(db.Integer)
    img = db.Column(db.String(512))
    create_date = db.Column(db.DateTime, nullable=False)
    modify_date = db.Column(db.DateTime, nullable=False)
    create_userID = db.Column(db.Integer, nullable=False)
    create_usertypeID = db.Column(db.Integer, nullable=False)
    published = db.Column(db.Integer, nullable=False)


class OnlineExamQuestion(db.Model):
    __tablename__ = 'online_exam_question'

    onlineExamQuestionID = db.Column(db.Integer, primary_key=True)
    onlineExamID = db.Column(db.Integer, nullable=False)
    questionID = db.Column(db.Integer)


class OnlineExamType(db.Model):
    __tablename__ = 'online_exam_type'

    onlineExamTypeID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(512))
    examTypeNumber = db.Column(db.Integer)
    status = db.Column(db.Integer, default="1")


class OnlineExamUserAnswer(db.Model):
    __tablename__ = 'online_exam_user_answer'

    onlineExamUserAnswerID = db.Column(db.Integer, primary_key=True)
    onlineExamQuestionID = db.Column(db.Integer, nullable=False)
    onlineExamRegisteredUserID = db.Column(db.Integer)
    userID = db.Column(db.Integer)


class OnlineExamUserAnswerOption(db.Model):
    __tablename__ = 'online_exam_user_answer_option'

    onlineExamUserAnswerOptionID = db.Column(db.Integer, primary_key=True)
    questionID = db.Column(db.Integer, nullable=False)
    optionID = db.Column(db.Integer)
    typeID = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text)
    time = db.Column(db.DateTime, nullable=False)


class OnlineExamUserStatu(db.Model):
    __tablename__ = 'online_exam_user_status'

    onlineExamUserStatus = db.Column(db.Integer, primary_key=True)
    onlineExamID = db.Column(db.Integer, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    totalQuestion = db.Column(db.Integer, nullable=False)
    totalAnswer = db.Column(db.Integer, nullable=False)
    nagetiveMark = db.Column(db.Integer, nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    userID = db.Column(db.Integer, nullable=False)
    classesID = db.Column(db.Integer)
    sectionID = db.Column(db.Integer)
    examtimeID = db.Column(db.Integer)
    totalCurrectAnswer = db.Column(db.Integer)
    totalMark = db.Column(db.String(40))
    totalObtainedMark = db.Column(db.Integer)
    totalPercentage = db.Column(db.Float(asdecimal=True))
    statusID = db.Column(db.Integer)


class Onlineadmission(db.Model):
    __tablename__ = 'onlineadmission'

    onlineadmissionID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    dob = db.Column(db.Date)
    sex = db.Column(db.String(10))
    religion = db.Column(db.String(25))
    email = db.Column(db.String(40))
    phone = db.Column(db.Text)
    address = db.Column(db.String(200))
    classesID = db.Column(db.Integer)
    bloodgroup = db.Column(db.String(5))
    country = db.Column(db.String(128))
    photo = db.Column(db.String(200))
    schoolyearID = db.Column(db.Integer)
    create_date = db.Column(db.DateTime)
    modify_date = db.Column(db.DateTime)
    studentID = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, comment=u'0 = New, 1=Approved, 2 = Waiting, 3 = Declined')
