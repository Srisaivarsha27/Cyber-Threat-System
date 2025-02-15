# routes/attacker.py
from fastapi import APIRouter, HTTPException
from models.attacker import Attacker
from database import execute_read_query, execute_write_query

router = APIRouter()

# 🟢 Create a new attacker entry
@router.post("/attackers")
def create_attacker(attacker: Attacker):
    query = """
    CREATE (a:Attacker {id: $id, name: $name, description: $description, category: $category, motivation: $motivation})
    RETURN a
    """
    execute_write_query(query, attacker.dict())
    return {"message": "Attacker entry created successfully"}

# 🔵 Get all attackers
@router.get("/attackers")
def get_all_attackers():
    query = "MATCH (a:Attacker) RETURN a"
    attackers = execute_read_query(query)

    if not attackers:
        raise HTTPException(status_code=404, detail="No attackers found")

    return {"attackers": [a["a"] for a in attackers]}

# 🔍 Get a specific attacker by ID
@router.get("/attackers/{attacker_id}")
def get_attacker(attacker_id: str):
    query = "MATCH (a:Attacker {id: $id}) RETURN a"
    result = execute_read_query(query, {"id": attacker_id})

    if not result:
        raise HTTPException(status_code=404, detail="Attacker not found")

    return {"attacker": result[0]["a"]}

# 🟠 Update an attacker entry by ID
@router.put("/attackers/{attacker_id}")
def update_attacker(attacker_id: str, attacker: Attacker):
    query = """
    MATCH (a:Attacker {id: $id})
    SET a.name = $name, a.description = $description, a.category = $category, a.motivation = $motivation
    RETURN a
    """
    result = execute_read_query(query, attacker.dict() | {"id": attacker_id})

    if not result:
        raise HTTPException(status_code=404, detail="Attacker not found")

    return {"message": "Attacker entry updated successfully"}

# 🔴 Delete an attacker entry by ID
@router.delete("/attackers/{attacker_id}")
def delete_attacker(attacker_id: str):
    query = "MATCH (a:Attacker {id: $id}) DETACH DELETE a"
    execute_write_query(query, {"id": attacker_id})
    return {"message": "Attacker entry deleted successfully"}
