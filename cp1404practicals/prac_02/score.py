import random


def determine_score_status(score):
    """Determine the status based on the score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"


def main():
    """
    Main function to interactively input scores and generate a random score.
    It prints the results for user input and the random score.
    """
    while True:
        user_input = input("Enter score (or press Enter to quit): ")

        if user_input == "":
            break

        try:
            score = float(user_input)
            result = determine_score_status(score)
            print(result)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Generate a random score and print the result
    random_score = random.randint(0, 100)
    print(f"Random Score: {random_score}")
    random_result = determine_score_status(random_score)
    print(f"Result for Random Score: {random_result}")


if __name__ == "__main__":
    main()
