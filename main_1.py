from custom_modules.calculation_functions import calc_circle

my_diameter = float(input("Voer de diameter in:\n"))


my_size = calc_circle(my_diameter, rounding=1)

print(my_size)