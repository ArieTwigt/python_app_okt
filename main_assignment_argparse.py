from custom_modules.import_functions import import_cars_by_brand
from custom_modules.export_functions import export_brand_to_csv, export_to_db
import argparse

# define the argument parser
parser = argparse.ArgumentParser()

# add arguments to the arg parser
parser.add_argument('--import_by', 
                    type=str, 
                    required=False, 
                    choices=['brand', 'license'],
                    default='brand',
                    help='Specify the way you want to import the car.')


parser.add_argument('--brand',
                    type=str, 
                    required=False)

parser.add_argument('--license',
                    type=str, 
                    required=False)

parser.add_argument('--color', 
                    type=str, 
                    required=False, 
                    help='Specify the color of the cars you would like to import')

parser.add_argument('--export',
                    type=str,
                    required=False,
                    choices=['db', 'csv', 'print'],
                    default='print',
                    help='Specify how to export the data')


# parse the arguments
args = parser.parse_args()

# execute the code if this is the main script
if __name__ == '__main__':

    # check if it is specified by brand of license plate
    import_by = args.import_by

    # conditional statement for the way to import from the API
    if import_by == 'brand':
        selected_brand = args.brand

        selected_color = args.color
        
        if selected_color == None:
            cars_df = import_cars_by_brand(selected_brand)
        else:
            cars_df = import_cars_by_brand  (selected_brand, color=selected_color)
    else:
        selected_plate = args.license
        #cars_df = get_car_by_license_plate(selected_plate)
 
    # options for exporting
    export_type = args.export

    if export_type == 'csv':
        if import_by == 'brand':
            export_brand_to_csv(cars_df, selected_brand)
        else:
            export_df_license(cars_df, selected_plate)
    elif export_type == 'db':
        export_to_db(cars_df)
    
    else:
        print(cars_df)
