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

class Product(db.Model):
    __tablename__ = 'product'

    productID = db.Column(db.Integer, primary_key=True)
    productcategoryID = db.Column(db.Integer, nullable=False)
    productname = db.Column(db.String(128), nullable=False)
    productbuyingprice = db.Column(db.Float(asdecimal=True), nullable=False)
    productsellingprice = db.Column(db.Float(asdecimal=True), nullable=False)
    productdesc = db.Column(db.Text, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    modify_date = db.Column(db.DateTime, nullable=False)
    create_userID = db.Column(db.Integer, nullable=False)
    create_usertypeID = db.Column(db.Integer, nullable=False)


class Productcategory(db.Model):
    __tablename__ = 'productcategory'

    productcategoryID = db.Column(db.Integer, primary_key=True)
    productcategoryname = db.Column(db.String(128), nullable=False)
    productcategorydesc = db.Column(db.Text, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    modify_date = db.Column(db.DateTime, nullable=False)
    create_userID = db.Column(db.Integer, nullable=False)
    create_usertypeID = db.Column(db.Integer, nullable=False)


class Productpurchase(db.Model):
    __tablename__ = 'productpurchase'

    productpurchaseID = db.Column(db.Integer, primary_key=True)
    schoolyearID = db.Column(db.Integer, nullable=False)
    productsupplierID = db.Column(db.Integer, nullable=False)
    productwarehouseID = db.Column(db.Integer, nullable=False)
    productpurchasereferenceno = db.Column(db.String(100), nullable=False)
    productpurchasedate = db.Column(db.Date, nullable=False)
    productpurchasefile = db.Column(db.String(200))
    productpurchasefileorginalname = db.Column(db.String(200))
    productpurchasedescription = db.Column(db.Text)
    productpurchasestatus = db.Column(db.Integer, nullable=False, comment=u'0 = pending, 1 = partial_paid,  2 = fully_paid')
    productpurchaserefund = db.Column(db.Integer, nullable=False, comment=u'0 = not refund, 1 = refund ')
    productpurchasetaxID = db.Column(db.Integer, nullable=False)
    productpurchasetaxamount = db.Column(db.Float(asdecimal=True), nullable=False)
    productpurchasediscount = db.Column(db.Float(asdecimal=True), nullable=False)
    productpurchaseshipping = db.Column(db.Float(asdecimal=True), nullable=False)
    productpurchasepaymentterm = db.Column(db.Integer, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    modify_date = db.Column(db.DateTime, nullable=False)
    create_userID = db.Column(db.Integer, nullable=False)
    create_usertypeID = db.Column(db.Integer, nullable=False)


class Productpurchaseitem(db.Model):
    __tablename__ = 'productpurchaseitem'

    productpurchaseitemID = db.Column(db.Integer, primary_key=True)
    schoolyearID = db.Column(db.Integer, nullable=False)
    productpurchaseID = db.Column(db.Integer, nullable=False)
    productID = db.Column(db.Integer, nullable=False)
    productpurchaseunitprice = db.Column(db.Float(asdecimal=True), nullable=False)
    productpurchasequantity = db.Column(db.Float(asdecimal=True), nullable=False)


class Productpurchasepaid(db.Model):
    __tablename__ = 'productpurchasepaid'

    productpurchasepaidID = db.Column(db.Integer, primary_key=True)
    productpurchasepaidschoolyearID = db.Column(db.Integer, nullable=False)
    schoolyearID = db.Column(db.Integer, nullable=False)
    productpurchaseID = db.Column(db.Integer, nullable=False)
    productpurchasepaiddate = db.Column(db.Date, nullable=False)
    productpurchasepaidreferenceno = db.Column(db.String(100), nullable=False)
    productpurchasepaidamount = db.Column(db.Float(asdecimal=True), nullable=False)
    productpurchasepaidpaymentmethod = db.Column(db.Integer, nullable=False, comment=u'1 = cash, 2 = cheque, 3 = crediit card, 4 = other')
    productpurchasepaidfile = db.Column(db.String(200))
    productpurchasepaidorginalname = db.Column(db.String(200))
    productpurchasepaiddescription = db.Column(db.Text)
    create_date = db.Column(db.DateTime, nullable=False)
    modify_date = db.Column(db.DateTime, nullable=False)
    create_userID = db.Column(db.Integer, nullable=False)
    create_usertypeID = db.Column(db.Integer, nullable=False)


class Productsale(db.Model):
    __tablename__ = 'productsale'

    productsaleID = db.Column(db.Integer, primary_key=True)
    schoolyearID = db.Column(db.Integer, nullable=False)
    productsalecustomertypeID = db.Column(db.Integer, nullable=False)
    productsalecustomerID = db.Column(db.Integer, nullable=False)
    productsalereferenceno = db.Column(db.String(100), nullable=False)
    productsaledate = db.Column(db.Date, nullable=False)
    productsalefile = db.Column(db.String(200))
    productsalefileorginalname = db.Column(db.String(200))
    productsaledescription = db.Column(db.Text)
    productsalestatus = db.Column(db.Integer, nullable=False, comment=u'0 = select_payment_status, 1 = due,  2 = partial, 3 = Paid')
    productsalerefund = db.Column(db.Integer, nullable=False, comment=u'0 = not refund, 1 = refund ')
    productsaletaxID = db.Column(db.Integer, nullable=False)
    productsaletaxamount = db.Column(db.Float(asdecimal=True), nullable=False)
    productsalediscount = db.Column(db.Float(asdecimal=True), nullable=False)
    productsaleshipping = db.Column(db.Float(asdecimal=True), nullable=False)
    productsalepaymentterm = db.Column(db.Integer, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    modify_date = db.Column(db.DateTime, nullable=False)
    create_userID = db.Column(db.Integer, nullable=False)
    create_usertypeID = db.Column(db.Integer, nullable=False)


class Productsaleitem(db.Model):
    __tablename__ = 'productsaleitem'

    productsaleitemID = db.Column(db.Integer, primary_key=True)
    schoolyearID = db.Column(db.Integer, nullable=False)
    productsaleID = db.Column(db.Integer, nullable=False)
    productID = db.Column(db.Integer, nullable=False)
    productsaleserialno = db.Column(db.String(100))
    productsaleunitprice = db.Column(db.Float(asdecimal=True), nullable=False)
    productsalequantity = db.Column(db.Float(asdecimal=True), nullable=False)


class Productsalepaid(db.Model):
    __tablename__ = 'productsalepaid'

    productsalepaidID = db.Column(db.Integer, primary_key=True)
    productsalepaidschoolyearID = db.Column(db.Integer, nullable=False)
    schoolyearID = db.Column(db.Integer, nullable=False)
    productsaleID = db.Column(db.Integer, nullable=False)
    productsalepaiddate = db.Column(db.Date, nullable=False)
    productsalepaidreferenceno = db.Column(db.String(100), nullable=False)
    productsalepaidamount = db.Column(db.Float(asdecimal=True), nullable=False)
    productsalepaidpaymentmethod = db.Column(db.Integer, nullable=False, comment=u'1 = cash, 2 = cheque, 3 = crediit card, 4 = other')
    productsalepaidfile = db.Column(db.String(200))
    productsalepaidorginalname = db.Column(db.String(200))
    productsalepaiddescription = db.Column(db.Text)
    create_date = db.Column(db.DateTime, nullable=False)
    modify_date = db.Column(db.DateTime, nullable=False)
    create_userID = db.Column(db.Integer, nullable=False)
    create_usertypeID = db.Column(db.Integer, nullable=False)


class Productsupplier(db.Model):
    __tablename__ = 'productsupplier'

    productsupplierID = db.Column(db.Integer, primary_key=True)
    productsuppliercompanyname = db.Column(db.String(128), nullable=False)
    productsuppliername = db.Column(db.String(40), nullable=False)
    productsupplieremail = db.Column(db.String(40))
    productsupplierphone = db.Column(db.String(20))
    productsupplieraddress = db.Column(db.Text)
    create_date = db.Column(db.DateTime, nullable=False)
    modify_date = db.Column(db.DateTime, nullable=False)
    create_userID = db.Column(db.Integer, nullable=False)
    create_usertypeID = db.Column(db.Integer, nullable=False)


class Productwarehouse(db.Model):
    __tablename__ = 'productwarehouse'

    productwarehouseID = db.Column(db.Integer, primary_key=True)
    productwarehousename = db.Column(db.String(128), nullable=False)
    productwarehousecode = db.Column(db.String(128), nullable=False)
    productwarehouseemail = db.Column(db.String(40))
    productwarehousephone = db.Column(db.String(20))
    productwarehouseaddress = db.Column(db.Text)
    create_date = db.Column(db.DateTime, nullable=False)
    modify_date = db.Column(db.DateTime, nullable=False)
    create_userID = db.Column(db.Integer, nullable=False)
    create_usertypeID = db.Column(db.Integer, nullable=False)