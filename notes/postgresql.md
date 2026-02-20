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