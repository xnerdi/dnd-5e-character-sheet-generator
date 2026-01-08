# Import necessary libraries
from fastapi import FastAPI, HTTPException, status, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the D&D 5e (2014) Character Sheet Generator!"}

# List all characters
@app.get("/api/v1/characters")
def list_characters():
    return {"characters": [...]}

# Get a specific character
@app.get("/api/v1/characters/{character_id}")
def get_character(character_id:int = Path(..., title="Character ID", description="ID of the character to retrieve")):
    if character_id not in characters:
        raise HTTPException(status_code=404, detail="Character not found")
    return {"character": characters[character_id]}
