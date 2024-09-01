
@app.route('/api/all-endpoints', methods=['GET'])
def all_endpoints():
    endpoints = [e.rule for e in app.url_map.iter_rules() if not e.rule.startswith('/admin')]
    admin_endpoints = [e.rule for e in app.url_map.iter_rules() if e.rule.startswith('/admin')]
    return jsonify({"public_endpoints": endpoints, "admin_endpoints": admin_endpoints})



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



@app.route('/fetch-data', methods=['POST'])
def fetch_data():
    external_api_url = request.json.get('url')
    sensitive_data = request.json.get('sensitive_data')
    try:
        response = requests.post(external_api_url, json={"data": sensitive_data})
        return response.text
    except Exception as e:
 