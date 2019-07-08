##########################################################################
# Name:     Syllabus
# Purpose: File contains User details of all the members in the Org
#
# Author:     Sai Nikhita Guduru
#
# Created:   07/07/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2018 - Present
# Licence:   <your licence>
##########################################################################
from main import db
from json import loads


class Syllabus(db.Model):
    __tablename__ = "syllabus"
    __table_args__ = (
        db.UniqueConstraint('term', 'class_no', 'subject', name='unique_component_commit'),
    )
    # unique identifier for a user, todo: need to have uuid or mobile as unique identifier
    id = db.Column(db.Integer, primary_key=True)
    # Term of syllabus
    term = db.Column(db.String(200), nullable=False)
    # class number
    class_no = db.Column(db.Integer, nullable=False)
    # subject
    subject = db.Column(db.String(80), nullable=False)
    # json for syllabus details for each section
    syllabus_details = db.Column(db.String(2000), nullable=False)
    # status of syllabus completion
    syllabus_status = db.Column(db.String(2000), nullable=False)

    def __repr__(self):
        return "{ term: {1}, class_no: {2}, subject: {3}, syllabus_details: {4}, syllabus_status: {5} }".format(self.term, self.class_no, self.subject, self.syllabus_details, self.syllabus_status)

    @classmethod
    def add_syllabus(cls, _syllabus):
        try:
            db.session.add(_syllabus)
            db.session.commit()

        except Exception as e:
            return None, e

        return _syllabus

    @classmethod
    def get_whole_syllabus(cls):
        return [syllabus.serialize() for syllabus in cls.query.all()]
        
    @classmethod
    def get_syllabus_combof_class_term_subject(cls, _class_no, _term, _subject):
        try:
            syllabus_object = cls.query.filter_by(class_no=_class_no, term=_term, subject=_subject).first()
            if not syllabus_object:
                return syllabus_object
            else:
                return syllabus_object
        except:
            return None
        
    @classmethod
    def get_syllabus_combo(cls, _syllabus_object):
        try:
            syllabus_combo_obj = cls.query.filter_by(class_no=_syllabus_object.class_no, term=_syllabus_object.term, subject=_syllabus_object.subject).first()
            if not syllabus_combo_obj:
                return syllabus_combo_obj
            else:
                return syllabus_combo_obj.serialize()
        except:
            return None

    def serialize(self):
        json_syllabus = {
            "term": self.term,
            "class_no": self.class_no,
            "subject": self.subject,
            "syllabus_details": loads(self.syllabus_details),
            "syllabus_status": loads(self.syllabus_status)
        }
        return json_syllabus

    ############################################################################################
    # All the functions to retrieve seeker details and update them
    ############################################################################################
    def update_syllabus(self):
        db.session.add(self)
        db.session.commit()
        return True, False
