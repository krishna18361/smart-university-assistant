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
