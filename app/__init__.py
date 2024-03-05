from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'bryanmarshall.com'
app.config['MYSQL_USER'] = 'dbjvussd9izrmn '
app.config['MYSQL_PASSWORD'] = 'unrxt8o2x8vzg'
app.config['MYSQL_DB'] = 'GradApp'

mysql = MySQL(app)

from app import routes
