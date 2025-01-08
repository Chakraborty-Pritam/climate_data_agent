import pandas as pd
from sklearn.ensemble import IsolationForest


def detect_anomalies(data):
    # Drop non-numeric columns (e.g., date columns)
    data_numeric = data.select_dtypes(include=['number'])

    # Check if there are any numeric columns left
    if data_numeric.empty:
        raise ValueError("No numeric columns found for anomaly detection.")

    # Fit the IsolationForest model
    model = IsolationForest(contamination=0.01)
    data['anomaly'] = model.fit_predict(data_numeric)

    # Return rows with anomalies
    anomalies = data[data['anomaly'] == -1]
    return anomalies


if __name__ == "__main__":
    # Load the dataset
    data = pd.read_csv('C:/Users/pritam/Downloads/GlobalLandTemperaturesByCity/GlobalLandTemperaturesByCity.csv')

    # Detect anomalies
    anomalies = detect_anomalies(data)

    # Print detected anomalies
    print("Detected anomalies:")
    print(anomalies)
