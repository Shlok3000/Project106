import numpy as np
import csv
import plotly.express as px

with open("data2.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x = "Marks In Percentage", y ="Days Present")
    fig.show()

def getDataSource(data_path):
    Percent_marks = []
    Days_present = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Percent_marks.append(float(row["Marks In Percentage"]))
            Days_present.append(float(row["Days Present"]))
    return {"x": Percent_marks, "y": Days_present}

def findCorrelation(data_source):
    corellation = np.corrcoef(data_source["x"], data_source["y"])
    print("Correlation of Percent in marks and days present", corellation[0,1])

def setup():
    data_path = "data2.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)

setup()