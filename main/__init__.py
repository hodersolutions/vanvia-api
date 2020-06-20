##########################################################################
# Name: main
# Purpose: main module which creates the Application instance
#
# Author:     Siva Samudrala
#
# Created:   29/06/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2018 - Present
# Licence:   <your licence>
##########################################################################
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import DefaultConfig

cors = CORS()
db = SQLAlchemy()
jwt = JWTManager()


def create_app(config_class=DefaultConfig):
    """
    Creates the app instance with its own config and other values.
    :param config_class:
    :return: app instance
    """
    app = Flask(__name__)
    # we need a .config file to store these values not a python class TODO
    app.config.from_object(DefaultConfig)

    db.init_app(app)
    cors.init_app(app)
    jwt.init_app(app)

    from attributes.castes.routes import castes
    from attributes.religions.routes import religions
    from attributes.subjects.routes import subjects
    from attributes.institutions.routes import institutions
    from attributes.towns.routes import towns
    from attributes.districts.routes import districts
    from attributes.states.routes import states
    from attributes.standards.routes import standards
    from logins.routes import logins
    from main.routes import main
    from roles.routes import roles
    from services.activities.routes import activities
    from services.alerts.routes import alerts
    from services.alumni.routes import alumni
    from services.assets.routes import assets
    from services.assignments.routes import assignments
    from services.attendance.routes import attendance
    from services.communications.routes import communications
    from services.conversations.routes import conversations
    from services.courses.routes import courses
    from services.e_library.routes import e_library
    from services.examinations.routes import examinations
    from services.events.routes import events
    from services.expenses.routes import expenses
    from services.feedback.routes import feedback
    from services.fees.routes import fees
    from services.funds.routes import funds
    from services.galleries.routes import galleries
    from services.inventory.routes import inventory
    from services.leaves.routes import leaves
    from services.marks.routes import marks
    from services.menu.routes import menu
    from services.moms.routes import moms
    from services.newsletters.routes import newsletters
    from services.others.routes import others
    from services.performance.routes import performance
    from services.questionbank.routes import questionbank
    from services.reimbursements.routes import reimbursements
    from services.salaries.routes import salaries
    from services.surveys.routes import surveys
    from services.users.routes import users

    app.register_blueprint(logins)
    app.register_blueprint(main)
    app.register_blueprint(roles)
    app.register_blueprint(users)
    app.register_blueprint(castes)
    app.register_blueprint(religions)
    app.register_blueprint(subjects)
    app.register_blueprint(institutions)
    app.register_blueprint(towns)
    app.register_blueprint(districts)
    app.register_blueprint(states)
    app.register_blueprint(users)
    app.register_blueprint(standards)

    return app
