from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="college_admission"
)
cursor = db.cursor()

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    department = request.form['department']
    email = request.form['email']
    dob = request.form['dob']
    phone = request.form['phone']
    address = request.form['address']

    # Insert data into the database
    sql = "INSERT INTO applicants (name, department, email, dob, phone, address) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (name, department, email, dob, phone, address)
    cursor.execute(sql, values)
    db.commit()

    return redirect('/success')

@app.route('/success')
def success():
    return "Application submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
