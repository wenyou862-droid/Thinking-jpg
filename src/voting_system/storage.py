import json
from pathlib import Path

DATA_FILE = Path("users_data.json")

def load_users() -> list:
    """Load users from the data file, or return an empty list if it doesn't exist."""
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_users(users: list) -> None:
    """Save the users list to the data file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=2)