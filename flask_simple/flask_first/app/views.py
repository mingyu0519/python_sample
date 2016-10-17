from flask import render_template, flash, redirect, request
from app import app
import time

app.config['SECRET_KEY']='you-will-never-guess'

@app.route('/')
@app.route('/index')
def index():
	user = { 'nickname': 'Miguel' } # fake user
	return render_template("index.html",
        title = 'Home',
        user = user)

@app.route('/boot')
def boot():
	user = { 'nicknamew': 'Miguwel' } # fake user
	return render_template("boot.html",
        title = 'Home',
        user = user)

@app.route('/submit',methods=['GET','POST'])
def submit():
	order_id = request.form.get('order')
	time.sleep(3)
	return render_template('result_base.html', order_id=order_id)
