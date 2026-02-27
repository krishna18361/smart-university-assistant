from flask import request, jsonify
from services.question_service import process_question
from services.db_service import get_all_questions
from services.db_service import get_question_by_id
from services.db_service import update_question_by_id



def get_questions():
    data = get_all_questions()
    return jsonify(data), 200

def get_single_question(question_id):
    result = get_question_by_id(question_id)

    if result is None:
        return jsonify({
            "error": "Question not found"
        }), 404

    return jsonify(result), 200
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
def update_question(question_id):

    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()

    new_question = data.get("question")
    new_answer = data.get("answer")

    if not new_question or not new_answer:
        return jsonify({"error": "Both question and answer required"}), 400

    updated = update_question_by_id(question_id, new_question, new_answer)

    if not updated:
        return jsonify({"error": "Question not found"}), 404

    return jsonify({"message": "Question updated successfully"}), 200