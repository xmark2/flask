from flask import Blueprint
from my_app.hello.models import MESSAGES

hello = Blueprint('hello',__name__)

from flask import render_template, request

@hello.route('/')
@hello.route('/hello')

def hello_world():
    user = request.args.get('user','Mark')
    return render_template('index.html', user=user)

def hello_world():
    return MESSAGES['default']

@hello.route('/show/<key>')
def get_message(key):
    return MESSAGES.get(key) or "%s not found!" % key

@hello.route('/add/<key>/<message>')
def add_or_update_message(key,message):
    MESSAGES[key] = message
    return "%s Added/Updated" % key
