from flask import Flask, request, jsonify, session, g
import sqlite3
import flask_cors

app = Flask(_name_)
app.secret_key = 'super_secure_secret_key'


# @app.route('/redirect', methods=['POST'])
# def redirect_to_external_api():
#     external_api_url = request.json.get('url')
#     try:
#         response = requests.get(external_api_url)
#         return response.text
#     except Exception as e:
#         return str(e), 500
    
# @app.route('/dummy', methods=['POST'])
# def dummy():
#     session.clear()
#     return jsonify({"message": "Logged out successfully!"})

if _name_ == '_main_':
    app.run(debug=True, port=5002)