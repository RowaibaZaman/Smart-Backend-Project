import os
# from sqlalchemy.orm import declarative_base, sessionmaker

class config:
     SQLALCHEMY_DATABASE_URI = 'mysql://root:12345@localhost/smart'

     SQLALCHEMY_TRACK_MODIFICATIONS = False

     # UPLOAD_FOLDER = r'C:/Users/HP/Desktop/uploads'
     # MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB limit
