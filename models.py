from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from app import db, login_manager


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String(200))

    recepies = db.relationship('Recepies', backref='author')

    def __repr__(self):
        return f"User: {self.username}"

    def set_password_hash(self, original_password):
        self.password = generate_password_hash(original_password)

    def check_password(self, original_password):
        return check_password_hash(self.password, original_password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Recepies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    ingredients = db.Column(db.Text)
    actions = db.Column(db.Text)
    img = db.Column(db.Text)
    link = db.Column(db.Text)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Recepie: {self.ingredients}"
