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
from passlib.hash import pbkdf2_sha256 as sha256


class Users(db.Model):
    __tablename__ = "users"

    # unique identifier for a user
    id = db.Column(db.Integer, primary_key=True)
    # uid, can be student's enrollment id, staff's employee_id
    uid = db.Column(db.Integer, nullable=False)
    # institute id
    uid = db.Column(db.Integer, nullable=False)
    # encrypted value
    password = db.Column(db.String(200), nullable=True)
    # first name of a user
    first_name = db.Column(db.String(80), nullable=True)
    # last name of a user
    last_name = db.Column(db.String(80), nullable=True)
    # email of the user, cannot be null, and should be unique
    email = db.Column(db.String(80), nullable=True)
    # mobile number of the user
    mobile = db.Column(db.String(80), nullable=True)
    # registration time
    creation_date = db.Column(db.DateTime, nullable=True, default=datetime.now())
    # If user is not with the Org anymore, TODO: use this effectively
    is_active = db.Column(db.Boolean, nullable=True, default=1)
    # user who is enrolling this record
    user_creator = db.Column(db.Integer, nullable=True)
    # user who is updating this record
    user_modifier = db.Column(db.Integer, nullable=True)
    # json value to store user specific details
    details = db.Column(db.String(2000), nullable=True)

    # foreign key from the user_roles table
    # roles_list = db.relationship('UserRoles', backref='enquiry', lazy=True)

    # foreign key from the user_details table
    # roles = db.relationship('UserDetails', backref='enquiry', lazy=True)

    def __repr__(self):
        return "{ email: {1}, id: {2}, mobile: {3} }".format(self.email, self.id, self.mobile)

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)

    def fullname(self):
        return "{} {}".format(self.first_name, self.last_name)

    @classmethod
    def add_user(cls, _user):
        try:
            # pw_hash = cls.generate_hash(_user.password)
            # _user.password = pw_hash
            # _user.is_active = 1
            db.session.add(_user)
            # add the role to the user before the db commit
            # user_roles.UserRoles.add_user_role(_user.id, _role)
            db.session.commit()
        except Exception as e:
            return None, e

        return cls.get_user_by_uid(_user.uid), None

    @classmethod
    def get_all_users(cls):
        return [user.serialize() for user in cls.query.all()]

    @classmethod
    def get_user_by_email(cls, _email):
        try:
            user_object = cls.query.filter_by(email=_email).first()
            if not user_object:
                return user_object
            else:
                return user_object.serialize()
        except:
            return None

    @classmethod
    def get_user_by_uid(cls, _uid):
        try:
            user_object = cls.query.filter_by(uid=_uid).first()
            if not user_object:
                return user_object
            else:
                return user_object
        except:
            return None

    @classmethod
    def get_users_from_text(cls, text):
        query = """select id, Users.firstname, Users.lastname from Users where Users.firstname like "%{}%"
        or Users.lastname like "%{}%" or Users.username like "%{}%" """.format(text, text, text)
        result = db.engine.execute(query)
        list_result = []
        for user in result:
            user_dict = {}
            user_dict['id'] = user[0]
            user_dict['label'] = "{} {}".format(user[1], user[2])
            list_result.append(user_dict)
        return list_result

    @classmethod
    def get_user_by_id(cls, id):
        user_object = cls.query.get(id)
        if not user_object:
            return None
        else:
            return user_object

    @classmethod
    def delete_user_by_uid(cls, _uid):
        try:
            cls.query.filter_by(uid=_uid).delete() # todo: use is_active instead of deleting the record
            db.session.commit()
        except:
            return False

        return True

    @classmethod
    def update_user_by_email(cls, _email, _user):
        try:
            user_to_update = cls.query.filter_by(email=_email).first()
            user_to_update.email = _user.email
            db.session.commit()
        except:
            return False

        return cls.get_user_by_email(_user.email)

    def serialize(self):
        json_user = {
            "id": self.id,
            "uid": self.uid,
            "mobile": self.mobile,
            "Email": self.email,
            # "registered_on": str(self.registered_on),
            "Fullname": self.fullname(),
            "details": self.details
        }
        return json_user

    ############################################################################################
    # All the functions to retrieve seeker details and update them
    ############################################################################################
    def update_user(self):
        db.session.add(self)
        db.session.commit()
        return True, False


