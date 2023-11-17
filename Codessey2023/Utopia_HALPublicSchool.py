import customtkinter as ctk
from PIL import Image, ImageTk
import tkinter as tk
import smtplib


import tkintermapview
import math
import requests
from shapely.geometry import Point, Polygon
import csv


import shapely.geometry



import networkx as nx
import os

def create_image(image_path):
    img=Image.open(image_path)
    photo=ImageTk.PhotoImage(img)
    return photo


def destroy():
    for widget in root.winfo_children():
        widget.destroy()


def login_page():
    destroy()

    def login():
        destroy()

        type1 = 'User'

        bg2=create_image(r"D:\Codessey2023\final\images-20231116T220518Z-001\images\login_background.png")
        bg=ctk.CTkLabel(root,text="",image=bg2)
        bg.place(x=0,y=0)

        login3=create_image(r"D:\Codessey2023\final\images-20231116T220518Z-001\images\login_btn.png")

        login_btn2=ctk.CTkButton(root,text="",image=login3,command=lambda:typeuser(type1))
        login_btn2.place(x=480,y=580)

        entry1=ctk.CTkEntry(root,placeholder_text="Username",height=54,width=650,fg_color="white",placeholder_text_color="black",text_color="black")
        entry1.place(x=420,y=250)

        entry2=ctk.CTkEntry(root,placeholder_text="Password",height=54,width=650,fg_color="white",placeholder_text_color="black",text_color="black")
        entry2.place(x=420,y=350)

        entry3=ctk.CTkEntry(root,placeholder_text="Captcha",height=54,width=388,fg_color="white",placeholder_text_color="black",text_color="black")
        entry3.place(x=680,y=450)

        captcha=create_image(r"D:\Codessey2023\final\images-20231116T220518Z-001\images\captcha.png")
        captcha1=ctk.CTkLabel(root,text="",image=captcha)
        captcha1.place(x=375,y=450)

        

        
        
    def sign_up():
        
        destroy()

        def next_signup():
            destroy()

            def sending_verification_code(entryemail):

                server = smtplib.SMTP('smtp.gmail.com', 587)

                server.starttls()

                server.login('codessyhps@gmail.com', 'bnwg ncsf sjrc dqsk')

                server.sendmail('codessyhps@gmail.com', '{}'.format(entryemail), 'verification code = codesseyhps2023')

                print('sent')

            
            def typeuser(choice):
                destroy()
                if choice=="User":
                    
                    def find_home():

                        bg2=create_image(r"D:\Codessey2023\final\images-20231116T220518Z-001\images\find_home_bg.jpg")
                        bg=ctk.CTkLabel(root,text="",image=bg2)
                        bg.place(x=0,y=0)
                        img6=create_image(r"D:\Codessey2023\final\images-20231116T220518Z-001\images\submit_find_home.png")
                        submit_find_home=ctk.CTkButton(root,text="",image=img6,width=40,command=lambda: os.startfile(r"D:\Codessey2023\final\searchhome.py"))
                        submit_find_home.place(x=1085,y=200)
                        entry3=ctk.CTkEntry(root,placeholder_text="Central Location:",height=65,width=450,fg_color="white",placeholder_text_color="black",text_color="black")
                        entry3.place(x=720,y=115)
                        entry4=ctk.CTkEntry(root,placeholder_text="Y/N:",height=40,width=54,fg_color="white",placeholder_text_color="black",text_color="black")
                        entry4.place(x=720,y=410)
                        entry5=ctk.CTkEntry(root,placeholder_text="Y/N:",height=40,width=54,fg_color="white",placeholder_text_color="black",text_color="black")
                        entry5.place(x=720,y=450)
                        entry6=ctk.CTkEntry(root,placeholder_text="Y/N:",height=40,width=54,fg_color="white",placeholder_text_color="black",text_color="black")
                        entry6.place(x=720,y=490)
                        entry7=ctk.CTkEntry(root,placeholder_text="Y/N:",height=40,width=54,fg_color="white",placeholder_text_color="black",text_color="black")
                        entry7.place(x=720,y=530)
                        entry8=ctk.CTkEntry(root,placeholder_text="Y/N:",height=40,width=54,fg_color="white",placeholder_text_color="black",text_color="black")
                        entry8.place(x=720,y=570)
                        entry9=ctk.CTkEntry(root,placeholder_text="Y/N:",height=40,width=54,fg_color="white",placeholder_text_color="black",text_color="black")
                        entry9.place(x=720,y=610)
                        entry10=ctk.CTkEntry(root,placeholder_text="Within __ kms",height=40,width=250,fg_color="white",placeholder_text_color="black",text_color="black")
                        entry10.place(x=800,y=410)
                        black_line1=create_image(r"D:\Codessey2023\final\images-20231116T220518Z-001\images\black_line.png")
                        black_line=ctk.CTkLabel(root,text="",image=black_line1)
                        black_line.place(x=200,y=640)

                        
                        
                        
                        '''api_key = '3NrvEGQ7qy9w9KibqNcGLZHSLUEjnvCO'


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
                                
                                ad = entry1.get()
                                radius_km = float(entry2.get())
                                
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

                            map_widget = tkintermapview.TkinterMapView(root, width = 1000, height = 500, corner_radius=10)
                            map_widget.place(relx=0.5, rely=0.5,anchor=tk.CENTER)
                            map_widget.set_zoom(0)
                            root.title('Map view')

                            button = ctk.CTkButton(root, text="Enter", command=ifclicked) 
                            button.place(relx = 0.5, rely = 0.85)

                            root.mainloop()

                        makescreen()'''

                    def find_services():

                        os.startfile(r"D:\Codessey2023\final\searchservices.py")

                        '''api_key = '3NrvEGQ7qy9w9KibqNcGLZHSLUEjnvCO'


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
                                
                                youimg = Image.open(r"D:\Codessey2023\drive-download-20231116T055713Z-001\Handsome marker title.png").resize((100, 50))
                                youctkimg = ImageTk.PhotoImage(youimg)
                                
                                pcard = Image.open(r"D:\Codessey2023\drive-download-20231116T055713Z-001\Profile info.jpg").resize((300,200))
                                pcardtk = ImageTk.PhotoImage(pcard)
                                
                                m = map_widget.set_marker(coordinates[0], coordinates[1],  icon=youctkimg)                    
                                
                                phonenumpath = r"D:\Codessey2023\drive-download-20231116T055713Z-001\phone_number_coordinates(1).csv"

                                with open(phonenumpath, 'r') as phones:
                                    
                                    phonereader = csv.reader(phones) 
                                    
                                    for i in phonereader:
                                        
                                        phno = i[2]
                                        em = i[3]
                                        
                                        if i:
                                        
                                            colat = float(i[0])
                                            colong = float(i[1])
                                            
                                            coor = (colat, colong)
                                            ptshapely = shapely.geometry.Point(colat, colong)
                                            
                                            if ptshapely.within(lpshapely) == True:
                                                m = map_widget.set_marker(colat, colong, image = pcardtk, marker_color_outside='green', marker_color_circle='blue',  image_zoom_visibility=(14, float('inf')) )
                                                
                                
                                
                            root = ctk.CTk()
                            root.geometry('1200x700')
                            root.title('Map view')
                            
                            
                            button = ctk.CTkButton(root, text="Enter", command=ifclicked) 
                            button.place(relx = 0.5, rely = 0.85)
                            
                            global map_widget
                            
                            map_widget = tkintermapview.TkinterMapView(root, width = 1000, height = 500, corner_radius=10)
                            map_widget.place(relx=0.5, rely=0.5,anchor=tk.CENTER)
                            map_widget.set_zoom(0)  
                            
                            


                            root.mainloop()

                        makescreen()
'''
                    def look_for_community():

                        os.startfile(r"D:\Codessey2023\final\searchcommunity.py")

                        '''api_key = '3NrvEGQ7qy9w9KibqNcGLZHSLUEjnvCO'


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
                                
                                youimg = Image.open(r"D:\Codessey2023\drive-download-20231116T055713Z-001\Handsome marker title.png").resize((100, 50))
                                youctkimg = ImageTk.PhotoImage(youimg)
                                
                                pcard = Image.open(r"D:\Codessey2023\drive-download-20231116T055713Z-001\Profile info.jpg").resize((300,200))
                                pcardtk = ImageTk.PhotoImage(pcard)
                                
                                m = map_widget.set_marker(coordinates[0], coordinates[1],  icon=youctkimg)                    
                                
                                phonenumpath = r"D:\Codessey2023\drive-download-20231116T055713Z-001\phone_number_coordinates(1).csv"

                                with open(phonenumpath, 'r') as phones:
                                    
                                    phonereader = csv.reader(phones) 
                                    
                                    for i in phonereader:
                                        
                                        phno = i[2]
                                        em = i[3]
                                        
                                        if i:
                                        
                                            colat = float(i[0])
                                            colong = float(i[1])
                                            
                                            coor = (colat, colong)
                                            ptshapely = shapely.geometry.Point(colat, colong)
                                            
                                            if ptshapely.within(lpshapely) == True:
                                                m = map_widget.set_marker(colat, colong, image = pcardtk, marker_color_outside='green', marker_color_circle='blue',  image_zoom_visibility=(14, float('inf')) )
                                                
                                
                                
                            root = ctk.CTk()
                            root.geometry('1200x700')
                            root.title('Map view')
                            

                            
                            button = ctk.CTkButton(root, text="Enter", command=ifclicked) 
                            button.place(relx = 0.5, rely = 0.85)
                            
                            global map_widget
                            
                            map_widget = tkintermapview.TkinterMapView(root, width = 1000, height = 500, corner_radius=10)
                            map_widget.place(relx=0.5, rely=0.5,anchor=tk.CENTER)
                            map_widget.set_zoom(0)  
                            
                            


                            root.mainloop()

                        makescreen()
'''
                    def contribute_to_ngo():

                        def ngomap():

                            os.startfile(r"D:\Codessey2023\final\searchngo.py")

                            '''api_key = '3NrvEGQ7qy9w9KibqNcGLZHSLUEjnvCO'


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
                                        
                                    
                                    
                                    
                                    
                                    ngopath = r"D:\Codessey2023\drive-download-20231116T055713Z-001\ngos_coordinates(1).csv"

                                    with open(ngopath, 'r') as ngos:
                                        
                                        ngoreader = csv.reader(ngos)        
                                        
                                        for i in ngoreader:
                                            
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
                                
                                button = ctk.CTkButton(root, text="Search", command=ifclicked) 
                                button.place(relx = 0.1, rely = 0.5)
                                
                                global map_widget
                                
                                map_widget = tkintermapview.TkinterMapView(root, width = 1000, height = 500, corner_radius=10)
                                map_widget.place(relx=0.5, rely=0.5,anchor=tk.CENTER)
                                map_widget.set_zoom(0)  


                                root.mainloop()

                            makescreen()
'''

                    bg2=create_image(r"D:\Codessey2023\final\images-20231116T220518Z-001\images\user_page.jpg")
                    bg=ctk.CTkLabel(root,text="",image=bg2)
                    bg.place(x=0,y=0)
                    img5=create_image(r"D:\Codessey2023\final\images-20231116T220518Z-001\images\find_home_btn.png")
                    find_home_btn=ctk.CTkButton(root,text="",image=img5,command=lambda:find_home())
                    find_home_btn.place(x=15,y=550)
                    img6=create_image(r"D:\Codessey2023\final\images-20231116T220518Z-001\images\services_btn.png")
                    services_btn=ctk.CTkButton(root,text="",image=img6,command=lambda:find_services())
                    services_btn.place(x=275,y=545)
                    img9=create_image(r"D:\Codessey2023\final\images-20231116T220518Z-001\images\community_btn.png")
                    community_btn=ctk.CTkButton(root,text="",image=img9,command=lambda:look_for_community())
                    community_btn.place(x=590,y=550)
                    img10=create_image(r"D:\Codessey2023\final\images-20231116T220518Z-001\images\contribute_btn.png")
                    contribute_btn=ctk.CTkButton(root,text="",image=img10,command=lambda:contribute_to_ngo())
                    contribute_btn.place(x=910,y=538)

                        
                    
                elif choice=="NGO":

                    def underprivileged():

                        os.startfile(r"D:\Codessey2023\final\helpunderprivileged.py")
                        
                        '''api_key = '3NrvEGQ7qy9w9KibqNcGLZHSLUEjnvCO'


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
                                    
                                
                                
                                
                                
                                ngopath = r"D:\Codessey2023\drive-download-20231116T055713Z-001\ngos_coordinates(1).csv"

                                with open(ngopath, 'r') as ngos:
                                    
                                    ngoreader = csv.reader(ngos)        
                                    
                                    for i in ngoreader:
                                        
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
                            
                            
                            button = ctk.CTkButton(root, text="Search", command=ifclicked) 
                            button.place(relx = 0.5, rely = 0.85)
                            
                            global map_widget
                            
                            map_widget = tkintermapview.TkinterMapView(root, width = 1000, height = 500, corner_radius=10)
                            map_widget.place(relx=0.5, rely=0.5,anchor=tk.CENTER)
                            map_widget.set_zoom(0)  


                            root.mainloop()

                        makescreen()
                    '''

                        
                    def disabled():

                        os.startfile(r"D:\Codessey2023\final\helpdisabled.py")

                        '''api_key = '3NrvEGQ7qy9w9KibqNcGLZHSLUEjnvCO'


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
                                    
                                
                                
                                
                                
                                ngopath = r"D:\Codessey2023\drive-download-20231116T055713Z-001\ngos_coordinates(1).csv"

                                with open(ngopath, 'r') as ngos:
                                    
                                    ngoreader = csv.reader(ngos)        
                                    
                                    for i in ngoreader:
                                        
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
                            
                            
                            button = ctk.CTkButton(root, text="Enter", command=ifclicked) 
                            button.place(relx = 0.5, rely = 0.85)
                            
                            global map_widget
                            
                            map_widget = tkintermapview.TkinterMapView(root, width = 1000, height = 500, corner_radius=10)
                            map_widget.place(relx=0.5, rely=0.5,anchor=tk.CENTER)
                            map_widget.set_zoom(0)  


                            root.mainloop()

                        makescreen()
'''
                    
                    bg2=create_image(r"D:\Codessey2023\final\images-20231116T220518Z-001\images\ngo_bg.png")
                    bg=ctk.CTkLabel(root,text="",image=bg2)
                    bg.place(x=0,y=0)
                    img13=create_image(r"D:\Codessey2023\final\images-20231116T220518Z-001\images\help_underpriviledged_btn.png")
                    underpriviledged_btn=ctk.CTkButton(root,text="",image=img13,command=lambda:underprivileged())
                    underpriviledged_btn.place(x=45,y=480)
                    img14=create_image(r"D:\Codessey2023\final\images-20231116T220518Z-001\images\help_disabled_btn.png")
                    disabled_btn=ctk.CTkButton(root,text="",image=img14,command=lambda:disabled())
                    disabled_btn.place(x=700,y=460)
                    
                elif choice=="Management":
                    #waste page has to be made again
                    #get the coordinates fixed,after that is donee...

                    os.startfile(r"D:\Codessey2023\final\routeforwastemanagement.py")
                    
                    '''def waste():

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
                                
                                global ptlist
                                ptlist = []

                                with open(housingpath, 'r') as hpath:
                                    
                                    housingreader = csv.reader(hpath)        
                                    
                                    for i in housingreader:
                                        
                                        if i:
                                        
                                            colat = float(i[0])
                                            colong = float(i[1])
                                            coor = [colat, colong]
                                            ptshapely = shapely.geometry.Point(colat, colong)
                                            
                                            if ptshapely.within(lpshapely) == True:
                                                m = map_widget.set_marker(colat, colong, marker_color_outside='green', marker_color_circle='blue')
                                                ptlist.append(coor)
                                                
                                def plotroute(ptlist):
                                    
                                    G = nx.complete_graph(len(ptlist))
                                    tsp_path = nx.approximation.traveling_salesman_problem(G)
                                    
                                    
                                    polypoints = []
                                    
                                    for i in tsp_path:
                                        
                                        polypoints.append(ptlist[i])
                                        
                                    poly = map_widget.set_polygon(polypoints, border_width=5)
                                        
                                        
                                plotroute(ptlist)
                                
                                
                            root = ctk.CTk()
                            root.geometry('1200x700')
                            root.title('Map view')
                            
                            entry1 = ctk.CTkEntry(root, placeholder_text="Enter the address")
                            entry1.place(relx = 0.1, rely=0.2)
                            
                            entry2 = ctk.CTkEntry(root, placeholder_text="Enter the radius in km")
                            entry2.place(relx = 0.1, rely=0.3)
                            
                            button = ctk.CTkButton(root, text="Enter", command=ifclicked) 
                            button.place(relx = 0.5, rely = 0.85)
                            
                            global map_widget
                            
                            map_widget = tkintermapview.TkinterMapView(root, width = 1000, height = 500, corner_radius=10)
                            map_widget.place(relx=0.5, rely=0.5,anchor=tk.CENTER)
                            map_widget.set_zoom(0)  
    


                            root.mainloop()

                        makescreen()

'''

                    bg2=create_image(r"D:\Codessey2023\final\images-20231116T220518Z-001\images\management_bg.jpeg")
                    bg=ctk.CTkLabel(root,text="",image=bg2)
                    bg.place(x=0,y=0)
                    img11=create_image(r"D:\Codessey2023\final\images-20231116T220518Z-001\images\waste_btn.png")
                    waste_btn=ctk.CTkButton(root,text="",image=img11,command=lambda:waste())
                    waste_btn.place(x=400,y=480)
                elif choice=="Services":
                    pass
                    
                
            bg2=create_image(r"D:\Codessey2023\final\images-20231116T220518Z-001\images\signup_2bg.png")
            bg=ctk.CTkLabel(root,text="",image=bg2)
            bg.place(x=0,y=0)
            signup2=create_image(r"D:\Codessey2023\final\images-20231116T220518Z-001\images\signup_btn_img2.png")
            signup_btn2=ctk.CTkButton(root,text="",image=signup2,command=lambda:print("it,finally signs up"))
            signup_btn2.place(x=445,y=550)
            entry=ctk.CTkEntry(root,placeholder_text="Phone No",height=54,width=585,fg_color="white",placeholder_text_color="black",text_color="black")
            entry.place(x=530,y=225)
            verification=ctk.CTkEntry(root,placeholder_text="Verification Code:",height=54,width=388,fg_color="white",placeholder_text_color="black",text_color="black")
            verification.place(x=680,y=320)

            def getcode():
                
                vercod = verification.get()

                if vercod == 'codesseyhps2023':

                    optionmenu=ctk.CTkOptionMenu(root,dropdown_hover_color="black",dropdown_fg_color="black",button_hover_color="black",values=["User","NGO","Management","Services"],height=54,width=585,command=typeuser,variable=option_var)
                    optionmenu.place(x=530,y=400)
            
                
            send_verify=ctk.CTkButton(root,text="Send Verification Code",command=lambda:sending_verification_code('pritamghiremath9@gmail.com'))
            send_verify.place(x=500,y=320)

            send_verify=ctk.CTkButton(root,text="Check Verification Code",command=lambda:getcode())
            send_verify.place(x=500,y=350)
            
            option_var=ctk.StringVar(value="User")
            
            
            
        def submit():
            a = entry3.get()
            if a == 'WD54J':
                next1=create_image(r"D:\Codessey2023\final\images-20231116T220518Z-001\images\next_btn_img.png")
                next_btn=ctk.CTkButton(root,text="",image=next1,command=lambda:next_signup())
                next_btn.place(x=450,y=580)
                

        
        bg2=create_image(r"D:\Codessey2023\final\images-20231116T220518Z-001\images\signup_1bg.png")
        bg=ctk.CTkLabel(root,text="",image=bg2)
        bg.place(x=0,y=0)
        global email
        email = ''
        entry=ctk.CTkEntry(root,placeholder_text="Email",height=54,width=760,fg_color="white",placeholder_text_color="black",text_color="black")
        entry.place(x=310,y=190)
        email = entry.get()
        entry1=ctk.CTkEntry(root,placeholder_text="Username",height=54,width=650,fg_color="white",placeholder_text_color="black",text_color="black")
        entry1.place(x=420,y=270)
        entry2=ctk.CTkEntry(root,placeholder_text="Password",height=54,width=650,fg_color="white",placeholder_text_color="black",text_color="black")
        entry2.place(x=420,y=360)
        entry3=ctk.CTkEntry(root,placeholder_text="Captcha",height=54,width=200,fg_color="white",placeholder_text_color="black",text_color="black")
        entry3.place(x=680,y=450)
        captcha=create_image(r"D:\Codessey2023\final\images-20231116T220518Z-001\images\captcha.png")
        captcha1=ctk.CTkLabel(root,text="",image=captcha)
        captcha1.place(x=370,y=450)
        captcha_submit=ctk.CTkButton(root,text="Submit",width=140,height=54,command=lambda:submit())
        captcha_submit.place(x=930,y=450)

        
    bg2=create_image(r"D:\Codessey2023\final\images-20231116T220518Z-001\images\login_page_bg.png")
    bg=ctk.CTkLabel(root,text="",image=bg2)
    bg.place(x=0,y=0)
    login_btn=create_image(r"D:\Codessey2023\final\images-20231116T220518Z-001\images\Login.jpeg")
    button1=ctk.CTkButton(root,text="",image=login_btn,command=lambda:login())
    button1.place(x=65,y=105)
    signup=create_image(r"D:\Codessey2023\final\images-20231116T220518Z-001\images\Sign_up.jpeg")
    button2=ctk.CTkButton(root,text="",image=signup,command=lambda:sign_up())
    button2.place(x=685,y=428)
    
        
ctk.set_appearance_mode("Dark")

root=ctk.CTk()
root.geometry("1200x700")
image_path=r"D:\Codessey2023\final\images-20231116T220518Z-001\images\homepage.png"
img = Image.open(image_path)
photo = ImageTk.PhotoImage(img)
label =ctk.CTkLabel(root,text="",image=photo)
label.place(x=0,y=0)
logo_img=r"D:\Codessey2023\final\images-20231116T220518Z-001\images\home_button(1).jpeg"
img1=Image.open(logo_img)
bg=ImageTk.PhotoImage(img1)
button1=ctk.CTkButton(root,text="",image=bg,command=lambda:login_page())
button1.place(x=420,y=100)
utopia=r"D:\Codessey2023\final\images-20231116T220518Z-001\images\utopia.png"
img2=Image.open(utopia)
home_text=ImageTk.PhotoImage(img2)
home_text1=ctk.CTkButton(root,text="",border_color="gray100",image=home_text,command=lambda:login_page())
home_text1.place(x=320,y=460)


root.mainloop()
