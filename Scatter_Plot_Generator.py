# Scatter_Plot_Generator.py
# pyinstaller --onefile Scatter_Plot_Generator.py
# @author: Javier Cuevas

import tkinter as tk
from tkinter import ttk
import pandas as pd
from openpyxl import Workbook
from Resources.Graph_Plotting import graph_plotting, tkinter_plotting
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#TODO: Make this into an executable where I can click populations and see the scatter plot
#TODO: Make buttons and entries for excel columns

root = tk.Tk()
root.title("Graph Plotting Calculator")

window_width = 1000
window_height = 500

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

def error(e):
    text.delete("1.0", tk.END)
    text.insert(tk.END, f"ERROR, Python Output: {e}")

def display_df(df):
    text.delete("1.0", tk.END)  # Delete previous text
    text.insert(tk.END, df.to_string())

def reading_files(excel_sheet, sheet_name):
    # Reading the Excel file
    try:
        df = pd.read_excel(excel_sheet, sheet_name = sheet_name)

    except Exception as e:
        error(e)

    return df

def button_1():
    df = reading_files(excel_file_entry.get(),excel_sheet_entry.get())
    display_df(df)

def button_2():
    df = reading_files(excel_file_entry.get(),excel_sheet_entry.get())
    try:
        tkinter_plotting(root,df,x_column_entry.get(),y_column_entry.get())
    except Exception as e:
        error(e)

excel_file_var = tk.StringVar()
excel_file_entry = tk.Entry(root, textvariable = excel_file_var)
excel_file_entry.pack(padx=10,pady=10)
excel_file_entry.insert(0, r'Resources/excel_file.xlsx')

excel_sheet_var = tk.StringVar()
excel_sheet_entry = tk.Entry(root, textvariable = excel_sheet_var)
excel_sheet_entry.pack(padx=10,pady=10)
excel_sheet_entry.insert(0, 'Sheet')

x_column_var = tk.StringVar()
x_column_entry = tk.Entry(root, textvariable = x_column_var)
x_column_entry.pack(padx=10,pady=10)
x_column_entry.insert(0, 'x_column')

y_column_var = tk.StringVar()
y_column_entry = tk.Entry(root, textvariable = y_column_var)
y_column_entry.pack(padx=10,pady=10)
y_column_entry.insert(0, 'y_column')

button1 = ttk.Button(root, text="Read Excel File", command=button_1)
button1.pack(padx=10,pady=10)

button2 = ttk.Button(root, text="Plot Graphs", command=button_2)
button2.pack(padx=10,pady=10)

text = tk.Text(root, height = 8)
text.pack(expand=True, fill='both')

root.mainloop()
