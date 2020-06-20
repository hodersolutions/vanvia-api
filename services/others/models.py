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

class AutomationRec(db.Model):
    __tablename__ = 'automation_rec'

    automation_recID = db.Column(db.Integer, primary_key=True)
    studentID = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    day = db.Column(db.String(3), nullable=False)
    month = db.Column(db.String(3), nullable=False)
    year = db.Column(db.String(4), nullable=False)
    nofmodule = db.Column(db.Integer, nullable=False)


class AutomationShudulu(db.Model):
    __tablename__ = 'automation_shudulu'

    automation_shuduluID = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    day = db.Column(db.String(3), nullable=False)
    month = db.Column(db.String(3), nullable=False)
    year = db.Column(db.String(4), nullable=False)


class Book(db.Model):
    __tablename__ = 'book'

    bookID = db.Column(db.Integer, primary_key=True)
    book = db.Column(db.String(60), nullable=False)
    subject_code = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    due_quantity = db.Column(db.Integer, nullable=False)
    rack = db.Column(db.Text, nullable=False)


class Category(db.Model):
    __tablename__ = 'category'

    categoryID = db.Column(db.Integer, primary_key=True)
    hostelID = db.Column(db.Integer, nullable=False)
    class_type = db.Column(db.String(60), nullable=False)
    hbalance = db.Column(db.String(20), nullable=False)
    note = db.Column(db.Text)



class Hmember(db.Model):
    __tablename__ = 'hmember'

    hmemberID = db.Column(db.Integer, primary_key=True)
    hostelID = db.Column(db.Integer, nullable=False)
    categoryID = db.Column(db.Integer, nullable=False)
    studentID = db.Column(db.Integer, nullable=False)
    hbalance = db.Column(db.String(20))
    hjoindate = db.Column(db.Date, nullable=False)


class Holiday(db.Model):
    __tablename__ = 'holiday'

    holidayID = db.Column(db.Integer, primary_key=True)
    schoolyearID = db.Column(db.Integer, nullable=False)
    fdate = db.Column(db.Date, nullable=False)
    tdate = db.Column(db.Date, nullable=False)
    title = db.Column(db.String(128), nullable=False)
    details = db.Column(db.Text, nullable=False)
    photo = db.Column(db.String(200))
    create_date = db.Column(db.DateTime, nullable=False)
    create_userID = db.Column(db.Integer, nullable=False)
    create_usertypeID = db.Column(db.Integer, nullable=False)


class Hostel(db.Model):
    __tablename__ = 'hostel'

    hostelID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    htype = db.Column(db.String(11), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    note = db.Column(db.Text)


class HourlyTemplate(db.Model):
    __tablename__ = 'hourly_template'

    hourly_templateID = db.Column(db.Integer, primary_key=True)
    hourly_grades = db.Column(db.String(128), nullable=False)
    hourly_rate = db.Column(db.Integer, nullable=False)


class Idmanager(db.Model):
    __tablename__ = 'idmanager'

    idmanagerID = db.Column(db.Integer, primary_key=True)
    schooltype = db.Column(db.String(20), nullable=False)
    idtitle = db.Column(db.String(128), nullable=False)
    idtype = db.Column(db.String(128), nullable=False)


class IniConfig(db.Model):
    __tablename__ = 'ini_config'

    configID = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(255), nullable=False)
    config_key = db.Column(db.String(255), nullable=False)
    value = db.Column(db.String(255), nullable=False)


class Instruction(db.Model):
    __tablename__ = 'instruction'

    instructionID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(512), nullable=False)
    content = db.Column(db.Text, nullable=False)


class Invoice(db.Model):
    __tablename__ = 'invoice'

    invoiceID = db.Column(db.Integer, primary_key=True)
    schoolyearID = db.Column(db.Integer, nullable=False)
    classesID = db.Column(db.Integer, nullable=False)
    studentID = db.Column(db.Integer, nullable=False)
    feetypeID = db.Column(db.Integer)
    feetype = db.Column(db.String(128), nullable=False)
    amount = db.Column(db.Float(asdecimal=True), nullable=False)
    discount = db.Column(db.Float(asdecimal=True), nullable=False)
    userID = db.Column(db.Integer)
    usertypeID = db.Column(db.Integer)
    uname = db.Column(db.String(60))
    date = db.Column(db.Date, nullable=False)
    create_date = db.Column(db.Date, nullable=False)
    day = db.Column(db.String(20))
    month = db.Column(db.String(20))
    year = db.Column(db.String(4), nullable=False)
    paidstatus = db.Column(db.Integer)
    deleted_at = db.Column(db.Integer, nullable=False, default="1")
    maininvoiceID = db.Column(db.Integer, nullable=False)


