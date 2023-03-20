from flask import Flask, render_template

app = Flask(__name__)  # Створюємо вебдодаток Flask


@app.route("/")  # Вказуємо url-адресу для виклику функції
def index():
    return render_template("index.html")  # Результат, що повертається у браузер


@app.route("/home")
def home():
    return render_template("my_page.html")


@app.route("/home/first")
def first():
    return render_template("first.html")


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(port=5001, debug=True)  # Запускаємо веб-сервер з цього файлу
