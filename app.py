from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
from flask_login import LoginManager
login_manager = LoginManager()

db = SQLAlchemy()
app = Flask(__name__)  # Створюємо вебдодаток Flask

app.config['SECRET_KEY'] = '70c4b7dfda8bd66dea2a9174e616c188'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///recepies.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["IMAGE_UPLOADS"] = "C:/Users/tarik/OneDrive/Документи/Homework/IT/myweb/flask/static/images/uploades"
db.init_app(app)

login_manager.init_app(app)
login_manager.login_view = "signin"
login_manager.login_message = "Для перегляду сторінки увійдіть або зареєструйтеся"
login_manager.login_message_category = "alert-warning"

from routes import *

if __name__ == "__main__":
	app.config['TEMPLATES_AUTO_RELOAD'] = True
	app.run(port=5001, debug=True)  # Запускаємо веб-сервер з цього файлу