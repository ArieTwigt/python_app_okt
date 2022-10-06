from custom_modules.import_functions import import_cars_by_brand
from custom_modules.clean_functions import clean_df

# get the car based on your brand
cars = import_cars_by_brand("opel")

# clean the data frame
cars_cleaned = clean_df(cars)

pass