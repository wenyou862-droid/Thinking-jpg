from .users import add_user
from .storage import load_users, save_users

def main():
    users = load_users()

    while True:
        print("\n1. Create user")
        print("2. List users")
        print("3. Exit")
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
            break
        else:
            print("Please choose 1, 2, or 3.")