class UsersAudit(db.Model):
    __tablename__ = "users_audit"

    # unique identifier for a user
    audit_id = db.Column(db.Integer, primary_key=True)
    # user identifier
    id = db.Column(db.Integer, nullable=False)
    # uid, can be student's enrollment id, staff's employee_id
    uid = db.Column(db.Integer, nullable=False)
    # encrypted value
    password = db.Column(db.String(200), nullable=True)
    # first name of a user
    first_name = db.Column(db.String(80), nullable=True)
    # last name of a user
    last_name = db.Column(db.String(80), nullable=True)
    # email of the user, cannot be null, and should be unique
    email = db.Column(db.String(80), nullable=True)
    # mobile number of the user
    mobile = db.Column(db.String(80), nullable=True)
    # registration time
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    # If user is not with the Org anymore, TODO: use this effectively
    is_active = db.Column(db.Boolean, nullable=True, default=1)
    # user who is enrolling this record
    user_creator = db.Column(db.Integer, nullable=True)
    # user who is updating this record
    user_modifier = db.Column(db.Integer, nullable=True)
    # json value to store user specific details
    details = db.Column(db.String(2000), nullable=True)


class Visitorinfo(db.Model):
    __tablename__ = 'visitorinfo'

    visitorID = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(60))
    email_id = db.Column(db.String(128))
    phone = db.Column(db.Text, nullable=False)
    photo = db.Column(db.String(128))
    company_name = db.Column(db.String(128))
    coming_from = db.Column(db.String(128))
    representing = db.Column(db.String(128))
    to_meet_personID = db.Column(db.Integer, nullable=False)
    to_meet_usertypeID = db.Column(db.Integer, nullable=False)
    check_in = db.Column(db.TIMESTAMP)
    check_out = db.Column(db.TIMESTAMP)
    status = db.Column(db.Integer, nullable=False)
    schoolyearID = db.Column(db.Integer, nullable=False)


class Vendor(db.Model):
    __tablename__ = 'vendor'

    vendorID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    contact_name = db.Column(db.String(255))
    date = db.Column(db.Date)


