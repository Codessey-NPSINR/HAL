import tkinter as tk
import customtkinter as ctk
import tkintermapview
import math
import requests
import shapely.geometry
from shapely.geometry import Point, Polygon
import csv

api_key = '3NrvEGQ7qy9w9KibqNcGLZHSLUEjnvCO'


def makescreen():
    
    
    def points_in_circle(center, radius, num_points=100):
        lat, lon = center
        points = []
        for i in range(num_points):
            angle = (2 * math.pi * i) / num_points
            dx = radius * math.cos(angle)
            dy = radius * math.sin(angle)

            new_lat = lat + (180 / math.pi) * (dy / 6371)
            new_lon = lon + (180 / math.pi) * (dx / (6371 * math.cos(math.radians(lat))))

            points.append((new_lat, new_lon))
        return points
    
    def get_coordinates_mapquest_custom(address, api_key):
        
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
        
        
        
    def ifclicked():
        
        
        ad = 'indiranagar, bangalore, india' # get from entry
        
        radius_km = 5 # get from entry
        
        coordinates = tuple(get_coordinates_mapquest_custom(ad, api_key))
        
        maincircle=points_in_circle(coordinates, radius_km)
        
        polymain = map_widget.set_polygon(maincircle, fill_color='green')
        
        lp = points_in_circle(coordinates, radius_km)
        lpshapely = shapely.geometry.Polygon(lp)
        
        map_widget.set_position(coordinates[0], coordinates[1], marker=True, text=ad)
        
        map_widget.set_zoom(10)
            
        
        
        
        
        housingpath = r"D:\Codessey2023\drive-download-20231116T055713Z-001\housing_coordinates(1).csv"

        with open(housingpath, 'r') as hpath:
            
            housingreader = csv.reader(hpath)        
            
            for i in housingreader:
                
                if i:
                
                    colat = float(i[0])
                    colong = float(i[1])
                    coor = (colat, colong)
                    ptshapely = shapely.geometry.Point(colat, colong)
                    
                    if ptshapely.within(lpshapely) == True:
                        m = map_widget.set_marker(colat, colong, marker_color_outside='green', marker_color_circle='blue')
            
        
        
    root = ctk.CTk()
    root.geometry('1200x700')
    root.title('Map view')
    
    entry1 = ctk.CTkEntry(root, placeholder_text="Enter the address")
    entry1.place(relx = 0.1, rely=0.2)
    
    entry2 = ctk.CTkEntry(root, placeholder_text="Enter the radius in km")
    entry2.place(relx = 0.1, rely=0.3)
    
    button = ctk.CTkButton(root, text="Enter", command=ifclicked) 
    button.place(relx = 0.1, rely = 0.5)
    
    global map_widget
    
    map_widget = tkintermapview.TkinterMapView(root, width = 1000, height = 500, corner_radius=10)
    map_widget.place(relx=0.5, rely=0.5,anchor=tk.CENTER)
    map_widget.set_zoom(0)  


    root.mainloop()

makescreen()
