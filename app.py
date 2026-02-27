#Flask app file
# ...existing code...
from flask import Flask, jsonify
from config.settings import Config
from routes.ask_routes import ask_question, get_questions, get_single_question
# ...existing code...
from services.question_service import process_question
from services.db_service import get_all_questions, get_question_by_id
from routes.ask_routes import ask_question, get_questions, get_single_question, update_question
from routes.ask_routes import ask_question, get_questions, get_single_question, update_question, delete_question
# ...existing code...
# ...existing code...

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
@app.route("/questions/<int:question_id>", methods=["GET"])
def question_by_id(question_id):
    return get_single_question(question_id)

@app.route("/questions/<int:question_id>", methods=["PUT"])
def update_question_route(question_id):
    return update_question(question_id)

@app.route("/questions", methods=["GET"])
def questions():
    return get_questions()

@app.route("/questions/<int:question_id>", methods=["DELETE"])
def delete_question_route(question_id):
    return delete_question(question_id)


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
