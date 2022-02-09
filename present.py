#CO-RELATION

import csv
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    days_present=[]
    marks_in_percentage=[]
    with open(data_path) as csv_file:
        csv_Reader=csv.DictReader(csv_file)
        for row in csv_Reader:
            days_present.append(float(row["Days Present"]))
            marks_in_percentage.append(float(row["Marks In Percentage"]))
    return{"x": days_present, "y":marks_in_percentage}
def findCorelation(data_source):
    corelation=np.corrcoef(data_source["x"], data_source["y"] )
    print("Corelation between Marks obtained and the attendance of a student is ", corelation[0,1])
def setup():
    data_path="present.csv"
    data_source=getDataSource(data_path)
    findCorelation(data_source)
setup()