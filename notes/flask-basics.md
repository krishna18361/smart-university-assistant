# Flask Basics
## What is Flask?
Flask is a Python web framework used to build backend servers and APIs./Flask is a tool that lets Python act as a server.
Normally Python runs scripts and stops.
It allows Python to:
- Receive requests/(Wait for requests)
- Process logic/(Process requests)
- Send responses

Flow:
Client → Flask → Function → Response
Browser → Flask → Your function → Response → Browser
--------------------------------------------------------------------------------------------
## What is a Route?
A route connects a URL to a Python function.
/ask → ask() function
Example:
```python
@app.route("/")
def home():
    return "Hello"
When user visits:
http://127.0.0.1:5000/

Flask runs the home() function.

## How API Accept data
data = request.get_json()
This allows your system to receive user input.
This is essential for your assistant.||||
----------------------------------------------------------------------------------------------
## What is request.get_json()?
It extracts JSON data sent by the client.
Example request:
{
"question": "What is attendance?"
}
Code:
data = request.get_json()
Now data is a Python dictionary.
------------------------------------------------------------------------------------------------
## What is jsonify()?
jsonify converts Python dictionary into JSON response.
Example:
return jsonify({"answer": "Hello"})
Response becomes JSON.
Flask converts Python → JSON → sends response.
How APIs send responses
You learned:
return jsonify({...})
This allows your backend to respond properly.
--------------------------------------------------------------------------------------------------
## DAY-1
What we implemented today
Routes:
/
/health
/ask
Purpose:
Foundation of Smart University Assistant backend.

What the Browser Does by Default
When you type a URL in the browser and press Enter,
the browser sends a:
GET request
But your route only allows:
POST request
So Flask says:
“GET is not allowed here” → Method Not Allowed (405)
This is correct behavior. Your code is working properly.

Difference Between GET and POST (Simple)
#GET
-Used to retrieve data
-Used when opening URLs in browser
-Example: /health
#POST
-Used to send data
-Used for forms, JSON, APIs
-Example: /ask

## how backend works
Client → Flask → Route → Function → Response
Server --> Application --> Database  here server is a computer that recieves request from a client 
and this computer runs application that contains logic about how to respond different clients request 
and database is where all the information is stored application accesses the database to extract all information 
that it needs and generate the proper response for client the client and server communicate with each other 
using an API[APPLICATION PROGRAM INTERFACE]- this API contains information about how client should make request 
and how the server must respond to the specific request 
--------------------------------------------------------------------------------------------------
## Input Validation day-2
Input validation ensures backend receives correct data.
Example checks:
- Request must be JSON
- Question must exist
- Question must be string
how to protect your backend from bad input and make it behave like a real system.
Instead of crashing or behaving silently, your backend now tells the client clearly:
This prevents crashes and invalid processing.
400 → Bad Request
200 → Success
User → Validation → Processing → Response
How to make your backend safe, reliable, and ready for real-world input.
--------------------------------------------------------------------------------------------------
# Day 3 — Project Structure and Route Separation
## What problem existed before?
Before Day 3, all code was inside app.py.
Structure:
app.py → contained routes and logic
This works for small apps but becomes messy as project grows.
Problems:
- Hard to maintain
- Hard to scale
- Difficult to add database logic later
## What we did on Day 3
We created a new folder:
routes/
and moved ask route logic into:
routes/ask_routes.py
## New structure
smart-university-assistant/
│
├── routes/
│   └── ask_routes.py
│
├── app.py
## Responsibilities now
app.py:
- Starts Flask server
- Registers routes
- Connects routes to functions
ask_routes.py:
- Contains actual route logic
- Handles validation
- Processes question
## How route flow works now
User sends request:
POST /ask
Flow:
Client → app.py → ask_routes.py → Response
## Why this is important
This makes backend:
- Clean
- Modular
- Scalable
- Easy to maintain
## Project perspective
This structure prepares the system for:
- PostgreSQL integration
- MongoDB integration
- LLM integration
Without clean structure, adding database would become messy.
-------------------------------------------------------------------------------------------------
# Day 4 — Service Layer Introduction
## What is Service Layer?
Service layer contains business logic of the application.
Routes should only handle HTTP requests.
Services handle processing logic.
## New Architecture
app.py → registers routes
routes/ → handles HTTP request
services/ → handles business logic
## Flow
Client → route → service → response
## Why service layer is important
This prepares project for:
- PostgreSQL integration
- MongoDB integration
- LLM integration
Service layer keeps logic separate from routes.
------------------------------------------------------------------------------
# Day 5 — Configuration Layer and Final Flask Architecture
Today we added a configuration layer to our Smart University Assistant backend.
We created a new folder:
config/
and a new file:
config/settings.py
This file stores application settings such as:
- App name
- Version
- Debug mode
- Database configuration (for future PostgreSQL integration)
This completes the Flask phase and prepares the project for database integration.
## Why configuration layer is needed
Before Day 5, configuration values were written directly inside app.py.
Example:
debug=True
This is not good for large applications because:
- Hard to manage settings
- Hard to change settings later
- Database configuration would become messy
Configuration layer solves this problem by centralizing all settings.
## What is configuration layer (simple explanation)
Configuration layer is a separate place where application settings are stored.
Instead of writing settings in app.py, we store them in:
config/settings.py
app.py loads settings from config file.
This makes application clean and scalable.
## What we implemented
We created file:
config/settings.py
Code:
class Config:
    APP_NAME = "Smart University Assistant"
    DEBUG = True
    VERSION = "1.0.0"
    DATABASE_CONFIG = {
        "host": "localhost",
        "port": 5432,
        "database": "university_assistant",
        "user": "postgres",
        "password": "password"
    }
This class stores all application configuration.
## How app.py uses configuration
We imported Config into app.py:
from config.settings import Config
Then used it:
app.config["APP_NAME"] = Config.APP_NAME
app.config["VERSION"] = Config.VERSION
app.config["DEBUG"] = Config.DEBUG
This connects configuration layer to Flask app.
## New project architecture after Day 5
smart-university-assistant/
│
├── app.py              → starts Flask server
│
├── routes/             → handles HTTP requests
│   └── ask_routes.py
│
├── services/           → contains business logic
│   └── question_service.py
│
├── config/             → contains application configuration
│   └── settings.py
│
├── notes/
│
└── venv/
This is professional backend architecture.
## Request flow after Day 5
Client sends request:
POST /ask
Flow:
Client → app.py → routes/ask_routes.py → services/question_service.py → Response
Configuration is loaded from config/settings.py
## Why __init__.py file was needed
We created:
__init__.py
inside:
config/
routes/
services/
This tells Python these folders are packages.
Without __init__.py, Python cannot import files from folders.
## What we learned today
We learned:
1. What is configuration layer
2. How to store application settings
3. How to load configuration into Flask
4. How professional backend architecture works
5. How to prepare backend for database integration
--------------------------------------------------------------------------------------
