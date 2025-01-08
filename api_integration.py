import cdsapi

def fetch_cds_data(api_url):
    # Initialize the CDS API client
    c = cdsapi.Client()

    # Define the request parameters
    request = {
        "product_type": "reanalysis",
        "format": "netcdf",
        "variable": "2m_temperature",  # Example variable
        "year": "2020",
        "month": "01",
        "day": "01",
        "time": "12:00",
    }

    try:
        # Send the request and download the data
        result = c.retrieve(api_url, request)

        # Save the data to a file
        output_file = "era5_temperature_20200101.nc"
        result.download(output_file)
        print(f"Data downloaded successfully to {output_file}")
        return output_file  # Return the path to the downloaded file
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None