class Issue(db.Model):
    __tablename__ = 'issue'

    issueID = db.Column(db.Integer, primary_key=True)
    lID = db.Column(db.String(128), nullable=False)
    bookID = db.Column(db.Integer, nullable=False)
    serial_no = db.Column(db.String(40), nullable=False)
    issue_date = db.Column(db.Date, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    return_date = db.Column(db.Date)
    note = db.Column(db.Text)


class Lmember(db.Model):
    __tablename__ = 'lmember'

    lmemberID = db.Column(db.Integer, primary_key=True)
    lID = db.Column(db.String(40), nullable=False)
    studentID = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(40))
    phone = db.Column(db.Text)
    lbalance = db.Column(db.String(20))
    ljoindate = db.Column(db.Date, nullable=False)


class Location(db.Model):
    __tablename__ = 'location'

    locationID = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text)
    create_date = db.Column(db.Date, nullable=False)
    modify_date = db.Column(db.Date, nullable=False)
    create_userID = db.Column(db.Integer, nullable=False)
    create_usertypeID = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Integer, nullable=False)


class Maininvoice(db.Model):
    __tablename__ = 'maininvoice'

    maininvoiceID = db.Column(db.Integer, primary_key=True)
    maininvoiceschoolyearID = db.Column(db.Integer, nullable=False)
    maininvoiceclassesID = db.Column(db.Integer, nullable=False)
    maininvoicestudentID = db.Column(db.Integer, nullable=False)
    maininvoiceuserID = db.Column(db.Integer)
    maininvoiceusertypeID = db.Column(db.Integer)
    maininvoiceuname = db.Column(db.String(60))
    maininvoicedate = db.Column(db.Date, nullable=False)
    maininvoicecreate_date = db.Column(db.Date, nullable=False)
    maininvoiceday = db.Column(db.String(20))
    maininvoicemonth = db.Column(db.String(20))
    maininvoiceyear = db.Column(db.String(4), nullable=False)
    maininvoicestatus = db.Column(db.Integer)
    maininvoicedeleted_at = db.Column(db.Integer, nullable=False, default="1")


class MakePayment(db.Model):
    __tablename__ = 'make_payment'

    make_paymentID = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.Text, nullable=False)
    gross_salary = db.Column(db.Text, nullable=False)
    total_deduction = db.Column(db.Text, nullable=False)
    net_salary = db.Column(db.Text, nullable=False)
    payment_amount = db.Column(db.Text, nullable=False)
    payment_method = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.Text)
    templateID = db.Column(db.Integer, nullable=False)
    salaryID = db.Column(db.Integer, nullable=False)
    usertypeID = db.Column(db.Integer, nullable=False)
    userID = db.Column(db.Integer, nullable=False)
    schoolyearID = db.Column(db.Integer)
    create_date = db.Column(db.DateTime, nullable=False)
    modify_date = db.Column(db.DateTime, nullable=False)
    create_userID = db.Column(db.Integer, nullable=False)
    create_username = db.Column(db.String(60), nullable=False)
    create_usertype = db.Column(db.String(60), nullable=False)
    total_hours = db.Column(db.Text)


class Notice(db.Model):
    __tablename__ = 'notice'

    noticeID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    notice = db.Column(db.Text, nullable=False)
    schoolyearID = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    create_date = db.Column(db.TIMESTAMP, nullable=False, default=datetime.now())
    create_userID = db.Column(db.Integer, nullable=False)
    create_usertypeID = db.Column(db.Integer, nullable=False)


class Page(db.Model):
    __tablename__ = 'pages'

    pagesID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    url = db.Column(db.String(250))
    content = db.Column(db.Text)
    status = db.Column(db.Integer, comment=u'1 => active, 2 => draft, 3 => trash, 4 => review  ')
    visibility = db.Column(db.Integer, comment=u'1 => public 2 => protected 3 => private ')
    publish_date = db.Column(db.DateTime)
    parentID = db.Column(db.Integer, nullable=False)
    pageorder = db.Column(db.Integer, nullable=False)
    template = db.Column(db.String(250))
    featured_image = db.Column(db.String(11))
    create_date = db.Column(db.DateTime)
    modify_date = db.Column(db.DateTime)
    create_userID = db.Column(db.Integer)
    create_username = db.Column(db.String(60))
    create_usertypeID = db.Column(db.Integer)
    password = db.Column(db.String(40))



