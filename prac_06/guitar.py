"""
estimation of time taken = 1 hour
started at 1:50
ened at 2: 32
actually took 42 mins less than expected
"""
class Guitar:
    CURRENT_YEAR = 2024  # define current year for age check

    def __init__(self, name="", year=0, cost=0):
        """declare initial value of information"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """str method returning what to print"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """function getting age of guitar"""
        return self.CURRENT_YEAR - self.year

    def is_vintage(self):
        """returns true if age of guitar is 50+="""
        return self.get_age() >= 50
