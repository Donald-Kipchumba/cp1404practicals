class Band:
    """Band class for storing details of a band."""

    def __init__(self, name):
        """Initialize a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({self.musicians})"

    def __repr__(self):
        """Return a string representation of a Band, showing the variables."""
        return str(vars(self))

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each musician playing their first (or no) instrument."""
        output = []
        for musician in self.musicians:
            output.append(musician.play())
        return "\n".join(output)


if __name__ == '__main__':
    from musician import Musician
    from guitar import Guitar

    # Test the Band class
    band = Band("Extreme")
    nuno = Musician("Nuno Bettencourt")
    nuno.add(Guitar("Washburn N4", 1990, 2499.95))
    nuno.add(Guitar("Takamine acoustic", 1986, 1200.0))
    band.add(nuno)
    band.add(Musician("Gary Cherone"))
    pat = Musician("Pat Badger")
    pat.add(Guitar("Mouradian CS-74 Bass", 2009, 1500.0))
    band.add(pat)
    kevin = Musician("Kevin Figueiredo")
    band.add(kevin)

    print("band (str)")
    print(band)
    print("band.play()")
    print(band.play())
