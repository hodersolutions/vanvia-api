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

class Media(db.Model):
    __tablename__ = 'media'

    mediaID = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, nullable=False)
    usertypeID = db.Column(db.Integer, nullable=False)
    mcategoryID = db.Column(db.Integer, nullable=False)
    file_name = db.Column(db.String(255), nullable=False)
    file_name_display = db.Column(db.String(255), nullable=False)


class MediaCategory(db.Model):
    __tablename__ = 'media_category'

    mcategoryID = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, nullable=False)
    usertypeID = db.Column(db.Integer, nullable=False)
    folder_name = db.Column(db.String(255), nullable=False)
    create_time = db.Column(db.TIMESTAMP, nullable=False, default=datetime.now())


class MediaGallery(db.Model):
    __tablename__ = 'media_gallery'

    media_galleryID = db.Column(db.Integer, primary_key=True)
    media_gallery_type = db.Column(db.Integer, nullable=False)
    file_type = db.Column(db.String(40))
    file_name = db.Column(db.String(255))
    file_original_name = db.Column(db.String(255))
    file_title = db.Column(db.Text, nullable=False)
    file_size = db.Column(db.String(40))
    file_width_height = db.Column(db.String(40))
    file_upload_date = db.Column(db.DateTime)
    file_caption = db.Column(db.Text)
    file_alt_text = db.Column(db.String(255))
    file_description = db.Column(db.Text)
    file_length = db.Column(db.String(128))
    file_artist = db.Column(db.String(128))
    file_album = db.Column(db.String(128))


class MediaShare(db.Model):
    __tablename__ = 'media_share'

    shareID = db.Column(db.Integer, primary_key=True)
    classesID = db.Column(db.Integer, nullable=False)
    public = db.Column(db.Integer, nullable=False)
    file_or_folder = db.Column(db.Integer, nullable=False)
    item_id = db.Column(db.Integer, nullable=False)
    create_time = db.Column(db.TIMESTAMP, nullable=False, default=datetime.now())