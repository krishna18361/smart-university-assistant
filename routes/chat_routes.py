from flask import request, jsonify
from services.mongo_service import save_chat_history, get_chat_history, get_all_chats, delete_chat
from services.llm_service import get_llm_response
import uuid

def create_new_chat():
    chat_id = str(uuid.uuid4())
    return jsonify({"chat_id": chat_id}), 200

def get_chats():
    chats = get_all_chats()
    return jsonify(chats), 200

def get_chat(chat_id):
    history = get_chat_history(chat_id)
    return jsonify(history), 200

def send_message(chat_id):
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    data = request.get_json()
    question = data.get("question")
    
    if not question:
        return jsonify({"error": "Question is required"}), 400
    
    # Get existing conversation history
    conversation_history = get_chat_history(chat_id)
    
    # Get LLM response
    answer = get_llm_response(question, conversation_history)
    
    # Save to MongoDB
    save_chat_history(chat_id, question, answer)
    
    return jsonify({
        "question": question,
        "answer": answer
    }), 200

def remove_chat(chat_id):
    deleted = delete_chat(chat_id)
    if not deleted:
        return jsonify({"error": "Chat not found"}), 404
    return jsonify({"message": "Chat deleted successfully"}), 200
