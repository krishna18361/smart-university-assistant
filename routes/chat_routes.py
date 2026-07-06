from flask import request, jsonify
from services.mongo_service import save_chat_history, get_chat_history, get_all_chats, delete_chat
from services.llm_service import get_llm_response
import uuid
import os
from werkzeug.utils import secure_filename

def create_new_chat():
    chat_id = str(uuid.uuid4())
    return jsonify({"chat_id": chat_id}), 200

def get_chats():
    chats = get_all_chats()
    return jsonify(chats), 200

def get_chat(chat_id):
    history = get_chat_history(chat_id)
    return jsonify(history), 200

def send_message(chat_id, upload_folder):
    question = request.form.get("question")
    file = request.files.get("file")
    
    if not question:
        return jsonify({"error": "Question is required"}), 400
    
    file_info = None
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(upload_folder, filename)
        file.save(filepath)
        file_info = {"filename": filename, "path": filepath}
    
    # Get existing conversation history
    conversation_history = get_chat_history(chat_id)
    
    # Get LLM response
    answer = get_llm_response(question, conversation_history, file_info)
    
    # Save to MongoDB
    save_chat_history(chat_id, question, answer, file_info)
    
    return jsonify({
        "question": question,
        "answer": answer,
        "file": file_info
    }), 200

def remove_chat(chat_id):
    deleted = delete_chat(chat_id)
    if not deleted:
        return jsonify({"error": "Chat not found"}), 404
    return jsonify({"message": "Chat deleted successfully"}), 200
