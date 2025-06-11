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

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Ciberjunk Flask Demo App is running."

# --- Vulnerable-like Endpoint for SQLi Demo ---
@app.route('/api/users')
def get_users():
    user_id = request.args.get('id', '')

    # Simulate a response that looks like it's handling a query
    if "' OR " in user_id or "--" in user_id or "=" in user_id:
        return jsonify({
            "error": "Suspicious query detected",
            "details": f"id = {user_id}"
        }), 400

    return jsonify({
        "id": user_id,
        "name": f"Demo User {user_id}"
    })
