from login import app
from flask import render_template, session, url_for

app.route('/')
def index():
    if 'user_login' in session:
        return render_template(url_for('home_page'))
    return render_template(url_for('login'))