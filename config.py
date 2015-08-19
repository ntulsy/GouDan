__author__ = 'Siyao'


WTF_CSRF_ENABLED = True
SECRET_KEY = 'SG%@dgd2#$!A'

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'goudan.db')