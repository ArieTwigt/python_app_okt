import pandas as pd


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
    df['aantal_cilinders'] = df['aantal_cilinders'].astype(int)
    df['catalogusprijs'] = df['catalogusprijs'].astype(float)

    # lege waarden

    
    # filters

    pass


'''

# Overzicht van DataFrame:
* df.info() --> Technische informatie over de DataFrame

# Kolommen selecteren in een DataFrame
df['kolom_naam']

'''