class Usertype(db.Model):
    __tablename__ = 'usertype'

    usertypeID = db.Column(db.Integer, primary_key=True)
    usertype = db.Column(db.String(60), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    modify_date = db.Column(db.DateTime, nullable=False)
    create_userID = db.Column(db.Integer, nullable=False)
    create_username = db.Column(db.String(60), nullable=False)
    create_usertype = db.Column(db.String(60), nullable=False)


class User(db.Model):
    __tablename__ = 'user'

    userID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    sex = db.Column(db.String(10), nullable=False)
    religion = db.Column(db.String(25))
    email = db.Column(db.String(40))
    phone = db.Column(db.Text)
    address = db.Column(db.Text)
    jod = db.Column(db.Date, nullable=False)
    photo = db.Column(db.String(200))
    username = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    usertypeID = db.Column(db.Integer, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    modify_date = db.Column(db.DateTime, nullable=False)
    create_userID = db.Column(db.Integer, nullable=False)
    create_username = db.Column(db.String(60), nullable=False)
    create_usertype = db.Column(db.String(60), nullable=False)
    active = db.Column(db.Integer, nullable=False)


class Teacher(db.Model):
    __tablename__ = 'teacher'

    teacherID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    designation = db.Column(db.String(128), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    sex = db.Column(db.String(10), nullable=False)
    religion = db.Column(db.String(25))
    email = db.Column(db.String(40))
    phone = db.Column(db.Text)
    address = db.Column(db.Text)
    jod = db.Column(db.Date, nullable=False)
    photo = db.Column(db.String(200))
    username = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    usertypeID = db.Column(db.Integer, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    modify_date = db.Column(db.DateTime, nullable=False)
    create_userID = db.Column(db.Integer, nullable=False)
    create_username = db.Column(db.String(60), nullable=False)
    create_usertype = db.Column(db.String(60), nullable=False)
    active = db.Column(db.Integer, nullable=False)


class Systemadmin(db.Model):
    __tablename__ = 'systemadmin'

    systemadminID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    sex = db.Column(db.String(10), nullable=False)
    religion = db.Column(db.String(25))
    email = db.Column(db.String(40))
    phone = db.Column(db.Text)
    address = db.Column(db.Text)
    jod = db.Column(db.Date, nullable=False)
    photo = db.Column(db.String(200))
    username = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    usertypeID = db.Column(db.Integer, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    modify_date = db.Column(db.DateTime, nullable=False)
    create_userID = db.Column(db.Integer, nullable=False)
    create_username = db.Column(db.String(60), nullable=False)
    create_usertype = db.Column(db.String(60), nullable=False)
    active = db.Column(db.Integer, nullable=False)
    systemadminextra1 = db.Column(db.String(128))
    systemadminextra2 = db.Column(db.String(128))


class Subjectteacher(db.Model):
    __tablename__ = 'subjectteacher'

    subjectteacherID = db.Column(db.Integer, primary_key=True)
    subjectID = db.Column(db.Integer, nullable=False)
    classesID = db.Column(db.Integer, nullable=False)
    teacherID = db.Column(db.Integer, nullable=False)


class Student(db.Model):
    __tablename__ = 'student'

    studentID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    dob = db.Column(db.Date)
    sex = db.Column(db.String(10), nullable=False)
    religion = db.Column(db.String(25))
    email = db.Column(db.String(40))
    phone = db.Column(db.Text)
    address = db.Column(db.Text)
    classesID = db.Column(db.Integer, nullable=False)
    sectionID = db.Column(db.Integer, nullable=False)
    roll = db.Column(db.String(50))
    bloodgroup = db.Column(db.String(5))
    country = db.Column(db.String(128))
    registerNO = db.Column(db.Integer)
    state = db.Column(db.String(128))
    library = db.Column(db.Integer, nullable=False)
    hostel = db.Column(db.Integer, nullable=False)
    transport = db.Column(db.Integer, nullable=False)
    photo = db.Column(db.String(200))
    parentID = db.Column(db.Integer)
    createschoolyearID = db.Column(db.Integer, nullable=False)
    schoolyearID = db.Column(db.Integer, nullable=False)
    admission_status = db.Column(db.Text)
    education_detail = db.Column(db.Text)
    admission_fee = db.Column(db.String(10))
    registration_fee = db.Column(db.String(10))
    admission_result = db.Column(db.String(20))
    emergency_contact_relation = db.Column(db.String(150))
    emergency_contact_no = db.Column(db.String(150))
    student_pob = db.Column(db.String(150))
    monthly_tuttion_fee = db.Column(db.String(10))
    username = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    usertypeID = db.Column(db.Integer, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    modify_date = db.Column(db.DateTime, nullable=False)
    create_userID = db.Column(db.Integer, nullable=False)
    create_username = db.Column(db.String(60), nullable=False)
    create_usertype = db.Column(db.String(60), nullable=False)
    active = db.Column(db.Integer, nullable=False)
    ethnicity = db.Column(db.String(1000))


class Studentextend(db.Model):
    __tablename__ = 'studentextend'

    studentextendID = db.Column(db.Integer, primary_key=True)
    studentID = db.Column(db.Integer, nullable=False)
    studentgroupID = db.Column(db.Integer, nullable=False)
    optionalsubjectID = db.Column(db.Integer, nullable=False)
    extracurricularactivities = db.Column(db.Text)
    remarks = db.Column(db.Text)


class Studentgroup(db.Model):
    __tablename__ = 'studentgroup'

    studentgroupID = db.Column(db.Integer, primary_key=True)
    group = db.Column(db.String(128), nullable=False)


class Studentrelation(db.Model):
    __tablename__ = 'studentrelation'

    studentrelationID = db.Column(db.Integer, primary_key=True)
    srstudentID = db.Column(db.Integer)
    srname = db.Column(db.String(40), nullable=False)
    srclassesID = db.Column(db.Integer)
    srclasses = db.Column(db.String(40))
    srroll = db.Column(db.String(50))
    srregisterNO = db.Column(db.String(128))
    srsectionID = db.Column(db.Integer)
    srsection = db.Column(db.String(40))
    srstudentgroupID = db.Column(db.Integer, nullable=False)
    sroptionalsubjectID = db.Column(db.Integer, nullable=False)
    srschoolyearID = db.Column(db.Integer)


class Admin(db.Model):
    __tablename__ = 'admin'

    id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(db.String(1000), nullable=False)
    password = db.Column(db.String(1000), nullable=False)
    lastadmin = db.Column(db.Integer, nullable=False)


class Parent(db.Model):
    __tablename__ = 'parents'

    parentsID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    father_name = db.Column(db.String(60), nullable=False)
    mother_name = db.Column(db.String(60), nullable=False)
    father_profession = db.Column(db.String(40), nullable=False)
    mother_profession = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(40))
    phone = db.Column(db.Text)
    address = db.Column(db.Text)
    guardian_realation_with_child = db.Column(db.String(60))
    guardian_nationality = db.Column(db.String(60))
    guardian_office_addresss = db.Column(db.String(200))
    guardian_qualification = db.Column(db.String(60))
    guardian_cnic = db.Column(db.String(60))
    guardian_address = db.Column(db.String(200))
    guardian_phone = db.Column(db.String(60))
    guardian_profession = db.Column(db.String(60))
    mother_nationality = db.Column(db.String(60))
    mother_office_addresss = db.Column(db.String(200))
    mother_qualification = db.Column(db.String(60))
    mother_cnic = db.Column(db.String(60))
    mother_address = db.Column(db.String(200))
    mother_phone = db.Column(db.String(60))
    father_nationality = db.Column(db.String(60))
    father_office_addresss = db.Column(db.String(200))
    father_qualification = db.Column(db.String(60))
    father_cnic = db.Column(db.String(60))
    photo = db.Column(db.String(200))
    username = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    usertypeID = db.Column(db.Integer, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    modify_date = db.Column(db.DateTime, nullable=False)
    create_userID = db.Column(db.Integer, nullable=False)
    create_username = db.Column(db.String(60), nullable=False)
    create_usertype = db.Column(db.String(60), nullable=False)
    active = db.Column(db.Integer, nullable=False)