class Payment(db.Model):
    __tablename__ = 'payment'

    paymentID = db.Column(db.Integer, primary_key=True)
    schoolyearID = db.Column(db.Integer, nullable=False)
    invoiceID = db.Column(db.Integer, nullable=False)
    studentID = db.Column(db.Integer, nullable=False)
    paymentamount = db.Column(db.Float(asdecimal=True))
    paymenttype = db.Column(db.String(128), nullable=False)
    paymentdate = db.Column(db.Date, nullable=False)
    paymentday = db.Column(db.String(11), nullable=False)
    paymentmonth = db.Column(db.String(10), nullable=False)
    paymentyear = db.Column(db.String(4), nullable=False)
    userID = db.Column(db.Integer, nullable=False)
    usertypeID = db.Column(db.Integer, nullable=False)
    uname = db.Column(db.String(60), nullable=False)
    transactionID = db.Column(db.Text)
    globalpaymentID = db.Column(db.Integer, nullable=False)



class Permission(db.Model):
    __tablename__ = 'permissions'

    permissionID = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.VARCHAR(255), nullable=False)
    name = db.Column(db.VARCHAR(50), nullable=False, default="", comment=u'In most cases, this should be the name of the module (e.g. news)')
    active = db.Column(db.Boolean, nullable=False, default=1)


class Post(db.Model):
    __tablename__ = 'posts'

    postsID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    url = db.Column(db.String(250))
    content = db.Column(db.Text)
    status = db.Column(db.Integer, comment=u'1 => active, 2 => draft, 3 => trash, 4 => review  ')
    visibility = db.Column(db.Integer, comment=u'1 => public 2 => protected 3 => private ')
    publish_date = db.Column(db.DateTime)
    parentID = db.Column(db.Integer, nullable=False)
    postorder = db.Column(db.Integer, nullable=False)
    featured_image = db.Column(db.String(11))
    create_date = db.Column(db.DateTime)
    modify_date = db.Column(db.DateTime)
    create_userID = db.Column(db.Integer)
    create_username = db.Column(db.String(60))
    create_usertypeID = db.Column(db.Integer)
    password = db.Column(db.String(40))


class PostsCategory(db.Model):
    __tablename__ = 'posts_categories'

    posts_categoriesID = db.Column(db.Integer, primary_key=True)
    posts_categories = db.Column(db.String(40))
    posts_slug = db.Column(db.String(250))
    posts_parent = db.Column(db.Integer)
    posts_description = db.Column(db.Text)


class PostsCategory(db.Model):
    __tablename__ = 'posts_category'

    posts_categoryID = db.Column(db.Integer, primary_key=True)
    postsID = db.Column(db.Integer, nullable=False)
    posts_categoriesID = db.Column(db.Integer, nullable=False)


class Promotionlog(db.Model):
    __tablename__ = 'promotionlog'

    promotionLogID = db.Column(db.Integer, primary_key=True)
    promotionType = db.Column(db.String(50))
    classesID = db.Column(db.Integer, nullable=False)
    jumpClassID = db.Column(db.Integer, nullable=False)
    schoolYearID = db.Column(db.Integer, nullable=False)
    jumpSchoolYearID = db.Column(db.Integer, nullable=False)
    subjectandsubjectcodeandmark = db.Column(db.Text)
    exams = db.Column(db.Text)
    markpercentages = db.Column(db.Text)
    promoteStudents = db.Column(db.Text)
    status = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    create_userID = db.Column(db.Integer, nullable=False)


class Purchase(db.Model):
    __tablename__ = 'purchase'

    purchaseID = db.Column(db.Integer, primary_key=True)
    assetID = db.Column(db.Integer, nullable=False)
    vendorID = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit = db.Column(db.Integer)
    purchase_date = db.Column(db.Date)
    service_date = db.Column(db.Date)
    purchase_price = db.Column(db.Float(asdecimal=True), nullable=False)
    purchased_by = db.Column(db.Integer, nullable=False)
    usertypeID = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    expire_date = db.Column(db.Date)
    create_date = db.Column(db.Date, nullable=False)
    modify_date = db.Column(db.Date, nullable=False)
    create_userID = db.Column(db.Integer, nullable=False)
    create_usertypeID = db.Column(db.Integer, nullable=False)


