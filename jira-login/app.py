from flask import Flask, request, render_template
import sqlite3
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

# Function to initialize the SQLite database
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)')
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', ('infosecAdmin', 'infosecAdminRandomInfosecAdmin'))
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', ('UserInfosec', 'thisisarandominfosecuser'))
    conn.commit()
    conn.close()

init_db()

def sanitize_input(input_string):
    input_string = input_string.replace('"','')
    input_string = input_string.replace('--','')
    input_string = input_string.replace('//','')
    input_string = input_string.replace("'",'')
    return input_string

# Route for the login page (sanitized but vulnerable to SQL injection)
@app.route('/', methods=['GET', 'POST'])
def login():
    error_message = None

    if request.method == 'POST':
        username = sanitize_input(request.form['username'])
        password = sanitize_input(request.form['password'])

        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        query = f"SELECT * FROM users WHERE username LIKE '{username}' AND password LIKE '{password}'"
        c.execute(query)

        user = c.fetchone()
        conn.close()

        if user:
            return render_template('login_success.html', flag=os.getenv("FLAG"))
        else:
            error_message = 'Incorrect username or password. Additionally, you cannot use the special character sets ", --, // and \''

    return render_template('login.html', error_message=error_message)



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
