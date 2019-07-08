##########################################################################
# Name:     Users Routes
# Purpose: File contains Syllabus request endpoints like create, update, fetch etc.
#
# Author:     Sai Nikhita Guduru
#
# Created:   07/07/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2018 - Present
# Licence:   <your licence>
##########################################################################
from flask import Blueprint
from flask import Response, request
from json import dumps,loads
from services.syllabus.models import Syllabus


syllabus = Blueprint('syllabus', __name__)


@syllabus.route("/syllabus", methods=["POST"])
def api_add_syllabus():
    syllabus = request.get_json()
    syllabus_object = Syllabus(term = syllabus["term"], class_no = syllabus["class_no"], subject = syllabus["subject"], syllabus_details = dumps(syllabus["syllabus_details"]), syllabus_status = dumps(syllabus["syllabus_status"]))
    syllabus_exist = Syllabus.get_syllabus_combo(syllabus_object)
    if syllabus_exist:
        result = {
            "status": "Failure",
            "message": "Combination of Term, Class and Subject already exists!!"
        }
    else:
        syllabus_db = Syllabus.add_syllabus(syllabus_object)
        if syllabus_db:
            result = {
                "status": "success",
                "message": "syllabus added"
            }

    return Response(dumps(result), 200, mimetype='application/json')


@syllabus.route("/syllabus/all", methods=["GET"])
def api_syllabus_all():
    result = {
        "status": "success",
        "message": "syllabus display",
        "syllabus": Syllabus.get_whole_syllabus()
    }
    return Response(dumps(result), 200, mimetype='application/json')

@syllabus.route("/syllabus/combo", methods=["GET"])
def api_syllabus_combo():
    class_no = request.headers.get('class_no')
    term = request.headers.get('term')
    subject = request.headers.get('subject')
    if not class_no or not term or not subject:
        error = {
            "status": "Failure",
            "message": "Some key is missing"
        }
        return Response(dumps(error), 400, mimetype='application/json')

    syllabus_combo = Syllabus.get_syllabus_combof_class_term_subject(class_no, term, subject)
    if syllabus_combo is None:
        result = {
            "status": "success",
            "message": "Combination not found.",
            "syllabus": syllabus_combo
        }
        return Response(dumps(result), 400, mimetype='application/json')

    if not syllabus_combo is None:
        syllabus_combo_serialized = syllabus_combo.serialize()
        result = {
            "status": "success",
            "message": "Combination found.",
            "syllabus": syllabus_combo_serialized
        }
        return Response(dumps(result), 200, mimetype='application/json')

    return Response({"message": 'fetch done'}, 201, mimetype='application/json')

@syllabus.route("/syllabus/combo", methods=["PUT"])
def api_update_syllabus():
    request_data = request.get_json()
    class_no = request.headers.get('class_no')
    term = request.headers.get('term')
    subject = request.headers.get('subject')
    syllabus = Syllabus.get_syllabus_combof_class_term_subject(class_no, term, subject)
    if not syllabus:
        error = {
            "status": "Failure",
            "message": "record not found"
        }

        return Response(dumps(error), 501, mimetype='application/json')
    if "syllabus_details" in request_data:
        syllabus.syllabus_details = dumps(request_data["syllabus_details"])
    if "syllabus_status" in request_data:
        syllabus.syllabus_status = dumps(request_data["syllabus_status"])
    success, error = syllabus.update_syllabus()
    if success:
        result_update = {
            "status": "success",
            "message": "syllabus details updated",
            "syllabus updated": loads(syllabus.syllabus_details),
            "syllabus status": loads(syllabus.syllabus_status)
        }
        response = Response(dumps(result_update), 201, mimetype='application/json')
        return response

    if error:
        result_update={
            "status": "Failure",
            "message": "syllabus details not updated",
            'syllabus': {'msg': str(error)}
        }
        return Response(dumps(result_update), 501, mimetype='application/json')

    return Response({"message": 'update done'}, 501, mimetype='application/json')


def serialize(self):
    json_syllabus = {
        "term": self.term,
        "class_no": self.class_no,
        "subject": self.subject,
        "syllabus_details": loads(self.syllabus_details),
        "syllabus_status": loads(self.syllabus_status)
    }
    
    return json_syllabus