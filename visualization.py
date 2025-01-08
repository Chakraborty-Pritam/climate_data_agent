import matplotlib.pyplot as plt
import pandas as pd

def visualize_data(data):
    data.plot()
    plt.show()

if __name__ == "__main__":
    data = pd.read_csv('C:/Users/pritam/Downloads/GlobalLandTemperaturesByCity/GlobalLandTemperaturesByCity.csv')
    visualize_data(data)
