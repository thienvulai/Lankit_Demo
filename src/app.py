from flask import Flask, render_template, request
from src import bp
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from src.views.home import home_bp
# from src.views.about import about_bp


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:N0n@me1984@localhost/testing'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class RequestMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fullname = db.Column(db.String(30))
    email = db.Column(db.String(30))
    message = db.Column(db.String(100))

    def __init__(self, fullname: str, email: str, message: str):
        self.fullname = fullname
        self.email = email
        self.message = message


@app.route('/')
def index():
    return render_template('home/index.html')


@app.route('/about')
def about():
    return render_template('about/index.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        message = request.form['message']
        msg1 = RequestMessage(fullname, email, message)

        db.session.add(msg1)
        db.session.commit()

    return render_template('contact/index.html')

# app.register_blueprint(home_bp)
# app.register_blueprint(about_bp)


if __name__ == '__main__':
    app.run()
