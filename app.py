#Flask app file
from flask import Flask, jsonify
from routes.ask_routes import ask_question

app = Flask(__name__)


@app.route("/")
def home():
    return "Smart University Assistant API is running"


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "Smart University Assistant"
    })


@app.route("/ask", methods=["POST"])
def ask():
    return ask_question()


if __name__ == "__main__":
    app.run(debug=True)
