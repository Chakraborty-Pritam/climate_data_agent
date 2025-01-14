from flask import Flask, render_template_string
from data_validation import validate_data
from anomaly_detection import detect_anomalies
from api_integration import fetch_openweathermap_data
import pandas as pd
import os
import plotly.express as px

# Initialize Flask app
app = Flask(__name__)


def fetch_and_process_data(location="London"):
    """
    Fetch data from the OpenWeatherMap API and process it.
    """
    # Fetch data from the API
    data = fetch_openweathermap_data(location)

    if data:
        # Convert the API response to a pandas DataFrame
        weather_data = {
            "temperature": [data["main"]["temp"]],
            "humidity": [data["main"]["humidity"]],
            "pressure": [data["main"]["pressure"]],
            "wind_speed": [data["wind"]["speed"]],
            "timestamp": [data["dt"]],  # Unix timestamp
        }
        df = pd.DataFrame(weather_data)

        # Validate the data
        if validate_data(df):
            # Detect anomalies
            anomalies = detect_anomalies(df)

            # Generate a report
            report = {
                'total_records': len(df),
                'missing_values': df.isnull().sum().sum(),
                'anomalies_detected': len(anomalies)
            }

            # Create a Plotly visualization
            fig = px.line(df, y=df.columns, title="Climate Data Visualization")
            graph_html = fig.to_html(full_html=False)

            return graph_html, report
        else:
            return None, "Data validation failed."
    else:
        return None, "Failed to fetch data from OpenWeatherMap API."


@app.route("/")
def home():
    """
    Home route to display the visualization and report.
    """
    # Fetch and process data
    graph_html, report = fetch_and_process_data()

    if graph_html:
        # Render the visualization and report in the browser
        return render_template_string(
            """
            <h1>Climate Data Visualization</h1>
            <div>{{ graph_html|safe }}</div>
            <h2>Report</h2>
            <pre>{{ report }}</pre>
            """,
            graph_html=graph_html,
            report=report
        )
    else:
        return f"<h1>Error</h1><p>{report}</p>"


if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)

