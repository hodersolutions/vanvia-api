##########################################################################
# Name:     validate
# Purpose: File contains all the decorators to validate the user request
#
# Author:     Sai Nikhita Guduur
#
# Created:   10/07/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2018 - Present
# Licence:   <your licence>
##########################################################################
from flask import request, Response
from json import dumps
from functools import wraps
from services.syllabus.models import Syllabus


def validate_add_syllabus(func):
    """
    The function should validate add syllabus request
    :param func:
    :return: 400 and the error text
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        body = request.get_json()
        if "class_no" not in body:
            error = {
                "status": "failure",
                "message": "Bad Input, Please enter valid class."
            }
            return Response(dumps(error), 400, mimetype="application/json")
        
        class_no = body["class_no"]

        if "term" not in body:
            error = {
                "status": "failure",
                "message": "Bad Input, Please enter term details."
            }
            return Response(dumps(error), 400, mimetype="application/json")
        
        term = body["term"]
        
        if "subject" not in body:
            error = {
                "status": "failure",
                "message": "Bad Input, Please enter subject details."
            }
            return Response(dumps(error), 400, mimetype="application/json")

        subject = body["subject"]
                
        if "syllabus_details" not in body:
            error = {
                "status": "failure",
                "message": "Bad Input, Please enter syllabus details."
            }
            return Response(dumps(error), 400, mimetype="application/json")

        if "syllabus_details" in body and not body["syllabus_details"]:
            error = {
                "status": "failure",
                "message": "Bad Input, Please enter valid syllabus details."
            }
            return Response(dumps(error), 400, mimetype="application/json")
        
        syllabus_exist = Syllabus.get_syllabus_combof_class_term_subject(class_no, term, subject)
        if syllabus_exist:
            error = {
                "status": "Failure",
                "message": "Combination of Term, Class and Subject already exists!!"
            }
            return Response(dumps(error), 501, mimetype='application/json')

        return func(*args, **kwargs)

    return wrapper

def validate_syllabus_update(func):
    """
    The function should validate the syllabus update request
    :param func:
    :return: 400 and the error text
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        body = request.get_json()
        if "term" in request.headers and not request.headers["term"]:
            error = {
                "status": "failure",
                "message": "Bad Input, Please enter valid term."
            }
            return Response(dumps(error), 400, mimetype="application/json")

        if "class_no" in request.headers and not request.headers["class_no"]:
            print("False")
            error = {
                "status": "failure",
                "message": "Bad Input, Please enter valid class."
            }
            return Response(dumps(error), 400, mimetype="application/json")

        if "subject" in request.headers and not request.headers["subject"]:
            error = {
                "status": "failure",
                "message": "Bad Input, Please enter valid subject."
            }
            return Response(dumps(error), 400, mimetype="application/json")
                        
        if "syllabus_details" not in body:
            error = {
                "status": "failure",
                "message": "Bad Input, Please enter syllabus details."
            }
            return Response(dumps(error), 400, mimetype="application/json")

        if "syllabus_details" in body and not body["syllabus_details"]:
            error = {
                "status": "failure",
                "message": "Bad Input, Please enter valid syllabus details."
            }
            return Response(dumps(error), 400, mimetype="application/json")
        
        term = request.headers.get('term')
        subject = request.headers.get('subject')
        class_no = request.headers.get('class_no')

        syllabus = Syllabus.get_syllabus_combof_class_term_subject(class_no, term, subject)
        if not syllabus:
            error = {
                "status": "Failure",
                "message": "record not found"
            }

            return Response(dumps(error), 501, mimetype='application/json')

        return func(*args, **kwargs)
    return wrapper
