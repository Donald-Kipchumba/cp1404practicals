def get_numbers():
    """
    Prompt the user for 5 numbers and return them as a list.

    Returns:
        list: A list of 5 numbers entered by the user.
    """
    numbers = []
    for i in range(5):
        while True:
            try:
                number = float(input(f"Enter number {i + 1}: "))
                numbers.append(number)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    return numbers

def analyze_numbers(numbers):
    """
    Analyze a list of numbers and display information about them.

    Args:
        numbers (list): A list of numbers to be analyzed.
    """
    if numbers:
        print(f"The first number is {numbers[0]}")
        print(f"The last number is {numbers[-1]}")
        print(f"The smallest number is {min(numbers)}")
        print(f"The largest number is {max(numbers)}")
        print(f"The average of the numbers is {sum(numbers) / len(numbers)}")
    else:
        print("The list is empty.")


def check_access(username):
    """
    Check if a given username is in the list of authorized usernames.

    Args:
        username (str): The username to check.

    Returns:
        str: "Access granted" if the username is authorized, otherwise "Access denied".
    """
    # List of authorized usernames
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

    if username in usernames:
        return "Access granted"
    else:
        return "Access denied"


def main():
    numbers = get_numbers()
    analyze_numbers(numbers)
    # Prompt the user for their username
    user_input = input("Enter your username: ")

    # Check access using the check_access function and print the result
    result = check_access(user_input)
    print(result)


if __name__ == "__main__":
    main()
