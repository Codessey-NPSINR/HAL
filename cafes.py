import tkinter as tk
import customtkinter as ctk
import tkintermapview
import math
import requests
from shapely.geometry import Point, Polygon
import csv

api_key = '3NrvEGQ7qy9w9KibqNcGLZHSLUEjnvCO'


def makescreen():
    
    def points_to_polygon(point_list):
        return Polygon(point_list)
    
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
        
    def ifclicked():
        
        def plotpoly(coordinates):
            
            rad = 0.5
            
            lp = points_in_circle(coordinates, rad)
            
            poly = map_widget.set_polygon(lp, fill_color='red')
            
            
        
        ad = entry1.get()
        radius_km = float(entry2.get())
        
        coordinates = tuple(get_coordinates_mapquest_custom(ad, api_key))
        
        maincircle=points_in_circle(coordinates, radius_km)
        
        #polymain = map_widget.set_polygon(maincircle, fill_color='green')
            
        
        lp = points_in_circle(coordinates, radius_km)
        
        
        map_widget.set_position(coordinates[0], coordinates[1], marker=True)
        
        map_widget.set_zoom(10)
            
        
        shppoly1 = points_to_polygon(lp)
        
        #intersectionpolygon = shppoly1.intersection(shppoly2)
        
        '''if intersectionpolygon:
            
            intersectionpolycoor = list(intersectionpolygon.exterior.coords)
            
            
            polygon_intersection = map_widget.set_polygon(intersectionpolycoor, fill_color='black')'''
        
        
        csvpath = r"D:\Codessey2023\drive-download-20231116T055713Z-001\coordinates_cafes(1).csv"
        
        with open(csvpath, 'r') as f:
            
            reader = csv.reader(f)        
            
            for i in reader:
                
                colat = float(i[0])
                colong = float(i[1])
                coor = (colat, colong)
                
                print(coor)
                plotpoly(coor)
                
                
    
    
    
    root = ctk.CTk()
    root.geometry('1200x700')
    root.title('Map view')
    
    entry1 = ctk.CTkEntry(root, placeholder_text="Enter the address")
    entry1.place(relx = 0.1, rely=0.2)
    
    
    
    entry2 = ctk.CTkEntry(root, placeholder_text="Enter the radius in km")
    entry2.place(relx = 0.1, rely=0.3)
    
   
     
    button = ctk.CTkButton(root, text="Enter", command=ifclicked) 
    button.place(relx = 0.1, rely = 0.5)
    
    map_widget = tkintermapview.TkinterMapView(root, width = 800, height = 500, corner_radius=10)
    map_widget.place(relx=0.7, rely=0.5,anchor=tk.CENTER)
    map_widget.set_zoom(0)  


    root.mainloop()

makescreen()