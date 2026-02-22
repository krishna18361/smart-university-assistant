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