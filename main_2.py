from custom_modules.import_functions import import_cars_by_brand
from custom_modules.clean_functions import clean_df
from custom_modules.export_functions import export_brand_to_csv, export_to_db

# get the brand from the promt
selected_brand = input("Select a brand:\n")

# get the car based on your brand
cars = import_cars_by_brand(selected_brand)

# clean the data frame
cars_cleaned = clean_df(cars)

# export the data frame to a csv
export_brand_to_csv(cars_cleaned)

# export the data to the database
export_to_db(cars_cleaned, export_type="brand")

pass