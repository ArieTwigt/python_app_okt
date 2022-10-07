import pandas as pd
import numpy as np


def clean_df(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Function to clean a pandas DataFrame:
    * right data types
    * empty values for float and int columns

    Parameters:
    * data frame

    Returns:
    * cleaned data frame
    
    '''

    # Convert to the right data types
    df['aantal_cilinders'] = df['aantal_cilinders'].astype(float)
    df['catalogusprijs'] = df['catalogusprijs'].astype(float)

    # lege waarden
    df['aantal_cilinders'] = df['aantal_cilinders'].fillna(0)

    df['aantal_cilinders'] = np.where(np.isnan(df['aantal_cilinders']), # evaluatie/vergelijking
                                     float(0.0),                     # als True de uitkomst is --> Vervang met 
                                     df['aantal_cilinders'] )  # als False de uitkomst is --> Behoud originele waarde
      
    df['catalogusprijs'] = np.where(np.isnan(df['catalogusprijs']), # evaluatie/vergelijking
                                     float(0.0),                     # als True de uitkomst is --> Vervang met 
                                     df['catalogusprijs'] )  # als False de uitkomst is --> Behoud originele waarde
      
    #
    df['aantal_cilinders'] = df['aantal_cilinders'].astype(int)

    df_filtered = df.query("catalogusprijs > 0")

    # calculated column aanmaken
    df_filtered['prijs_per_cilinder'] = df_filtered['catalogusprijs'] /  df_filtered['aantal_cilinders']

    # sorteren van een dataframe
    df_filtered.sort_values(by="prijs_per_cilinder", ascending=False)
    

    return df_filtered


'''

# Overzicht van DataFrame:
* df.info() --> Technische informatie over de DataFrame

# Kolommen selecteren in een DataFrame
df['kolom_naam']

# Beschrijving
* df['aantal_cilinders'].unique()
* df['aantal_cilinders'].value_counts()

# filters, only cars with a price higher than 0
exclude_colors = ['N.v.t.', 'Niet geregistreerd']
df_filtered = df.query("catalogusprijs > 0 \
                        & aantal_cilinders == 4 \
                        & eerste_kleur != @exclude_colors")
'''