class Reset(db.Model):
    __tablename__ = 'reset'

    resetID = db.Column(db.Integer, primary_key=True)
    keyID = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(60), nullable=False)


class Routine(db.Model):
    __tablename__ = 'routine'

    routineID = db.Column(db.Integer, primary_key=True)
    classesID = db.Column(db.Integer, nullable=False)
    sectionID = db.Column(db.Integer, nullable=False)
    subjectID = db.Column(db.Integer, nullable=False)
    schoolyearID = db.Column(db.Integer, nullable=False)
    teacherID = db.Column(db.Integer, nullable=False)
    day = db.Column(db.String(60), nullable=False)
    start_time = db.Column(db.String(10), nullable=False)
    end_time = db.Column(db.String(10), nullable=False)
    room = db.Column(db.Text, nullable=False)


class School(db.Model):
    __tablename__ = 'schools'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(1000), nullable=False)
    email = db.Column(db.String(1000), nullable=False)
    dbuser = db.Column(db.String(1000), default="")
    dbpassword = db.Column(db.String(1000), nullable=False)
    dbname = db.Column(db.String(1000), nullable=False)
    domain = db.Column(db.String(1000), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)
    active = db.Column(db.Integer, nullable=False, default="1")


class Schoolyear(db.Model):
    __tablename__ = 'schoolyear'

    schoolyearID = db.Column(db.Integer, primary_key=True)
    schooltype = db.Column(db.String(40))
    schoolyear = db.Column(db.String(128), nullable=False)
    schoolyeartitle = db.Column(db.String(128))
    startingdate = db.Column(db.Date, nullable=False)
    endingdate = db.Column(db.Date, nullable=False)
    semestercode = db.Column(db.Integer)
    create_date = db.Column(db.DateTime, nullable=False)
    modify_date = db.Column(db.DateTime, nullable=False)
    create_userID = db.Column(db.Integer, nullable=False)
    create_username = db.Column(db.String(100), nullable=False)
    create_usertype = db.Column(db.String(100), nullable=False)


