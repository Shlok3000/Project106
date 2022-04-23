import numpy as np
import csv
import plotly.express as px

with open("Data.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x = "Coffee in ml", y ="sleep in hours")
    fig.show()

def getDataSource(data_path):
    coffee_ML = []
    sleep_Time = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffee_ML.append(float(row["Coffee in ml"]))
            sleep_Time.append(float(row["sleep in hours"]))
    return {"x": coffee_ML, "y": sleep_Time}

def findCorrelation(data_source):
    corellation = np.corrcoef(data_source["x"], data_source["y"])
    print("Correlation of amount of Coffee drank and sleeping time", corellation[0,1])

def setup():
    data_path = "Data.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)

setup()