from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to Flask Lab Project!</h1>"

@app.route('/health')
def health():
    return jsonify({"status": "OK"}), 200

@app.route('/data', methods=['POST'])
def data():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    return jsonify({"received": data}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
