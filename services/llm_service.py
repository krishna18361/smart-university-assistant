from openai import OpenAI
from config.settings import Config

def get_llm_response(question: str, conversation_history: list = None):
    try:
        client = OpenAI(api_key=Config.OPENAI_API_KEY)
        
        if not Config.OPENAI_API_KEY or Config.OPENAI_API_KEY == "your_openai_api_key_here":
            return "Please set your OpenAI API key in the .env file to use the LLM feature."
        
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
                messages.append({"role": "user", "content": msg["question"]})
                messages.append({"role": "assistant", "content": msg["answer"]})
        
        # Add current question
        messages.append({"role": "user", "content": question})
        
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
        return f"Sorry, I encountered an error: {str(e)}"
