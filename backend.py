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

    # Store the trash type and update count
    conn = sqlite3.connect('trash_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT count FROM trash_counts WHERE trash_type = ?', (trash_type,))
    row = cursor.fetchone()
    if row:
        new_count = row[0] + 1
        cursor.execute('UPDATE trash_counts SET count = ? WHERE trash_type = ?', (new_count, trash_type))
    else:
        cursor.execute('INSERT INTO trash_counts (trash_type, count) VALUES (?, ?)', (trash_type, 1))
    conn.commit()
    conn.close()

    return jsonify({'status': 'success', 'trash_type': trash_type})