class Section(db.Model):
    __tablename__ = 'section'

    sectionID = db.Column(db.Integer, primary_key=True)
    section = db.Column(db.String(60), nullable=False)
    category = db.Column(db.String(128), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    classesID = db.Column(db.Integer, nullable=False)
    teacherID = db.Column(db.Integer, nullable=False)
    note = db.Column(db.Text)
    create_date = db.Column(db.DateTime, nullable=False)
    modify_date = db.Column(db.DateTime, nullable=False)
    create_userID = db.Column(db.Integer, nullable=False)
    create_username = db.Column(db.String(60), nullable=False)
    create_usertype = db.Column(db.String(60), nullable=False)


class Setting(db.Model):
    __tablename__ = 'setting'

    fieldoption = db.Column(db.String(100), primary_key=True)
    value = db.Column(db.String(255))


class Slider(db.Model):
    __tablename__ = 'slider'

    sliderID = db.Column(db.Integer, primary_key=True)
    pagesID = db.Column(db.Integer, nullable=False)
    slider = db.Column(db.Integer, nullable=False)


class Sociallink(db.Model):
    __tablename__ = 'sociallink'

    sociallinkID = db.Column(db.Integer, primary_key=True)
    usertypeID = db.Column(db.Integer, nullable=False)
    userID = db.Column(db.Integer, nullable=False)
    facebook = db.Column(db.String(200), nullable=False)
    twitter = db.Column(db.String(200), nullable=False)
    linkedin = db.Column(db.String(200), nullable=False)
    googleplus = db.Column(db.String(200))


class SubAttendance(db.Model):
    __tablename__ = 'sub_attendance'

    attendanceID = db.Column(db.Integer, primary_key=True)
    schoolyearID = db.Column(db.Integer, nullable=False)
    studentID = db.Column(db.Integer, nullable=False)
    classesID = db.Column(db.Integer, nullable=False)
    sectionID = db.Column(db.Integer, nullable=False)
    subjectID = db.Column(db.Integer, nullable=False)
    userID = db.Column(db.Integer, nullable=False)
    usertype = db.Column(db.String(60), nullable=False)
    monthyear = db.Column(db.String(10), nullable=False)
    a1 = db.Column(db.String(3))
    a2 = db.Column(db.String(3))
    a3 = db.Column(db.String(3))
    a4 = db.Column(db.String(3))
    a5 = db.Column(db.String(3))
    a6 = db.Column(db.String(3))
    a7 = db.Column(db.String(3))
    a8 = db.Column(db.String(3))
    a9 = db.Column(db.String(3))
    a10 = db.Column(db.String(3))
    a11 = db.Column(db.String(3))
    a12 = db.Column(db.String(3))
    a13 = db.Column(db.String(3))
    a14 = db.Column(db.String(3))
    a15 = db.Column(db.String(3))
    a16 = db.Column(db.String(3))
    a17 = db.Column(db.String(3))
    a18 = db.Column(db.String(3))
    a19 = db.Column(db.String(3))
    a20 = db.Column(db.String(3))
    a21 = db.Column(db.String(3))
    a22 = db.Column(db.String(3))
    a23 = db.Column(db.String(3))
    a24 = db.Column(db.String(3))
    a25 = db.Column(db.String(3))
    a26 = db.Column(db.String(3))
    a27 = db.Column(db.String(3))
    a28 = db.Column(db.String(3))
    a29 = db.Column(db.String(3))
    a30 = db.Column(db.String(3))
    a31 = db.Column(db.String(3))


class Subject(db.Model):
    __tablename__ = 'subject'

    subjectID = db.Column(db.Integer, primary_key=True)
    classesID = db.Column(db.Integer, nullable=False)
    type = db.Column(db.Integer, nullable=False)
    passmark = db.Column(db.Integer, nullable=False)
    finalmark = db.Column(db.Integer, nullable=False)
    subject = db.Column(db.String(60), nullable=False)
    subject_author = db.Column(db.String(100))
    subject_code = db.Column(db.Text, nullable=False)
    teacher_name = db.Column(db.String(60), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    modify_date = db.Column(db.DateTime, nullable=False)
    create_userID = db.Column(db.Integer, nullable=False)
    create_username = db.Column(db.String(60), nullable=False)
    create_usertype = db.Column(db.String(60), nullable=False)


class Syllabu(db.Model):
    __tablename__ = 'syllabus'

    syllabusID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text)
    date = db.Column(db.Date, nullable=False)
    usertypeID = db.Column(db.Integer, nullable=False)
    userID = db.Column(db.Integer, nullable=False)
    originalfile = db.Column(db.Text, nullable=False)
    file = db.Column(db.Text)
    classesID = db.Column(db.Integer, nullable=False)
    schoolyearID = db.Column(db.Integer, nullable=False)


class Tattendance(db.Model):
    __tablename__ = 'tattendance'

    tattendanceID = db.Column(db.Integer, primary_key=True)
    schoolyearID = db.Column(db.Integer, nullable=False)
    teacherID = db.Column(db.Integer, nullable=False)
    usertypeID = db.Column(db.Integer, nullable=False)
    monthyear = db.Column(db.String(10), nullable=False)
    a1 = db.Column(db.String(3))
    a2 = db.Column(db.String(3))
    a3 = db.Column(db.String(3))
    a4 = db.Column(db.String(3))
    a5 = db.Column(db.String(3))
    a6 = db.Column(db.String(3))
    a7 = db.Column(db.String(3))
    a8 = db.Column(db.String(3))
    a9 = db.Column(db.String(3))
    a10 = db.Column(db.String(3))
    a11 = db.Column(db.String(3))
    a12 = db.Column(db.String(3))
    a13 = db.Column(db.String(3))
    a14 = db.Column(db.String(3))
    a15 = db.Column(db.String(3))
    a16 = db.Column(db.String(3))
    a17 = db.Column(db.String(3))
    a18 = db.Column(db.String(3))
    a19 = db.Column(db.String(3))
    a20 = db.Column(db.String(3))
    a21 = db.Column(db.String(3))
    a22 = db.Column(db.String(3))
    a23 = db.Column(db.String(3))
    a24 = db.Column(db.String(3))
    a25 = db.Column(db.String(3))
    a26 = db.Column(db.String(3))
    a27 = db.Column(db.String(3))
    a28 = db.Column(db.String(3))
    a29 = db.Column(db.String(3))
    a30 = db.Column(db.String(3))
    a31 = db.Column(db.String(3))


class Theme(db.Model):
    __tablename__ = 'themes'

    themesID = db.Column(db.Integer, primary_key=True)
    sortID = db.Column(db.Integer, nullable=False, default="1")
    themename = db.Column(db.String(128), nullable=False)
    backend = db.Column(db.Integer, nullable=False, default="1")
    frontend = db.Column(db.Integer, nullable=False, default="1")
    topcolor = db.Column(db.Text, nullable=False)
    leftcolor = db.Column(db.Text, nullable=False)


class Tmember(db.Model):
    __tablename__ = 'tmember'

    tmemberID = db.Column(db.Integer, primary_key=True)
    studentID = db.Column(db.Integer, nullable=False)
    transportID = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(40))
    phone = db.Column(db.Text)
    tbalance = db.Column(db.String(11))
    tjoindate = db.Column(db.Date, nullable=False)


