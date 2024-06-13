
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        
        return redirect(url_for('home'))
    return render_template('login.html')