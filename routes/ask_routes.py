from flask import request, jsonify

def ask_question():

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

    answer = "This is a dummy response. Validation successful."

    return jsonify({
        "question": question,
        "answer": answer
    }), 200