class Track(db.Model):
    __tablename__ = 'track'

    id = db.Column(db.BigInteger, primary_key=True)
    url = db.Column(db.String(1000, u'utf8_unicode_ci'), nullable=False)


class Transport(db.Model):
    __tablename__ = 'transport'

    transportID = db.Column(db.Integer, primary_key=True)
    route = db.Column(db.Text, nullable=False)
    vehicle = db.Column(db.Integer, nullable=False)
    fare = db.Column(db.String(11), nullable=False)
    note = db.Column(db.Text)


class Uattendance(db.Model):
    __tablename__ = 'uattendance'

    uattendanceID = db.Column(db.Integer, primary_key=True)
    schoolyearID = db.Column(db.Integer, nullable=False)
    userID = db.Column(db.Integer, nullable=False)
    usertypeID = db.Column(db.Integer, nullable=False)
    monthyear = db.Column(db.String(10), nullable=False)
    a1 = db.Column(db.String(3))
    a2 = db.Column(db.String(3))
    a3 = db.Column(db.String(3))
    a4 = db.Column(db.String(3))
    a5 = db.Column(db.String(3))
    a6 = db.Column(db.String(3))
    a7 = db.Column(db.String(3))
    a8 = db.Column(db.String(3))
    a9 = db.Column(db.String(3))
    a10 = db.Column(db.String(3))
    a11 = db.Column(db.String(3))
    a12 = db.Column(db.String(3))
    a13 = db.Column(db.String(3))
    a14 = db.Column(db.String(3))
    a15 = db.Column(db.String(3))
    a16 = db.Column(db.String(3))
    a17 = db.Column(db.String(3))
    a18 = db.Column(db.String(3))
    a19 = db.Column(db.String(3))
    a20 = db.Column(db.String(3))
    a21 = db.Column(db.String(3))
    a22 = db.Column(db.String(3))
    a23 = db.Column(db.String(3))
    a24 = db.Column(db.String(3))
    a25 = db.Column(db.String(3))
    a26 = db.Column(db.String(3))
    a27 = db.Column(db.String(3))
    a28 = db.Column(db.String(3))
    a29 = db.Column(db.String(3))
    a30 = db.Column(db.String(3))
    a31 = db.Column(db.String(3))


class Update(db.Model):
    __tablename__ = 'update'

    updateID = db.Column(db.Integer, primary_key=True)
    version = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    userID = db.Column(db.Integer, nullable=False)
    usertypeID = db.Column(db.Integer, nullable=False)
    log = db.Column(db.Text, nullable=False)
    status = db.Column(db.Integer, nullable=False)


class Weaverandfine(db.Model):
    __tablename__ = 'weaverandfine'

    weaverandfineID = db.Column(db.Integer, primary_key=True)
    globalpaymentID = db.Column(db.Integer, nullable=False)
    invoiceID = db.Column(db.Integer, nullable=False)
    paymentID = db.Column(db.Integer, nullable=False)
    studentID = db.Column(db.Integer, nullable=False)
    schoolyearID = db.Column(db.Integer, nullable=False)
    weaver = db.Column(db.Float(asdecimal=True), nullable=False)
    fine = db.Column(db.Float(asdecimal=True), nullable=False)



class Class(db.Model):
    __tablename__ = 'classes'

    classesID = db.Column(db.Integer, primary_key=True)
    classes = db.Column(db.String(60), nullable=False)
    classes_numeric = db.Column(db.Integer, nullable=False)
    teacherID = db.Column(db.Integer, nullable=False)
    studentmaxID = db.Column(db.Integer)
    note = db.Column(db.Text)
    create_date = db.Column(db.DateTime, nullable=False)
    modify_date = db.Column(db.DateTime, nullable=False)
    create_userID = db.Column(db.Integer, nullable=False)
    create_username = db.Column(db.String(60), nullable=False)
    create_usertype = db.Column(db.String(60), nullable=False)