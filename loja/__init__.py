from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
#from flask_uploads import IMAGES, UploadSet, configure_uploads, patch_request_class

import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///devfruit.db'
app.config['SECRET_KEY'] = 'mysecretkey'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

#app.config['UPLOAD_FOLDER'] = os.path.join(basedir,'static/images')
#ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

'''
flask_uploads
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir,'static/images')
photos = UploadSet('photos',IMAGES)
configure_uploads(app, photos)
patch_request_class(app)
'''

from loja.admin import rotas
from loja.produtos import rotas