# config.py
from neo4j import GraphDatabase

# Neo4j connection settings
URI = "bolt://localhost:7687"  # Update if using Neo4j AuraDB
AUTH = ("neo4j", "empire2026")  # Change credentials as needed

# Create a Neo4j database driver
db = GraphDatabase.driver(URI, auth=AUTH)


