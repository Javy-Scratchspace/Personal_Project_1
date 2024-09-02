# Executable_File.py

import tkinter as tk
from Resources.Graph_Plotting import graph_plotting
from Resources.Graph_Plotting import reading_files

#TODO: Make this into an executable where I can click populations and see the scatter plot
#TODO: Make buttons and entries for excel columns

root = tk.Tk()
root.title("Graph Plotting Calculator")

window_width = 600
window_height = 400

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

def init():
    tk.Text(root, height = 8).pack

def button_1():
    reading_files()

def button_2():
    graph_plotting(r'Population_From_2019_2023.xlsx', 'Population', 'Year', 'Africa')

root = root.mainloop()
