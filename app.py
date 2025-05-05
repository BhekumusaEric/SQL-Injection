from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# Setup in-memory DB for demo purposes
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    cursor.execute("INSERT INTO users VALUES ('admin', 'adminpass')")
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template_string('''
        <h2>Login</h2>
        <form action="/login" method="post">
            Username: <input name="username"><br>
            Password: <input name="password" type="password"><br>
            <input type="submit">
        </form>
    ''')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # ❌ VULNERABLE: SQL Injection here
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    
    if result:
        return "<h3>Login successful — Welcome!</h3>"
    else:
        return "<h3>Login failed.</h3>"

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
