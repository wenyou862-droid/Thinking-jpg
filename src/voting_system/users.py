def add_user(users: list[str], name: str) -> list[str]:
    """Add a new user if the name is not already taken."""
    name = name.strip()

    if not name:
        raise ValueError("Name cannot be empty.")
    if name in users:
        raise ValueError("This user already exists.")

    return users + [name]