import pandas as pd

def generate_report(data, anomalies):
    report = {
        'total_records': len(data),
        'missing_values': data.isnull().sum().sum(),
        'anomalies_detected': len(anomalies)
    }
    return report

if __name__ == "__main__":
    data = pd.read_csv('C:/Users/pritam/Downloads/climate_change_dataset.csv')
    anomalies = pd.read_csv('C:/Users/pritam/Downloads/climate_change_dataset.csv')
    report = generate_report(data, anomalies)
    print("Report:")
    print(report)
