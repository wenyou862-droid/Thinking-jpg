def add_request(
    requests: list[dict],
    created_by: str,
    reviewers: list[str],
    item: str,
    quantity: int,
    price: float,
    reason: str,
) -> list[dict]:
    """Create a new purchase request and add it to the list."""
    item = item.strip()
    reason = reason.strip()

    if not item:
        raise ValueError("Item cannot be empty.")
    if quantity <= 0:
        raise ValueError("Quantity must be positive.")
    if price < 0:
        raise ValueError("Price cannot be negative.")
    if not reviewers:
        raise ValueError("You must select at least one reviewer.")
    if created_by in reviewers:
        raise ValueError("You cannot be your own reviewer.")

    new_request = {
        "created_by": created_by,
        "reviewers": reviewers,
        "item": item,
        "quantity": quantity,
        "price": price,
        "reason": reason,
        "votes": {},
    }

    return requests + [new_request]