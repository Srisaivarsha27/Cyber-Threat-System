# models/attacker.py
from pydantic import BaseModel

# Attacker model with 5 properties
class Attacker(BaseModel):
    id: str
    name: str
    description: str
    category: str
    motivation: str
