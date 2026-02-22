from flask import request, jsonify
from services.question_service import process_question
from services.db_service import get_all_questions


def get_questions():
    data = get_all_questions()
    return jsonify(data), 200
def ask_question():

    # Validation layer
    if not request.is_json:
        return jsonify({
            "error": "Request must be JSON"
        }), 400

    data = request.get_json()

    question = data.get("question")

    if not question:
        return jsonify({
            "error": "Question is required"
        }), 400

    if not isinstance(question, str):
        return jsonify({
            "error": "Question must be a string"
        }), 400

    # Call service layer
    result = process_question(question)

    return jsonify(result), 200
