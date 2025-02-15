# routes/threats.py
from fastapi import APIRouter, HTTPException
from models.threats import Threat
from database import execute_read_query, execute_write_query

router = APIRouter()

# 🟢 Create a new threat
@router.post("/threats")
def create_threat(threat: Threat):
    query = """
    CREATE (t:Threat {id: $id, name: $name, description: $description, category: $category, impact_level: $impact_level})
    RETURN t
    """
    execute_write_query(query, threat.dict())
    return {"message": "Threat created successfully"}

# 🔵 Get all threats
@router.get("/threats")
def get_all_threats():
    query = "MATCH (t:Threat) RETURN t"
    threats = execute_read_query(query)
    
    if not threats:
        raise HTTPException(status_code=404, detail="No threats found")
    
    return {"threats": [t["t"] for t in threats]}

# 🔍 Get a specific threat by ID
@router.get("/threats/{threat_id}")
def get_threat(threat_id: str):
    query = "MATCH (t:Threat {id: $id}) RETURN t"
    result = execute_read_query(query, {"id": threat_id})

    if not result:
        raise HTTPException(status_code=404, detail="Threat not found")

    return {"threat": result[0]["t"]}

# 🟠 Update a threat by ID
@router.put("/threats/{threat_id}")
def update_threat(threat_id: str, threat: Threat):
    query = """
    MATCH (t:Threat {id: $id})
    SET t.name = $name, t.description = $description, t.category = $category, t.impact_level = $impact_level
    RETURN t
    """
    result = execute_read_query(query, threat.dict() | {"id": threat_id})

    if not result:
        raise HTTPException(status_code=404, detail="Threat not found")

    return {"message": "Threat updated successfully"}

# 🔴 Delete a threat by ID
@router.delete("/threats/{threat_id}")
def delete_threat(threat_id: str):
    query = "MATCH (t:Threat {id: $id}) DETACH DELETE t"
    execute_write_query(query, {"id": threat_id})
    return {"message": "Threat deleted successfully"}
