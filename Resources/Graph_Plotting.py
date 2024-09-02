import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import Workbook

def graph_plotting(excel_sheet,sheet_name,x,y):

    # Reading the Excel file
    try:
        df = pd.read_excel(excel_sheet, sheet_name=sheet_name)
    except:
        wb = Workbook()
        wb.save('Data_Sample.xlsx')

    # Creating the scatter plot
    plt.scatter(df[x], df[y])

    # Adding labels and title
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(f'Populations In {y} During Covid Times')

    # Displaying the plot
    plt.show()

graph_plotting(r'Population_From_2019_2023.xlsx', 'Population', 'Year', 'Africa')