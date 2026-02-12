#Flask app file
from flask import Flask, request, jsonify

# Create Flask application
app = Flask(__name__)

# Route 1: Home route
@app.route("/")
def home():
    return "Smart University Assistant API is running"

# Route 2: Health route
@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "Smart University Assistant"
    })

# Route 3: Ask route
@app.route("/ask", methods=["GET","POST"])
def ask():

    # Get JSON data from request
    data = request.get_json()

    # Extract question from JSON
    question = data.get("question")

    # Dummy answer (AI will come later)
    answer = "This is a dummy response. AI integration will come later."

    # Send response
    return jsonify({
        "question": question,
        "answer": answer
    })

# Run server
if __name__ == "__main__":
    app.run(debug=True)
