from flask import render_template
from app import mysql
from app import app


@app.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM student WHERE student_id = 1")
    result = cur.fetchone()
    username = result['first_name']
    return render_template('home.html', username=username)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')