def main():
    # Set the minimum password length
    min_length = 10

    # Keep asking for a password until it's long enough
    while True:
        # Ask the user for a password
        password = input("Enter a password: ")

        # Check if the password is too short
        if len(password) < min_length:
            print("Password is too short. It should be at least", min_length, "characters long.")
        else:
            break  # The password is good, exit the loop

    # Print asterisks to show the password's length
    print("Password accepted! Here's a visual representation:")
    print("*" * len(password))


if __name__ == "__main__":
    main()
