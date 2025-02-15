# database.py
from config import db

# Function to execute a read query
def execute_read_query(query, parameters={}):
    with db.session() as session:
        return session.run(query, parameters).data()

# Function to execute a write query
def execute_write_query(query, parameters={}):
    with db.session() as session:
        session.run(query, parameters)
