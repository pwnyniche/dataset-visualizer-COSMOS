""" Database Connection details"""

import mysql.connector
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

mydb = mysql.connector.connect(
    host="sql6.freemysqlhosting.net",
    port=3306,
    user="sql6495395",
    password="KbedCE3Mia",
    database='sql6495395'
)
my_cursor = mydb.cursor(dictionary=True)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql6495395:KbedCE3Mia@sql6.freemysqlhosting.net:3306/sql6495395'
app.config['SECRET_KEY'] = 'mysecret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app=app)

