#  ---- AlternativeFuelMapper ----
# A Python program that uses the NREL API to
# find the nearest alternative fuel station
# to a given latitude and longitude.

import requests
import json


def get_nearest_station(location):
    api_key = 'API-TOKEN'  # Replace this with your NREL API key
    base_url = 'https://developer.nrel.gov/api/alt-fuel-stations/v1/nearest.json'
    params = {
        'api_key': api_key,
        'location': location,
        'radius': 15,   # Limits search to thi radius, in miles
        'limit': 1
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        fuel_stations = data.get('fuel_stations', [])

        if fuel_stations:
            return fuel_stations[0]
        else:
            print('No fuel stations found near the given location.')
            return None
    else:
        print('An error occurred:', response.text)
        return None


def main():
    location = input('Please enter the location (street, city, state): ')
    nearest_station = get_nearest_station(location)

    if nearest_station:
        print('Nearest Station Information:')
        print('Name:', nearest_station['station_name'])
        print('Address:', nearest_station['street_address'])
        print('Fuel Type:', nearest_station['fuel_type_code'])
        print('Distance:', nearest_station['distance'])
    else:
        print('No station found.')


if __name__ == '__main__':
    main()
