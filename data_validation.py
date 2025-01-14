import pandas as pd


def validate_data(data):
    # Check for missing values
    if data.isnull().any().any():
        print("Missing values detected.")
        return False

    # Check if numeric columns contain valid numeric data
    for column in data.select_dtypes(include=['number']).columns:
        if not pd.api.types.is_numeric_dtype(data[column]):
            print(f"Invalid data type in column '{column}'. Expected numeric data.")
            return False

    print("Data validation successful.")
    return True

