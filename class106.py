import pandas as pd
import plotly.express as px
import numpy as np 
import csv 

def getDataSource(data_path):
    ice_cream_sales = []
    cold_drink_sales = []
    with open (data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            ice_cream_sales.append(float(row["Temperature"]))
            cold_drink_sales.append(float(row["Ice-cream Sales"]))

    return{"x": ice_cream_sales, "y": cold_drink_sales}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between tempertature vs ice cream sales: ", correlation[0,1])

def setup():
    data_path = "iceCreamsale.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)

setup()

        