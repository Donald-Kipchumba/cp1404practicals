from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def display_taxis(taxis):
    """Display details of available taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    """Choose a taxi from the list."""
    display_taxis(taxis)
    while True:
        choice = input("Choose taxi: ")
        try:
            choice = int(choice)
            if 0 <= choice < len(taxis):
                return taxis[choice]
            else:
                print("Invalid taxi choice")
        except ValueError:
            print("Invalid input")


def main():
    print("Let's drive!")
    current_taxi = None
    total_bill = 0

    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    while True:
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()

        if choice == 'q':
            break
        elif choice == 'c':
            current_taxi = choose_taxi(taxis)
            print(f"Bill to date: ${total_bill:.2f}")
        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = float(input("Drive how far? "))
                current_taxi.drive(distance)
                fare = current_taxi.get_fare()
                total_bill += fare
                print(f"Your trip cost you ${fare:.2f}")
                print(f"Bill to date: ${total_bill:.2f}")
        else:
            print("Invalid option")

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


if __name__ == '__main__':
    main()
