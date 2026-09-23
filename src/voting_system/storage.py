import json
from pathlib import Path

DATA_FILE = Path("users_data.json")
REQUESTS_FILE = Path("requests_data.json")

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

def load_requests() -> list:
    """Load requests from the data file, or return an empty list if it doesn't exist."""
    if not REQUESTS_FILE.exists():
        return []
    with open(REQUESTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_requests(requests_list: list) -> None:
    """Save the requests list to the data file."""
    with open(REQUESTS_FILE, "w", encoding="utf-8") as f:
        json.dump(requests_list, f, ensure_ascii=False, indent=2)