#Flask app file
from flask import Flask, jsonify
from routes.ask_routes import ask_question
from config.settings import Config
from routes.ask_routes import ask_question, get_questions

app = Flask(__name__)

# Load configuration
app.config["APP_NAME"] = Config.APP_NAME
app.config["VERSION"] = Config.VERSION
app.config["DEBUG"] = Config.DEBUG


@app.route("/")
def home():
    return jsonify({
        "app": app.config["APP_NAME"],
        "version": app.config["VERSION"],
        "status": "running"
    })

@app.route("/questions", methods=["GET"])
def questions():
    return get_questions()


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": app.config["APP_NAME"]
    })


@app.route("/ask", methods=["POST"])
def ask():
    return ask_question()


if __name__ == "__main__":
    app.run(debug=Config.DEBUG)
