from myproject2 import app, db
from flask import (render_template, render_template,
                   redirect, request, url_for, flash, abort)
from flask_login import login_user, login_required, logout_user
from myproject2.models import User
from myproject2.forms import RegistrationForm, LoginForm

@app.route('/')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('welcome/')
@login_required
def welcome_user():
    return render_template('welcome_user.html')

