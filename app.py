from flask_sqlalchemy import SQLAlchemy

from flask import Flask, render_template

db = SQLAlchemy()
app = Flask(__name__)  # Створюємо вебдодаток Flask

app.config['SECRET_KEY'] = '70c4b7dfda8bd66dea2a9174e616c188'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///recepies.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

from routes import *

if __name__ == "__main__":
	app.config['TEMPLATES_AUTO_RELOAD'] = True
	app.run(port=5001, debug=True)  # Запускаємо веб-сервер з цього файлу