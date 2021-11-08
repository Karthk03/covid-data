from re import X
import pandas as py
import plotly.express as px

df = py.read_csv('covidData.csv')
fid = px.scatter(df,y = 'cases', x = 'date', color = 'country', title = 'covid casses')
fid.show()
