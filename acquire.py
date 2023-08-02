#Import Libraries
import pandas as pd
import numpy as np
import os
from pydataset import data

# Acquire



# Create function to retrieve HR_churn data
def get_HR_churn_data(file_path):
    """
    Load the dataset from the specified CSV file path.
    
    Parameters:
        file_path (str): The full file path to the CSV dataset file.
        
    Returns:
        pandas.DataFrame: The loaded dataset as a DataFrame.
    """
    try:
        # Load the dataset using pandas read_csv function
        df = pd.read_csv(file_path)
        print("Dataset successfully loaded.")
        return df
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error occurred while loading the dataset: {e}")
        return None
