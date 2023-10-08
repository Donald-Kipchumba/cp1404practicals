import random

NUM_QUICK_PICKS = 5
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_QUICK_PICK = 6

def generate_quick_pick():
    """Generate a single quick pick (list of 6 unique, sorted numbers)."""
    quick_pick = sorted(random.sample(range(MIN_NUMBER, MAX_NUMBER + 1), NUMBERS_PER_QUICK_PICK))
    return quick_pick

def main():
    try:
        num_quick_picks = int(input("How many quick picks? "))
        if num_quick_picks < 1:
            print("Please enter a positive number.")
            return

        for X in range(num_quick_picks):
            quick_pick = generate_quick_pick()
            print(" ".join(map(str, quick_pick)))

    except ValueError:
        print("Invalid input. Please enter a valid number.")


main()
