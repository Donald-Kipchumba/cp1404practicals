import random
from car import Car


class UnreliableCar(Car):
    """Represent an UnreliableCar object, a type of Car with reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialize an UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car only if a random number is less than reliability."""
        if random.uniform(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
