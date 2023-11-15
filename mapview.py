import tkinter as tk
import tkintermapview

root = tk.Tk()
root.geometry('1000x700')
root.title('Map view')

map_widget = tkintermapview.TkinterMapView(root, width = 1400, height = 700, corner_radius=10)
map_widget.place(relx=0.5, rely=0.5,anchor=tk.CENTER)
map_widget.set_position(12.97394, 77.6439)
map_widget.set_zoom(10)

marker_ind = map_widget.set_marker(12.97394, 77.6439, text="Point", marker_color_circle='blue', marker_color_outside='green')

marker_1 = map_widget.set_marker(12.928973919704065, 77.3319710696493, text="A", marker_color_circle='blue', marker_color_outside='green')

marker_2 = map_widget.set_marker(12.928973919704065, 77.9558289303507, text="B", marker_color_circle='blue', marker_color_outside='green')

marker_3 = map_widget.set_marker(13.018906080295936, 77.9558289303507, text="C", marker_color_circle='blue', marker_color_outside='green')

marker_4 = map_widget.set_marker(13.018906080295936, 77.3319710696493, text="D", marker_color_circle='blue', marker_color_outside='green')

root.mainloop()
