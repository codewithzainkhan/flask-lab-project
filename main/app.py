from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__, template_folder="../member2_frontend/templates", static_folder="../member2_frontend/static")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/result')
def result():
    return render_template("result.html")

@app.route('/health')
def health():
    return jsonify({"status": "OK"}), 200

@app.route('/data', methods=['POST'])
def data():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "Invalid input"}), 400
    message = f"Hello, {data['name']}! Data received successfully."
    return jsonify({"message": message}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
