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