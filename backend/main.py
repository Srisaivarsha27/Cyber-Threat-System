# main.py
from fastapi import FastAPI
from routes import threats, malware, vulnerability, attacker  # Import all routes

app = FastAPI()

# Include routers for threats, malware, vulnerabilities, and attackers
app.include_router(threats.router)
app.include_router(malware.router)
app.include_router(vulnerability.router)
app.include_router(attacker.router)

# Root endpoint
@app.get("/")
def root():
    return {"message": "Cyber Threat Intelligence API is running!"}
