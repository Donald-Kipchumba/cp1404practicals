from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes extra features."""

    flagfall = 4.50  # Class variable

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on the parent class Taxi."""
        super().__init__(name, fuel)
        self.price_per_km *= fanciness
        self.fanciness = fanciness

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi object."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the total price for the taxi trip, including flagfall."""
        return round(super().get_fare() + self.flagfall, 1)
