from flask import render_template, Blueprint, url_for

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home/')
def home():

    context = {
        'title': 'Home',
    }

    return render_template(
        'index.html',
        **context
    )