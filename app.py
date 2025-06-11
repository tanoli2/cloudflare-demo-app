from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to Cloudflare Demo App</h1>"

@app.route('/admin')
def admin():
    return "<h1>Admin Page - Protect with Cloudflare Zero Trust</h1>"

@app.route('/api/data', methods=['GET'])
def api_data():
    return jsonify({"message": "API protected by Cloudflare"})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if data.get('username') == 'admin' and data.get('password') == 'secret':
        return jsonify({"status": "success"})
    return jsonify({"status": "fail"}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
