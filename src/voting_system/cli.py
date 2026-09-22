from .users import add_user
from .storage import load_users, save_users
from .requests import add_request

def main():
    users = load_users()
    requests_list = []

    while True:
        print("\n1. Create user")
        print("2. List users")
        print("3. Login")
        print("4. Create request")
        print("5. Exit")
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
                item = input("What do you want to buy? ")
                quantity = int(input("Quantity: "))
                price = float(input("Price: "))
                reason = input("Reason: ")
                reviewer_input = input("Reviewers (comma separated usernames): ")
                reviewers = [r.strip() for r in reviewer_input.split(",")]
                try:
                    requests_list = add_request(
                    requests_list, current_user, reviewers, item, quantity, price, reason)
                    print("Request created!")
                except ValueError as error:
                    print(error)
        elif choice == "5":
            break
        else:
            print("Please choose 1, 2, 3，4 or 5.")