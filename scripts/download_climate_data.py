import requests
import os

def download_climate_data():
    # Example URLs for climate data from NASA and NOAA
    nasa_url = 'https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv'
    noaa_url = 'https://www.ncei.noaa.gov/data/global-precipitation/v1.0/access/'

    response_nasa = requests.get(nasa_url)
    with open('data/nasa_climate_data.csv', 'wb') as file:
        file.write(response_nasa.content)

    # For NOAA data, we might need to download multiple files
    os.makedirs('data/noaa', exist_ok=True)
    response_noaa = requests.get(noaa_url)
    # Parse response_noaa to get individual file links and download them
    # ...

os.makedirs('data', exist_ok=True)
download_climate_data()
