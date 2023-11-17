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
        
        global map_widget
        
        global listallpoly
        
        
        def plotpoly(coordinates):
            
            rad = 0.5
            
            global map_widget
            
            lp = points_in_circle(coordinates, rad)
            
            #poly = map_widget.set_polygon(lp, fill_color='red')
            
            shppoly = points_to_polygon(lp)
            
            intersection = shppolymain.intersection(shppoly)
            
            intersecpolypoints = list(intersection.exterior.coords)
            
            if intersecpolypoints:

                poly = map_widget.set_polygon(intersecpolypoints, fill_color = 'red')
                
        
        global map_widget
        
        ad = 'indiranagar, bangalore, india'
        radius_km = 3
        
        coordinates = tuple(get_coordinates_mapquest_custom(ad, api_key))
        
        maincircle=points_in_circle(coordinates, radius_km)
        
        #polymain = map_widget.set_polygon(maincircle, fill_color='green')
        
        lp = points_in_circle(coordinates, radius_km)
        
        map_widget.set_position(coordinates[0], coordinates[1], marker=True, text=ad)
        
        map_widget.set_zoom(10)
            
        
        shppolymain = points_to_polygon(lp)
        
        selcafe = True
        selgyms = False
        selhos = False
        selpark = True
        selres = False
        
        if selcafe == True:
        
            cafepath = r"D:\Codessey2023\drive-download-20231116T055713Z-001\coordinates_cafes(1).csv"

            with open(cafepath, 'r') as fcafe:
                
                cafereader = csv.reader(fcafe)        
                
                for i in cafereader:
                    
                    if i:
                    
                        colat = float(i[0])
                        colong = float(i[1])
                        coor = (colat, colong)
                        
                        plotpoly(coor)
            
        
        if selgyms == True:
            
            gympath = r"D:\Codessey2023\drive-download-20231116T055713Z-001\coordinates_gyms(1).csv"
            
            with open(gympath, 'r') as fgym:
                
                readergym = csv.reader(fgym)
                
                for i in readergym:
                    
                    if i:
                    
                        colat = float(i[0])
                        colong = float(i[1])
                        coor = (colat, colong)
                        
                        plotpoly(coor)
                        
        if selhos == True:
            
            hospath = r"D:\Codessey2023\drive-download-20231116T055713Z-001\coordinates_hospital(1).csv"
            
            with open(hospath, 'r') as fhos:
                
                readerhos = csv.reader(fhos)
                
                for i in readerhos:
                    
                    if i:
                    
                        colat = float(i[0])
                        colong = float(i[1])
                        coor = (colat, colong)
                        
                        plotpoly(coor)
                        
        
        if selpark == True:            
        
            parkpath = r"D:\Codessey2023\drive-download-20231116T055713Z-001\coordinates_parks(1).csv"
            
            with open(parkpath, 'r') as fpark:
                
                readerpark = csv.reader(fpark)
                
                for i in readerpark:
                    
                    if i:
                    
                        colat = float(i[0])
                        colong = float(i[1])
                        coor = (colat, colong)
                        
                        plotpoly(coor)
                        
        if selres == True:
                    
            respath = r"D:\Codessey2023\drive-download-20231116T055713Z-001\coordinates_restaurants(1).csv"
            
            with open(respath, 'r') as fres:
                
                readerres = csv.reader(fres)
                
                for i in readerres:
                    
                    if i:
                    
                        colat = float(i[0])
                        colong = float(i[1])
                        coor = (colat, colong)
                        
                        plotpoly(coor)
        
    root = ctk.CTk()
    root.geometry('1200x700')
    root.title('Map view')
    
    
    button = ctk.CTkButton(root, text="Enter", command=ifclicked) 
    button.place(relx = 0.2, rely = 0.9)
    
    global map_widget
    
    map_widget = tkintermapview.TkinterMapView(root, width = 1000, height = 500, corner_radius=10)
    map_widget.place(relx=0.5, rely=0.5,anchor=tk.CENTER)
    map_widget.set_zoom(0)  


    root.mainloop()

makescreen()
