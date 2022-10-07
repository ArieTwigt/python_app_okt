import requests
import pandas as pd
import sqlite3


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


def import_brand_from_db(brand: str) -> pd.DataFrame:
    '''
    Import the car from the own database
    
    '''

    db_path = "data/data.db"
    con = sqlite3.connect(db_path)

    qry = '''
          SELECT merk, handelsbenaming, catalogusprijs
          FROM cars_brands 
          WHERE merk == ?
          '''

    df_imported_cars = pd.read_sql_query(qry, con=con, params=(brand,))

    return df_imported_cars
