from functools import wraps
from flask import Flask, render_template, url_for, redirect, request, flash, session
from pymongo import MongoClient
import base64

app = Flask(__name__)
app.secret_key = 'your_secret_key'

client = MongoClient('mongodb://localhost:27017')
db = client['desi_dhaba']
menu_collection = db['menu']
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
    starters = menu_collection.find({'category': 'starter'})
    mains = menu_collection.find({'category': 'main course'})
    desserts = menu_collection.find({'category': 'dessert'})
    return render_template('menu.html', starters=starters, mains=mains, desserts=desserts)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    if query:
        item = menu_collection.find_one({'name': {'$regex': query, '$options': 'i'}})
        if item:
            return render_template('menu.html', search_result=item)
        else:
            return render_template('menu.html', search_result='not_found')
    return redirect(url_for('menu'))

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
        dishes = request.form['dishes']
        booking_data = {'name': name, 'date': date, 'time': time, 'guests': guests, 'dishes': dishes}
        bookings_collection.insert_one(booking_data)
        flash('Table booked successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('booking.html')

@app.template_filter('b64encode')
def b64encode_filter(data):
    return base64.b64encode(data).decode('utf-8')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logged out successfully!', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)