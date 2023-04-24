from app import app, db
from flask import flash, redirect, render_template, request, url_for
from models import Recepies, User
from flask_login import login_user, logout_user, current_user, login_required
import datetime

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
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	if request.method == "POST":
		user = User.query.filter_by(username=request.form['username']).first()
		if user and user.check_password(request.form['password']):
			if login_user(user, remember=True, duration=datetime.timedelta(days=7)):
				return redirect(url_for('index'))
			flash("Ви увійшли", "alert-info")
		else:
			flash("Неправильний логін або пароль", "alert-danger")
	return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Ви вийшли з профілю", "alert-success")
    return redirect(url_for('signin'))

@app.route("/addin", methods=["POST", "GET"])
def addin():
	if request.method == "POST":
		recepie = Recepies(title=request.form["title"], ingredients=request.form['ingredients'], actions=request.form['actions'], img=request.form['photo'])
		db.session.add(recepie)
		db.session.commit()
		flash("Рецепт успішно додано!", "alert-success")
	return render_template("recep_adder.html")