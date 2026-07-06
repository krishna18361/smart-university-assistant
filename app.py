from flask import Flask, jsonify
from flask_cors import CORS
from config.settings import Config
from routes.ask_routes import ask_question, get_questions, get_single_question, update_question, delete_question
from routes.chat_routes import create_new_chat, get_chats, get_chat, send_message, remove_chat

app = Flask(__name__)
CORS(app)

# Load configuration
app.config["APP_NAME"] = Config.APP_NAME
app.config["VERSION"] = Config.VERSION
app.config["DEBUG"] = Config.DEBUG

# Existing routes
@app.route("/")
def home():
    return jsonify({
        "app": app.config["APP_NAME"],
        "version": app.config["VERSION"],
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": app.config["APP_NAME"]
    })

@app.route("/ask", methods=["POST"])
def ask():
    return ask_question()

@app.route("/questions", methods=["GET"])
def questions():
    return get_questions()

@app.route("/questions/<int:question_id>", methods=["GET"])
def question_by_id(question_id):
    return get_single_question(question_id)

@app.route("/questions/<int:question_id>", methods=["PUT"])
def update_question_route(question_id):
    return update_question(question_id)

@app.route("/questions/<int:question_id>", methods=["DELETE"])
def delete_question_route(question_id):
    return delete_question(question_id)

# New chat routes (MongoDB)
@app.route("/api/chats", methods=["POST"])
def create_chat():
    return create_new_chat()

@app.route("/api/chats", methods=["GET"])
def list_chats():
    return get_chats()

@app.route("/api/chats/<chat_id>", methods=["GET"])
def get_chat_history(chat_id):
    return get_chat(chat_id)

@app.route("/api/chats/<chat_id>/messages", methods=["POST"])
def post_message(chat_id):
    return send_message(chat_id)

@app.route("/api/chats/<chat_id>", methods=["DELETE"])
def delete_chat_route(chat_id):
    return remove_chat(chat_id)

if __name__ == "__main__":
    app.run(debug=Config.DEBUG)
