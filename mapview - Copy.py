import tkinter as tk
import tkintermapview

def get_bounding_box(latitude, longitude, radius_km):
    """
    Get the bounding box for a location.

    Parameters:
    - latitude (float): Latitude of the center point.
    - longitude (float): Longitude of the center point.
    - radius_km (float): Radius in kilometers.

    Returns:
    - Tuple of (min_latitude, min_longitude, max_latitude, max_longitude).
    """
    # Earth radius in kilometers
    earth_radius = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat_rad = latitude * (3.141592653589793 / 180.0)
    lon_rad = longitude * (3.141592653589793 / 180.0)

    # Calculate the angular distance in radians
    delta_lat_rad = radius_km / earth_radius
    delta_lon_rad = radius_km / (earth_radius * (abs(latitude) / 90.0))

    # Calculate bounding box coordinates
    min_latitude = latitude - (delta_lat_rad * (180.0 / 3.141592653589793))
    min_longitude = longitude - (delta_lon_rad * (180.0 / 3.141592653589793))
    max_latitude = latitude + (delta_lat_rad * (180.0 / 3.141592653589793))
    max_longitude = longitude + (delta_lon_rad * (180.0 / 3.141592653589793))

    return min_latitude, min_longitude, max_latitude, max_longitude

import requests

def get_coordinates_mapquest_custom(address, api_key):
    """
    Get the coordinates (latitude and longitude) of an address using MapQuest Geocoding API without using geopy.

    Parameters:
    - address (str): The address for which you want to obtain coordinates.
    - api_key (str): Your MapQuest API key.

    Returns:
    - Tuple of (latitude, longitude) or None if the address is not found or an error occurs.
    """
    base_url = "https://www.mapquestapi.com/geocoding/v1/address"
    
    params = {
        "key": api_key,
        "location": address,
        "outFormat": "json",
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200 and data.get("results"):
            location = data["results"][0]["locations"][0]
            return location["latLng"]["lat"], location["latLng"]["lng"]
        else:
            print("Error: Unable to retrieve coordinates.")
            return None

    except Exception as e:
        print(f"Error getting coordinates: {e}")
        return None

# Example usage:
api_key = '3NrvEGQ7qy9w9KibqNcGLZHSLUEjnvCO'
#ad = input('Enter address: ')
ad = 'indiranagar, bangalore, india'
coordinates = get_coordinates_mapquest_custom(ad, api_key)

if coordinates:
    print(f"Coordinates for {ad}: {coordinates}")


# Example usage:
latitude = coordinates[0] # Example latitude (San Francisco)
longitude = coordinates[1]  # Example longitude (San Francisco)
radius_km = 5  # Example radius in kilometers

bounding_box = get_bounding_box(latitude, longitude, radius_km)
print("Bounding Box:", bounding_box)


root = tk.Tk()
root.geometry('1000x700')
root.title('Map view')


minlat = bounding_box[0]
minlong = bounding_box[1]
maxlat = bounding_box[2]
maxlong = bounding_box[3]

marker_ind = map_widget.set_marker(12.97394, 77.6439, text="Point", marker_color_circle='blue', marker_color_outside='green')

marker_1 = map_widget.set_marker(12.928973919704065, 77.3319710696493, text="A", marker_color_circle='blue', marker_color_outside='green')

marker_2 = map_widget.set_marker(12.928973919704065, 77.9558289303507, text="B", marker_color_circle='blue', marker_color_outside='green')

marker_3 = map_widget.set_marker(13.018906080295936, 77.9558289303507, text="C", marker_color_circle='blue', marker_color_outside='green')

marker_4 = map_widget.set_marker(13.018906080295936, 77.3319710696493, text="D", marker_color_circle='blue', marker_color_outside='green')

root.mainloop()