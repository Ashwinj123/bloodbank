from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_username'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'blood_bank_db'

# Initialize MySQL
mysql = MySQL(app)

# Routes

@app.route('/')
def home():
    return render_template('db.html')

@app.route('/donor')
def donor():
    return render_template('db1.html')

@app.route('/patient')
def patient():
    return render_template('patient.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Perform login authentication (you need to implement this)

        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
