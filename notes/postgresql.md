# Day 6 — PostgreSQL Installation
Today I installed PostgreSQL database system.
PostgreSQL is used to store application data permanently.
Without database, backend forgets everything after response.
With PostgreSQL, backend can store:
- student questions
- answers
- chat history
Database created:
university_assistant
Command used:
CREATE DATABASE university_assistant;
PostgreSQL will be connected to Flask backend in next phase.
-----------------------------------------------------------------------------------
# Day 7 — Flask PostgreSQL Connection
Installed psycopg2 driver.
Created db_service.py.
Flask backend can now connect to PostgreSQL database.
Connection tested successfully.
This prepares backend for storing data.
-------------------------------------------------------------------------------------
# Day 8 — Created questions table and storing data

Created questions table in PostgreSQL.

Backend now stores student questions and answers.

Database is now actively used by Flask backend.
----------------------------------------------------------------------------------------
# Day 9 — Fetching Data from Database

Created get_all_questions() function.

Added GET /questions route.

Backend can now retrieve stored questions.

System now supports both INSERT and SELECT operations.
-------------------------------------------------------------------------------------------
---

# Day 10 — Fetch Single Question by ID

## What we implemented

Added functionality to retrieve a specific question using its ID.

New endpoint:

GET /questions/<id>

Example:

GET /questions/1

Returns the question with ID = 1.


## Backend Changes

1. Added get_question_by_id() in db_service.py

This function:
- Connects to PostgreSQL
- Executes SELECT query with WHERE id = %s
- Returns single row using cursor.fetchone()

2. Added get_single_question() in ask_routes.py

This function:
- Calls get_question_by_id()
- Returns 404 error if record not found
- Returns JSON response if record exists


## Error Handling Added

If question does not exist:

{
  "error": "Question not found"
}

Status code: 404


## What I Learned

- How to use dynamic route parameters in Flask
- How to fetch single row using fetchone()
- How to handle 404 errors properly
- Importance of importing functions correctly
- How Python namespace works
- --------------------------------------------------------------------------------
---

# Day 11 — Update Question Endpoint (PUT)

## What was implemented

Added functionality to update an existing question and answer using its ID.

New endpoint:

PUT /questions/<id>

Example:

PUT /questions/1


## Backend Changes

1. Added update_question_by_id() in db_service.py

This function:
- Connects to PostgreSQL
- Executes SQL UPDATE query
- Uses cursor.rowcount to check if record exists
- Returns True if updated, False if not found

SQL used:

UPDATE questions
SET question = %s,
    answer = %s
WHERE id = %s;


2. Added update_question() in ask_routes.py

This function:
- Validates JSON request
- Ensures both question and answer are provided
- Calls update_question_by_id()
- Returns 404 if record not found
- Returns success message if updated


## Important Concepts Learned

- How to use PUT method in Flask
- How SQL UPDATE works
- What cursor.rowcount does
- How to implement proper 404 handling
- How dynamic route parameters work
  Example: /questions/<int:question_id>


## Example Request

curl -X PUT http://127.0.0.1:5000/questions/1 \
-H "Content-Type: application/json" \
-d '{"question":"Updated","answer":"Updated answer"}'


## API Status After Day 11

POST   /ask              → Create  
GET    /questions        → Read all  
GET    /questions/<id>   → Read one  
PUT    /questions/<id>   → Update  

System now supports:
CREATE + READ + UPDATE