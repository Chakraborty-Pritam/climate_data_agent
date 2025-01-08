import pandas as pd
import numpy as np

def validate_data(data):
    # Check for missing values
    if data.isnull().any().any():
        print("Missing values detected.")
        return False
    # Check for data types consistency
    if not all(data.dtypes == data.dtypes.iloc[0]):
        print("Inconsistent data types detected.")
        return False
    return True

if __name__ == "__main__":
    data = pd.read_csv('C:/Users/pritam/Downloads/GlobalLandTemperaturesByCity/GlobalLandTemperaturesByCity.csv')
    if validate_data(data):
        print("Data validation successful.")
    else:
        print("Data validation failed.")
