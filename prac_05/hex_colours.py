"""
COLOR_TO_CODE = {"Ash Grey": "#b2beb5", "Asparagus": "#87a96b", "Azure1": "#f0ffff", "Blond": "#faf0be",
                "Blue Green": "#0d98ba", "Coffee": "#6f4e37", "Copper": "#b87333", "Moccasin": "#ffe4b5",
                "Mulberry": "#c54b8c", "Persian Green": "#00a693"}

print COLOR_TO_CODE

color_name = input get color

whlie color_name != ""
    try:
        print color_name is color code
    execpt keyerror
        print invalid color name
    color_name = input get color
"""

COLOR_TO_CODE = {"Ash Grey": "#b2beb5", "Asparagus": "#87a96b", "Azure1": "#f0ffff", "Blond": "#faf0be",
                 "Blue Green": "#0d98ba", "Coffee": "#6f4e37", "Copper": "#b87333", "Moccasin": "#ffe4b5",
                 "Mulberry": "#c54b8c", "Persian Green": "#00a693"}

print(COLOR_TO_CODE)

color_name = input("Enter color : ").title()

while color_name != "":
    try:
        print(f"Colour code of {color_name} is {COLOR_TO_CODE[color_name]}")
    except KeyError:
        print("Invalid color name")
    color_name = input("Enter color : ").title()
