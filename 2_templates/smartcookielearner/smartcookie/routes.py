from flask import render_template
from smartcookie import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html', title='Quiz')

@app.route('/coding')
def coding():
    return render_template('coding.html', title='Coding')

@app.route('/ai')
def AI():
    return render_template('ai.html', title='ai')

@app.route('/profile')
def profile():
    return render_template('profile.html', title='Profile')
