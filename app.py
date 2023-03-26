from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)  # Створюємо вебдодаток Flask
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///recepies.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(50), unique = True, nullable = False)
	password = db.Column(db.String, nullable = False)
	name = db.Column(db.String(200))
	logiks = db.Column(db.Integer, default = 0)

	projects = db.relationship('Project', backref = 'author')


class Project(db.Model):
	id=db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String, nullable = False)
	description = db.Column(db.Text)
	link = db.Column(db.Text)
	
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


@app.route("/")  # Вказуємо url-адресу для виклику функції
def index():
	return render_template("my_page.html")  # Результат, що повертається у браузер


if __name__ == "__main__":
	app.config['TEMPLATES_AUTO_RELOAD'] = True
	app.run(port=5001, debug=True)  # Запускаємо веб-сервер з цього файлу
