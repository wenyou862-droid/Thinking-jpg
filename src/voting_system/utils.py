def get_positive_int(prompt: str) -> int:
    """Keep asking until the user enters a positive integer."""
    while True:
        value = input(prompt)
        try:
            number = int(value)
            if number <= 0:
                print("Please enter a positive number.")
                continue
            return number
        except ValueError:
            print("That's not a valid number. Please try again.")


def get_non_negative_float(prompt: str) -> float:
    """Keep asking until the user enters a non-negative number."""
    while True:
        value = input(prompt)
        try:
            number = float(value)
            if number < 0:
                print("Price cannot be negative.")
                continue
            return number
        except ValueError:
            print("That's not a valid number. Please try again.")