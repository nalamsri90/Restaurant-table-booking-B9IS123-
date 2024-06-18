
from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

bookings = []
users = []
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

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        fullname = request.form['fullname']
        mobile = request.form['mobile']
        email = request.form['email']
        password = request.form['password']
        users.append({'username': username, 'fullname': fullname, 'mobile': mobile, 'email': email, 'password': password})
        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        name = request.form['name']
        date = request.form['date']
        time = request.form['time']
        guests = request.form['guests']
        bookings.append({'name': name, 'date': date, 'time': time, 'guests': guests})
        return redirect(url_for('home'))
    return render_template('booking.html')


if __name__ == '__main__':
    app.run(debug=True)