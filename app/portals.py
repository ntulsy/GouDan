__author__ = 'Siyao'

from app import app
from models import *
from crossdomain import crossdomain
import json


@app.route('/issue', methods=['GET'])
@crossdomain(origin='*', headers='Content-Type')
def index():
    return json.dumps(Issue.query.all())

