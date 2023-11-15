import tkinter as tk
import customtkinter as ctk
import tkintermapview
import math
import requests
import geopandas as gpd
import fiona
#import numpy as np
#from shapely.geometry import Polygon

api_key = '3NrvEGQ7qy9w9KibqNcGLZHSLUEjnvCO'
kml_file_path = r"D:\Codessey2023\bangalore-slum.kml"

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
        
        global polygon_1
        polygon_1 = ''
        
        if polygon_1:
            polygon_1.delete()
        
        ad = entry1.get()
        radius_km = int(entry2.get())

        coordinates = get_coordinates_mapquest_custom(ad, api_key)

        
        colat = coordinates[0]
        colong = coordinates[1]
        
        lp = points_in_circle((colat, colong), radius_km)
        
        marker1 = map_widget.set_position(colat, colong, marker=True)
        
        map_widget.set_zoom(10)
        

        if coordinates: # checking for nulls
            print(f"Coordinates for {ad}: {coordinates}")
            

        polygon_1 = map_widget.set_polygon(lp,
                                            fill_color='red',
                                           # outline_color="red",
                                           # border_width=12,
                                           command=print('polygon clicked'),
                                           name="circ")
        global df
        
        
        
    def plotkml():
        
        fiona.drvsupport.supported_drivers['KML'] = 'rw' # import kml driver
        geo_df = gpd.read_file(kml_file_path,driver='KML')
        

        
        geo_df['centroid'] = geo_df['geometry'].centroid
        
        for ind in geo_df.index:
            
            if geo_df['centroid'][ind]:
                lat = float(geo_df['centroid'][ind].y)
                long = float(geo_df['centroid'][ind].x)
                m = map_widget.set_marker(lat, long)
        
        '''for ind in geo_df.index:
            
            if geo_df['geometry'][ind].geom_type == 'Polygon':
                polygons.append(geo_df['geometry'][ind])
                
            elif geo_df['geometry'][ind].geom_type == 'MultiPolygon':
                
                multdf = gpd.GeoDataFrame(geo_df[ind], geometry = 'geometry', crs=geo_df.crs)
                
                for index in multdf.index:
                    
                    try:
                        polygons.append(multdf['geometry'][index])
                    except KeyError(3):
                        pass
           '''     
        
        
        '''
        for index in range(len(polygons)):
            map_widget.set_polygon([(46.0732306, 6.0095215),
                                    ...
                                    (46.3772542, 6.4160156)],
                                   # fill_color=None,
                                   # outline_color="red",
                                   # border_width=12,
                                   command=polygon_click,
                                   name="switzerland_polygon")
          '''
          
        
            
    
    root = ctk.CTk()
    root.geometry('1000x700')
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
    
    plotkml()    

    root.mainloop()

makescreen()