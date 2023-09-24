def main():
    while True:
        print("\nMain Menu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input("\nChoose an option: ").upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            if 'score' not in locals():
                print("Please get a valid score first.")
            else:
                print_result(score)
        elif choice == "S":
            if 'score' not in locals():
                print("Please get a valid score first.")
            else:
                show_stars(score)
        elif choice == "Q":
            print("Farewell!")
            return
        else:
            print("Invalid option. Please choose again.")


def get_valid_score():
    while True:
        try:
            score = float(input("Enter a score between 0-100: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid input. Please enter a number between 0-100.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def print_result(score):
    print("Your score is", score)


def show_stars(score):
    print('*' * int(score))


if __name__ == "__main__":
    main()
