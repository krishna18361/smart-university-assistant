from openai import OpenAI
from config.settings import Config
import random
import os

# Dummy responses for testing without OpenAI API key
dummy_responses = [
    "Great question! Here's what I know about university policies: Attendance is mandatory for all courses, with a minimum requirement of 75% to be eligible for exams.",
    "Excellent query! Scholarships are available based on both merit and financial need. You can apply through the university's student portal.",
    "That's a common question! Exam schedules are usually released 2 weeks before the exam period begins. Check your student dashboard for updates.",
    "Interesting! The university library is open from 8 AM to 10 PM on weekdays, and 10 AM to 6 PM on weekends.",
    "Perfect question! For student guidance, you can visit the academic advising office in Building A, Room 101, or book an appointment online."
]

def get_llm_response(question: str, conversation_history: list = None, file_info=None):
    try:
        # Check if API key is set
        if not Config.OPENAI_API_KEY or Config.OPENAI_API_KEY == "your_openai_api_key_here":
            # Use dummy response for testing
            response_text = random.choice(dummy_responses)
            if file_info:
                response_text = f"I've received your file '{file_info['filename']}'. " + response_text
            return response_text
        
        client = OpenAI(api_key=Config.OPENAI_API_KEY)
        
        # Prepare messages
        messages = [
            {
                "role": "system",
                "content": "You are a helpful university assistant. Provide accurate, concise information about academic matters, courses, exams, attendance, scholarships, campus facilities, and student guidance."
            }
        ]
        
        # Add conversation history if available
        if conversation_history:
            for msg in conversation_history:
                if msg.get("role") == "user" and msg.get("question"):
                    messages.append({"role": "user", "content": msg["question"]})
                elif msg.get("role") == "assistant" and msg.get("answer"):
                    messages.append({"role": "assistant", "content": msg["answer"]})
        
        # Add current question and file info
        user_content = question
        if file_info:
            user_content = f"[File: {file_info['filename']}]\n\n{question}"
        
        messages.append({"role": "user", "content": user_content})
        
        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=1000
        )
        
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"LLM Error: {e}")
        response_text = random.choice(dummy_responses)
        if file_info:
            response_text = f"I've received your file '{file_info['filename']}'. " + response_text
        return response_text  # Fallback to dummy on error
