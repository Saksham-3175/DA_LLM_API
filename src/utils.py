import pandas as pd

def clean_data(df):
    """
    Cleans the input DF by handling missing values and standardizing the data.
    """
    try:
        #Replacing missing values with zeros for numeric fields
        df.fillna(0, inplace = True)
        #Additional cleaning logic can be added here
        return df
    except Exception as e:
        raise Exception(f"Error Cleaning data: {e}")