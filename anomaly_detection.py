import pandas as pd
from sklearn.ensemble import IsolationForest


def detect_anomalies(data):
   
    data_numeric = data.select_dtypes(include=['number'])

    if data_numeric.empty:
        raise ValueError("No numeric columns found for anomaly detection.")

    model = IsolationForest(contamination=0.01)
    data['anomaly'] = model.fit_predict(data_numeric)

    anomalies = data[data['anomaly'] == -1]
    return anomalies


if __name__ == "__main__":
    data = pd.read_csv('C:/Users/pritam/Downloads/climate_change_dataset.csv')

    anomalies = detect_anomalies(data)

    print("Detected anomalies:")
    print(anomalies)
