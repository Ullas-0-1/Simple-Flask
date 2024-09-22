from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL Connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ullas01112004",
    database="flaskdb"
)

# Route for home page
@app.route('/')
def index():
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return render_template('index.html', users=users)

# Route to handle form submission
@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    
    cursor = mydb.cursor()
    sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
    values = (name, email)
    cursor.execute(sql, values)
    mydb.commit()
    
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
