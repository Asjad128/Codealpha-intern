from flask import Flask, request, render_template

import sqlite3
app = Flask(__name__)

@app.route('/user')
def get_user():
    user_id = request.args.get('user_id')
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    if user:
        return f"User: {user}"
    else:
        return "User not found"

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
