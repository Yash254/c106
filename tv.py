import plotly.express as px
import csv
import numpy as np

def getdatasource(data_path):
    st=[]
    at=[]
    with open(data_path)as f:
        df=csv.DictReader(f)
        for row in df:
            st.append(float(row["Size of TV"]))
            at.append(float(row["Average time spent watching TV in a week"]))
    
    return {"x":st,"y":at}

def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource['y'])
    print("correlation is-",correlation[0,1])

def setup():
    data_path="tv.csv"
    datasource=getdatasource(data_path)
    findcorrelation(datasource)

setup()