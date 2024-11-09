from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize the database
def init_db():
    conn = sqlite3.connect('trash_data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS trash_data (id INTEGER PRIMARY KEY, trash_type TEXT)''')
    conn.commit()
    conn.close()

@app.route('/store_trash_data', methods=['POST'])
def store_trash_data():
    data = request.json
    trash_type = data.get('trash_type')

    # Store the trash type in the database
    conn = sqlite3.connect('trash_data.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO trash_data (trash_type) VALUES (?)", (trash_type,))
    conn.commit()
    conn.close()

    return jsonify({'status': 'success', 'trash_type': trash_type})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
