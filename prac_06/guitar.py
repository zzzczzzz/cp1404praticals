"""
estimation of time taken = 1 hour
started at 1:50
ened at 2: 32
actually took 42 mins less than expected
"""
class Guitar:
    CURRENT_YEAR = 2024

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        return self.CURRENT_YEAR - self.year

    def is_vintage(self):
        return self.get_age() >= 50
