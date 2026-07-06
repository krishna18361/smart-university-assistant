from pymongo import MongoClient
from datetime import datetime
from config.settings import Config

def get_mongo_client():
    try:
        client = MongoClient(Config.MONGODB_URI)
        # Verify connection
        client.admin.command('ping')
        return client
    except Exception as e:
        print(f"MongoDB connection failed: {e}")
        return None

def save_chat_history(chat_id, question, answer):
    client = get_mongo_client()
    if not client:
        return False
    
    try:
        db = client[Config.MONGODB_DB_NAME]
        collection = db["chat_history"]
        
        # Save user message
        user_message = {
            "chat_id": chat_id,
            "role": "user",
            "question": question,
            "answer": None,
            "timestamp": datetime.utcnow()
        }
        collection.insert_one(user_message)
        
        # Save assistant message
        assistant_message = {
            "chat_id": chat_id,
            "role": "assistant",
            "question": None,
            "answer": answer,
            "timestamp": datetime.utcnow()
        }
        collection.insert_one(assistant_message)
        
        return True
    except Exception as e:
        print(f"Error saving chat history: {e}")
        return False
    finally:
        client.close()

def get_chat_history(chat_id):
    client = get_mongo_client()
    if not client:
        return []
    
    try:
        db = client[Config.MONGODB_DB_NAME]
        collection = db["chat_history"]
        
        messages = list(collection.find(
            {"chat_id": chat_id},
            {"_id": 0}
        ).sort("timestamp", 1))
        
        return messages
    except Exception as e:
        print(f"Error fetching chat history: {e}")
        return []
    finally:
        client.close()

def get_all_chats():
    client = get_mongo_client()
    if not client:
        return []
    
    try:
        db = client[Config.MONGODB_DB_NAME]
        collection = db["chat_history"]
        
        # Get distinct chat_ids with their first user message and last timestamp
        pipeline = [
            {"$match": {"role": "user"}},
            {
                "$group": {
                    "_id": "$chat_id",
                    "first_question": {"$first": "$question"},
                    "last_timestamp": {"$max": "$timestamp"}
                }
            },
            {
                "$sort": {"last_timestamp": -1}
            }
        ]
        
        chats = list(collection.aggregate(pipeline))
        result = []
        for chat in chats:
            title = chat["first_question"]
            if title:
                title = title[:50] + "..." if len(title) > 50 else title
            else:
                title = "New Chat"
            result.append({
                "chat_id": chat["_id"],
                "title": title,
                "last_updated": str(chat["last_timestamp"])
            })
        
        return result
    except Exception as e:
        print(f"Error fetching chats: {e}")
        return []
    finally:
        client.close()

def delete_chat(chat_id):
    client = get_mongo_client()
    if not client:
        return False
    
    try:
        db = client[Config.MONGODB_DB_NAME]
        collection = db["chat_history"]
        
        result = collection.delete_many({"chat_id": chat_id})
        return result.deleted_count > 0
    except Exception as e:
        print(f"Error deleting chat: {e}")
        return False
    finally:
        client.close()
