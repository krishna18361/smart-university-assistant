# Smart University Assistant

A premium AI-powered university assistant platform for students.

## Features

- Conversational AI interface
- Chat history management (MongoDB)
- Personalized assistance
- Modern, elegant UI

## Tech Stack

### Backend
- Python 3
- Flask
- MongoDB
- OpenAI API

### Frontend
- React
- Vite
- Tailwind CSS
- Axios

## Installation & Setup

### Prerequisites
- Python 3.9+
- Node.js 18+
- MongoDB 7+

### Backend Setup

1. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
# Copy .env file and update values
cp .env.example .env  # (we created .env directly, so just update OPENAI_API_KEY)
```

4. Update `.env` file with your OpenAI API key:
```env
OPENAI_API_KEY=your_actual_openai_api_key_here
```

5. Make sure MongoDB is running locally on port 27017

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

## Running the Application

### Backend
From project root:
```bash
source venv/bin/activate
python app.py
```
Backend will run on http://localhost:5000

### Frontend
From frontend directory:
```bash
npm run dev
```
Frontend will run on http://localhost:3000

## Project Structure
```
smart-university-assistant/
├── app.py                 # Main Flask app
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables
├── config/                # Configuration settings
│   └── settings.py
├── routes/                # API routes
│   ├── ask_routes.py
│   └── chat_routes.py
├── services/              # Business logic
│   ├── db_service.py      # PostgreSQL service
│   ├── mongo_service.py   # MongoDB service
│   ├── llm_service.py     # OpenAI service
│   └── question_service.py
└── frontend/              # React frontend
    ├── src/
    │   ├── App.jsx
    │   ├── main.jsx
    │   └── index.css
    └── package.json
```
