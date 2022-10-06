import requests
import pandas as pd


def import_cars_by_brand(brand:str) -> pd.DataFrame:
    '''
    Returns a list of cars from the RDW API

    Parameters:
    * brand

    Returns:
    * List of cars
    
    '''
    
    # explicit is better than implicit
    brand_upper = brand.upper()

    # define the endpoint
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand_upper}"

    # execute the request
    response = requests.get(endpoint)

    # get the content from the response
    cars_list = response.json()
    
    # convert the list to a pandas DataFrame
    cars_df = pd.DataFrame(cars_list)

    return cars_df