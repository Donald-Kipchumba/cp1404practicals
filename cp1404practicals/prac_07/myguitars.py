from guitar import Guitar
import os

import os

current_directory = os.getcwd()
print("Current directory:", current_directory)


def load_guitars():
    guitars = []
    with open('guitar.csv', 'r') as file:
        for line in file:
            data = line.strip().split(',')
            name, year, cost = data[0], int(data[1]), float(data[2])
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
    return guitars


def display_guitars(guitars):
    print("All Guitars:")
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")
    print()


def write_guitars(guitars):
    with open('guitars.csv', 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


def main():
    guitars = load_guitars()
    display_guitars(guitars)

    # Sorting guitars by year (oldest to newest) using sorted() function
    guitars = sorted(guitars)
    print("Guitars sorted by year:")
    display_guitars(guitars)

    # Get user input for new guitars
    while True:
        name = input("Enter the name of the guitar (press Enter to exit): ")
        if name == "":
            break
        year = int(input("Enter the year: "))
        cost = float(input("Enter the cost: "))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)

    # Sorting after adding new guitars
    guitars = sorted(guitars)
    write_guitars(guitars)
    print("Updated guitars have been written to guitars.csv.")

    # Read and display all guitars again
    print("\nAll Guitars after update:")
    guitars = load_guitars()
    display_guitars(guitars)

if __name__ == '__main__':
    main()

