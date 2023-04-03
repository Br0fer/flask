from flask import render_template, request, url_for, redirect, flash
from app import app, db
from models import User, Recepies

@app.route("/")  # Вказуємо url-адресу для виклику функції
def index():
	recepies = Recepies.query.all()
	print(recepies)
	return render_template("my_page.html", recepies=recepies)  # Результат, що повертається у браузер

@app.route("/signup", methods = ["POST", "GET"])
def signup():
	if request.method == "POST":
		is_username = User.query.filter_by(username=request.form['username']).first()
		if is_username:
			flash("Таке ім'я користувача уже існує!", "alert-warning")
		elif len(request.form['password']) < 6 or len(request.form['username']) < 6:
			flash("Логін і пароль мають довші за 6 символі!", "alert-warning")
		elif request.form['password'] == request.form['passwordCheck']:
			user = User(name=request.form['name'],
						username=request.form['username'])
			user.set_password_hash(request.form['password'])
			db.session.add(user)
			db.session.commit()
			flash("Профіль створено!", "alert-success")
		else:
			flash("Паролі не збігаються!", "alert-danger")

	return render_template("signup.html")

@app.route("/signin", methods = ["POST", "GET"])
def signin():
	return render_template("login.html")