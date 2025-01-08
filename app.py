from data_validation import validate_data
from anomaly_detection import detect_anomalies
from api_integration import fetch_cds_data
from visualization import visualize_data
from report_generation import generate_report
import pandas as pd


def main():
    # Define the API URL
    api_url = "reanalysis-era5-single-levels"  # Example dataset name

    # Fetch data from the CDS API
    data_file = fetch_cds_data(api_url)

    if data_file:
        # Load the data into a pandas DataFrame
        data = pd.read_csv(data_file)

        # Validate the data
        if validate_data(data):
            # Detect anomalies
            anomalies = detect_anomalies(data)

            # Visualize the data
            visualize_data(data)

            # Generate a report
            report = generate_report(data, anomalies)
            print("Report:")
            print(report)
        else:
            print("Data validation failed.")
    else:
        print("Failed to fetch data from API.")


if __name__ == "__main__":
    main()
