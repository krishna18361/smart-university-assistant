#Flask app file
from flask import Flask, request, jsonify

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

    # Step 1: Check if request has JSON
    if not request.is_json:
        return jsonify({
            "error": "Request must be JSON"
        }), 400

    # Step 2: Get JSON data
    data = request.get_json()

    # Step 3: Check if question exists
    question = data.get("question")

    if not question:
        return jsonify({
            "error": "Question is required"
        }), 400

    # Step 4: Check question type
    if not isinstance(question, str):
        return jsonify({
            "error": "Question must be a string"
        }), 400

    # Step 5: Dummy response
    answer = "This is a dummy response. Validation successful."

    return jsonify({
        "question": question,
        "answer": answer
    }), 200


if __name__ == "__main__":
    app.run(debug=True)
