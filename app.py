from functools import wraps
from flask import Flask, render_template, url_for, redirect, request, flash, session
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'your_secret_key'

client = MongoClient('mongodb://localhost:27017')
db = client['desi_dhaba']
users_collection = db['users']
bookings_collection = db['bookings']

bookings = []
users = []

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash('Please log in to book a table.', 'error')
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def home():
    return render_template('home.html', bookings=bookings)

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = next((user for user in users if user['username'] == username and user['password'] == password), None)
        user = users_collection.find_one({'username':username})
        if user:
            session['username'] = username
            if user['password'] == password:
                flash('Logged in successfully!', 'success')
                next_page = request.args.get('next')
                return redirect(next_page or url_for('home'))
        else:
            flash('Invalid username or password', 'error')
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
        user_data = {'username': username, 'fullname': fullname, 'mobile': mobile, 'email': email, 'password': password}
        users.append({'username': username, 'fullname': fullname, 'mobile': mobile, 'email': email, 'password': password})
        users_collection.insert_one(user_data)
        flash('Registered successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/booking', methods=['GET', 'POST'])
@login_required
def booking():
    if request.method == 'POST':
        name = request.form['name']
        date = request.form['date']
        time = request.form['time']
        guests = request.form['guests']
        dish = request.form['dish']
        bookings.append({'name': name, 'date': date, 'time': time, 'guests': guests})
        flash('Table booked successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('booking.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logged out successfully!', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)