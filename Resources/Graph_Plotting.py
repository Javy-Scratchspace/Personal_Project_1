import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk
import numpy as np
        
def graph_plotting(df,x,y):

    # Creating the scatter plot
    plt.scatter(df[x], df[y])

    # Adding labels and title
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(f'Populations In {y} During Covid Times')

    # Displaying the plot
    plt.show()

def tkinter_plotting(root,df,x,y):

    a, b = np.polyfit(x ,y, 1)

    plt.scatter(df[x], df[y])
    plt.plot(x, a*x + b, color = "red")
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(f'{x} vs. {y} graph')
    plt.savefig(f'{x}_vs_{y}.png')

    img = Image.open(f'{x}_vs_{y}.png')
    photo = ImageTk.PhotoImage(img)

    # Display the image on the canvas
    canvas = tk.Canvas(root, width=300, height=200)
    canvas.pack
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)  #HACK: For some reason, without the canvas addition it won't even save an image

    



