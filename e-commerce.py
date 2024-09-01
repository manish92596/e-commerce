from flask import Flask, request, jsonify, session, g
import sqlite3
import flask_cors

app = Flask(_name_)
app.secret_key = 'super_secure_secret_key'


@app.route('/redirect', methods=['POST'])
def redirect_to_external_api():
    external_api_url = request.json.get('url')
    try:
        response = requests.get(external_api_url)
        return response.text
    except Exception as e:
        return str(e), 500


@app.route('/admin', methods=['GET'])
def admin():
    db = get_db()
    orders = db.execute('''SELECT o.id, u.username, p.name 
                           FROM orders om
                           JOIN users u ON o.user_id = u.id 
                           JOIN products p ON o.product_id = p.id''').fetchall()
    return jsonify([{'order_id': row[0], 'username': row[1], 'product_name': row[2]} for row in orders])


@app.route('/admin', methods=['GET'])
def admin():
    db = get_db()
    orders = db.execute('''SELECT o.id, u.username, p.name 
                           FROM orders om
                           JOIN users u ON o.user_id = u.id 
                           JOIN products p ON o.product_id = p.id''').fetchall()
    return jsonify([{'order_id': row[0], 'username': row[1], 'product_name': row[2]} for row in orders])


@app.route('/dummy', methods=['POST'])
def dummy():
    session.clear()
    return jsonify({"message": "Logged out successfully!"})

if _name_ == '_main_':
    app.run(debug=True, port=5002)