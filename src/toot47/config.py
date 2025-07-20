import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# --- Environment Variables ---
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASS = os.getenv("NEO4J_PASS", "password")

# --- Paths ---
PROMPTS_DIR = Path(__file__).parent.parent.parent / "prompts"

# --- Prompts ---
def load_system_prompt():
    """Loads the system prompt from prompts/system.md"""
    try:
        with open(PROMPTS_DIR / "system.md", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "You are a helpful AI assistant."

SYSTEM_PROMPT = load_system_prompt() 