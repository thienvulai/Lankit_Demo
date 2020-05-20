from flask import Blueprint, render_template

bp_route = Blueprint('bp_route', __name__)


@bp_route.route('/')
def index():
    return render_template('home/index.html')


@bp_route.route('/about')
def about():
    return render_template('about/index.html')


@bp_route.route('/contact')
def contact():
    return render_template('contact/index.html')
