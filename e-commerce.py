
@app.route('/adminmn', methods=['GET'])
def admin():
    db = get_db()
    orders = db.execute('''SELECT o.id, u.username, p.name 
                           FROM orders om
                           JOIN users u ON o.user_id = u.id 
                           JOIN products p ON o.product_id = p.id''').fetchall()
    return jsonify([{'order_id': row[0], 'username': row[1], 'product_name': row[2]} for row in orders])
