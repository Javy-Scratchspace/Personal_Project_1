import pandas as pd
import matplotlib.pyplot as plt

def graph_plotting(x):
    
    # Set the sheet name and y label
    if x == "Population (Africa)":
        area = "Africa"
    elif x == "Population (Central America)":
        area = "Central America"
    elif x == "Population (Carribean-Latin)":
        area = "Latin America"
    elif x == "Population (South America)":
        area = "South America"
    elif x == "Population (Asia)":
        area = "Asia"
    elif x == "Population (Oceania)":
        area = "Oceania"
    elif x == "Population (Polynesia)":
        area = "Polynesia"
    elif x == "Population (Europe)":
        area = "Europe"

    # Reading the Excel file
    df = pd.read_excel(r'Population_From_2019_2023.xlsx', sheet_name=x)

    # Creating the scatter plot
    plt.scatter(df["Year"], df[area])

    # Adding labels and title
    plt.xlabel("Year")
    plt.ylabel(area)
    plt.title(f'Populations In {area} During Covid Times')

    # Displaying the plot
    plt.show()


graph_plotting("Population (Asia)")