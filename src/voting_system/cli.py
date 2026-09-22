from .users import add_user
from .storage import load_users, save_users
from .requests import add_request

def main():
    users = load_users()
    requests_list = []
    current_user = None

    while True:
        print("\n1. Create user")
        print("2. List users")
        print("3. Login")
        print("4. Create request")
        print("5. List requests")
        print("6. Exit")
        choice = input("Please enter your choice: ")

        if choice == "1":
            name = input("User name: ")
            try:
                users = add_user(users, name)
                save_users(users)
                print(f"Created user: {name.strip()}")
            except ValueError as error:
                print(error)
        elif choice == "2":
            print("Users:", ", ".join(users) if users else "None yet")
        elif choice == "3":
            name = input("Username: ").strip()
            if name in users:
                current_user = name
                print(f"Logged in as {current_user}")
            else:
                print("User not found.")
        elif choice == "4":
            if current_user is None:
                print("Please login first.")
            else:
                while True:
                    reviewer_input = input("Reviewers (comma separated usernames): ")
                    reviewers = [r.strip() for r in reviewer_input.split(",")]

                    invalid = [r for r in reviewers if r not in users]
                    if invalid:
                        for name in invalid:
                            answer = input(f"User '{name}' doesn't exist. Create now? (y/n): ").strip().lower()
                            if answer == "y":
                                try:
                                    users = add_user(users, name)
                                    save_users(users)
                                    print(f"Created user: {name}")
                                except ValueError as error:
                                    print(error)

                        # check if everybody exits
                        still_invalid = [r for r in reviewers if r not in users]
                        if still_invalid:
                            print(f"Still missing: {', '.join(still_invalid)}. Let's try again.")
                            continue

                    if current_user in reviewers:
                        print("You cannot be your own reviewer. Try again.")
                        continue

                    break
                item = input("What do you want to buy? ")
                quantity = int(input("Quantity: "))
                price = float(input("Price: "))
                reason = input("Reason: ")
                try:
                    requests_list = add_request(
                        requests_list, users, current_user, reviewers, item, quantity, price, reason)
                    print("Request created!")
                except ValueError as error:
                    print(error)
        elif choice == "5":
            if not requests_list:
                print("No requests yet.")
            else:
                for i, req in enumerate(requests_list, start=1):
                    print(f"{i}. {req['item']} x{req['quantity']} - ${req['price']} "
                          f"(by {req['created_by']}, reviewers: {', '.join(req['reviewers'])})")
        elif choice == "6":
            break
        else:
            print("Please choose 1, 2, 3，4，5 or 6.")