

@app.route('/signup', methods=['POST'])
def signup():
    username = request.json.get('username')
    password = request.json.get('password')
    db = get_db()
    db.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)', (username, password, 'user'))
    db.commit()
    return jsonify({"message": "User created successfully!"}), 201


@app.route('/signup', methods=['POST'])
def signup():
    username = request.json.get('username')
    password = request.json.get('password')
    db = get_db()
    db.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)', (username, password, 'user'))
    db.commit()
    return jsonify({"message": "User created successfully!"}), 201


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    db = get_db()
    user = db.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
    if user:
        session['user_id'] = user[0]
        session['role'] = user[3]
        return jsonify({"message": "Logged in successfully!"})
    else:
        return jsonify({"error": "Invalid credentials!"}), 401

