from unreliable_car import UnreliableCar


def main():
    my_car = UnreliableCar("Unreliable", 100, 50)
    print(my_car)
    distance = int(input("Drive how far? "))
    distance_driven = my_car.drive(distance)
    print(f"The car drove {distance_driven} km.")
    print(my_car)


if __name__ == '__main__':
    main()
