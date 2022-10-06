import os
import pandas as pd
import numpy as np
from datetime import datetime

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


# Exp. list comprehensions
# * names_list = ['arie', 'james', 'lara']
# * [x.upper() for x in names_list]
# * [x.upper() for x in names_list if x[0].lower() == 'a']
# * [x.upper() if x[0] == 'a' else x.replace('a', 'O') for x in names_list]