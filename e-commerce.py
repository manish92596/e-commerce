def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, role TEXT)''')
        g.db.execute('''CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, price REAL)''')
        g.db.execute('''CREATE TABLE orders (id INTEGER PRIMARY KEY, user_id INTEGER, product_id INTEGER)''')
        g.db.execute('''INSERT INTO users (username, password, role) VALUES ('admin', 'adminpass', 'admin')''')
        g.db.execute('''INSERT INTO users (username, password, role) VALUES ('user1', 'user1pass', 'user')''')
        g.db.execute('''INSERT INTO products (name, price) VALUES ('Product1', 10.0)''')
        g.db.execute('''INSERT INTO products (name, price) VALUES ('Product2', 20.0)''')
        g.db.commit()
    return g.db

@app.teardown_appcontext
def close_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

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

