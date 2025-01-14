import matplotlib.pyplot as plt
import pandas as pd

def visualize_data(data):
    data.plot()
    plt.show()

if __name__ == "__main__":
    data = pd.read_csv('C:/Users/pritam/Downloads/climate_change_dataset.csv')
    visualize_data(data)
