import logging
from datetime import datetime
import json
import re
from google.cloud import storage
#from google.cloud.storage import Blob


from flask import Flask, render_template, request

#use dev_appserver.py .
#para ativar o server localmente
#localhost:8080/form

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submitted', methods=['POST'])
def submitted_form():
    name = request.form['name']
    email = request.form['email']
    site = request.form['site_url']
    comments = request.form['comments']
    return render_template(
    'submitted_form.html',
    name=name,
    email=email,
    site=site,
    comments=comments)

#test coment
#new line