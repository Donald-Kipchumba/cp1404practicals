import re


def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+'
    return re.match(pattern, email)


def extract_name(email):
    name = email.split('@')[0]
    return name.title()


def main():
    email_dict = {}

    while True:
        email = input("Email: ")
        if not email:
            break

        if not validate_email(email):
            print("Invalid email. Please enter a valid email address.")
            continue

        name = extract_name(email)
        confirmed_name = input(f"Is your name {name}? (Y/n) ").strip()

        if confirmed_name and confirmed_name.lower() != 'y':
            name = input("Name: ").strip()

        email_dict[email] = name

    print("\nList of users:")
    for email, name in email_dict.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    print("Welcome to the User Email and Name Entry Program.")
    print("Please follow the instructions below:")
    print("1. Enter your email address when prompted. Example: Email: john@example.com")
    print("2. Confirm if the extracted name is correct by typing Y (for yes) or n (for no) and then pressing Enter.")
    print("   If the name is correct, you can just press Enter.")
    print("   If not, provide the correct name and press Enter.")
    print("3. Repeat steps 1 and 2 for each user.")
    print(
        "4. To finish entering emails and see the list of users, simply press Enter when asked for an "
        "email (without providing any input).")
    main()
