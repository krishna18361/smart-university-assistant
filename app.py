from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from config.settings import Config
from routes.ask_routes import ask_question, get_questions, get_single_question, update_question, delete_question
from routes.chat_routes import create_new_chat, get_chats, get_chat, send_message, remove_chat
from models import db, User
from datetime import timedelta
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config.from_object(Config)

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://{Config.DATABASE_CONFIG['user']}:{Config.DATABASE_CONFIG['password']}"
    f"@{Config.DATABASE_CONFIG['host']}:{Config.DATABASE_CONFIG['port']}"
    f"/{Config.DATABASE_CONFIG['database']}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = Config.SECRET_KEY
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=7)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize extensions
db.init_app(app)
jwt = JWTManager(app)
CORS(app)

# Create tables
with app.app_context():
    try:
        db.create_all()
    except Exception as e:
        print(f"Database initialization error: {e}")

# Auth routes
@app.route('/api/auth/signup', methods=['POST'])
def signup():
    data = request.get_json()
    
    if not data or 'email' not in data or 'password' not in data or 'name' not in data:
        return jsonify({"error": "Missing required fields"}), 400
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email already registered"}), 400
    
    user = User(email=data['email'], name=data['name'])
    user.set_password(data['password'])
    
    try:
        db.session.add(user)
        db.session.commit()
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token, user={"name": user.name, "email": user.email}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({"error": "Missing required fields"}), 400
    
    user = User.query.filter_by(email=data['email']).first()
    if not user or not user.check_password(data['password']):
        return jsonify({"error": "Invalid credentials"}), 401
    
    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token, user={"name": user.name, "email": user.email}), 200

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

# Chat routes with file upload support
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
    return send_message(chat_id, app.config['UPLOAD_FOLDER'])

@app.route("/api/chats/<chat_id>", methods=["DELETE"])
def delete_chat_route(chat_id):
    return remove_chat(chat_id)

if __name__ == "__main__":
    app.run(debug=Config.DEBUG)
