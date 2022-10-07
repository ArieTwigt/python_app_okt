from cmath import exp
import os
import pandas as pd
import numpy as np
from datetime import datetime
import sqlite3


def export_brand_to_csv(df: pd.DataFrame, brand: str=None, data_folder="data") -> None:
    '''
    Export the DataFrame to a csv file
    '''
    
    if brand is None:
        unique_brands = list(df['merk'].unique())
        brands = [merk for merk in unique_brands if merk != np.nan]
        brand = brands[0]

    # define the current date and time
    current_date_time = datetime.now().strftime("%Y%m%d%H%M%S")
    
    # define the filename
    filename = f"export_{brand}_{current_date_time}.csv"

    # add folder to the filename
    folder = f"data/brands/{brand}"

    if not os.path.exists(folder):
        os.makedirs(folder)

    file_folder_path = f"{folder}/{filename}"

    # export to csv
    print(f"Exporting to csv: {file_folder_path}")
    df.to_csv(file_folder_path, sep=";", index=False)
    print(f"Exported to csv")

    pass


# create a function that writes to the database
def export_to_db(df: pd.DataFrame, export_type: str='brand') -> None:
    '''
    Method for exporting data to the SQLite table

    '''

    # specify the table name
    if export_type == 'brand':
        table_name = 'cars_brands'
    elif export_type == 'license':
        table_name = 'license'
    else:
        raise ValueError(f"Param 'export_type' should be one of 'brand' or 'licence', got {export_type}")


    # specify and define the database path
    db_path = "data/data.db"
    con = sqlite3.connect(db_path)  

    # create a sub seleciton of columns
    selected_columns = ['merk', 'handelsbenaming', 'catalogusprijs', 'aantal_cilinders', 'eerste_kleur']
    df_filtered = df[selected_columns]

    # export the DataFrame
    print("Exporting to database")
    df_filtered.to_sql(table_name, con, if_exists='append', index=False)
    print("Exported to database")





# Exp. list comprehensions
# * names_list = ['arie', 'james', 'lara']
# * [x.upper() for x in names_list]
# * [x.upper() for x in names_list if x[0].lower() == 'a']
# * [x.upper() if x[0] == 'a' else x.replace('a', 'O') for x in names_list]


# Link: https://learn.microsoft.com/en-us/azure/azure-sql/database/connect-query-python?view=azuresql
#
# connectionstring = 'mssql+pyodbc://{uid}:{password}@{server}:1433/{database}?driver={driver}'.format(
#         uid=AZUREUID,
#         password=AZUREPWD,
#         server=AZURESRV,
#         database=AZUREDB,
#         driver=DRIVER.replace(' ', '+'))
#     
# engn = create_engine(connectionstring)
