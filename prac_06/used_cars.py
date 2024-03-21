"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from car import (Car)


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("my_car", 180)
    my_car.drive(30)
    print(my_car)
    #print(f"Car has fuel: {my_car.fuel}")
    #print(my_car)
    limo = Car("limo", 100)
    limo.add_fuel(20)
    print(limo)
    limo.drive(115)
    print(limo)
    limo.add_fuel(300)
    limo.drive(150)
    print(limo)
    adc = Car("adc", 800)
    adc.drive(4)
    adc.drive(31)
    adc.drive(503)
    adc.add_fuel(30)
    print(adc)



main()