# models/threats.py
from pydantic import BaseModel

# Threat model with 5 properties
class Threat(BaseModel):
    id: str
    name: str
    description: str
    category: str
    impact_level: str
