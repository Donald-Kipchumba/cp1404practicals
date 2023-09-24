def main():
    # Set the minimum password length
    min_length = 8

    # Get a valid password from the user
    password = get_password(min_length)

    # Print asterisks to show the password's length
    print_password_length(password)

def get_password(min_length):
    while True:
        # Ask the user for a password
        password = input("Enter a password: ")

        # Check if the password is too short
        if len(password) < min_length:
            print("Password is too short. It should be at least", min_length, "characters long.")
        else:
            return password  # Return the valid password

def print_password_length(password):
    print("Password accepted! Here's a visual representation:")
    print("*" * len(password))

if __name__ == "__main__":
    main()
