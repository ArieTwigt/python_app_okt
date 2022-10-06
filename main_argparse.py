from custom_modules.calculation_functions import calc_circle
import argparse

# create an argparse instance
parser = argparse.ArgumentParser()

# add arguments to argparse
parser.add_argument("--diameter", type=float, required=True, help="The diameter of the circle")
parser.add_argument("--rounding", type=int, required=False, default=1, help="Round the value")
parser.add_argument("--double", type=int, required=False, default=1, help="Double the result")
parser.add_argument("--export", type=str, required=False, default="no", choices=["yes", "no"], help="Export the file")

# parse the arguments
args = parser.parse_args()

# get the arguments from the args
selected_diameter = args.diameter
selected_rounding = args.rounding
selected_double = args.double
selected_export = args.export


# execute the function
my_size = calc_circle(selected_diameter, double_up=selected_double, rounding=selected_rounding)

# print the result
print(my_size)

# export or not
if selected_export == "yes":
    print("Exporting the data")










#def groet_namen(*args):
#    for name in args:
#        print(f"Hallo {name}")
#
#groet_namen('arie', 'jaap', 'dirk', 'james')
#
#def beschrijving(**kwargs):
#    print(kwargs)
#    for key, value in kwargs.items():
#        print(f"{key} is een {value}")
#
#
#beschrijving(merk="AUDI", vermogen=200, kleur="Wit", opties=['verwarming', 'spiegels'])
#
#pass