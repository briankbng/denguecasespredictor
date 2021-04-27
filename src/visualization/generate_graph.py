# -*- coding: utf-8 -*-

###################################################################################
# Installation
###################################################################################
# pip install bokeh

###################################################################################
# streamlit run /home/ai-user/Documents/Demo/generate_graph.py

import os
import pandas as pd

from bokeh.plotting import figure, output_file, show
from bokeh.embed import components

from bokeh.models import ColumnDataSource
from bokeh.models import Legend
from bokeh.transform import dodge
   
def getPredDengueCases(startDate, endDate):
    # Simulate the object returned from Prediction Module
    df=pd.read_csv("predicted_cases.csv", header=0, parse_dates=['date'])
    newDf = (df['date'] >= startDate) & (df['date'] <= endDate)
    predCases = df.loc[newDf]
    return predCases

def generateGraphForActualAndPredictedDengueCases(startDate, endDate, predCases, displayWeather):
    print ('startDate: '+startDate)
    print ('endDate  : '+endDate)
    
    predCases['date_str']=predCases['date'].astype(str)
    
    # Fetch Actual Weather Conditions and Cases 
    df=pd.read_csv("cleaned.csv", header=0, parse_dates=['date'])
    df['date_str']=df['date'].astype(str)
    newDf = (df['date'] >= startDate) & (df['date'] <= endDate)
    histCases = df.loc[newDf]
    
    # create a new plot
    output_file("graph.html")
    p = figure(plot_width=800, plot_height=300, title="Actual Cases vs Predicted Cases", x_range=histCases['date_str'])
    p.toolbar.autohide = True
    
    if (displayWeather):
        data = {'date_str' : histCases['date_str'],
                'mean_temp': histCases['mean_temp'],
                'max_temp' : histCases['max_temp'],
                'min_temp' : histCases['min_temp'],
                'humidity' : histCases['humidity'],
                'mean_rain_fall' : histCases['mean_rain_fall'],
                'mean_wind' : histCases['mean_wind']}
        source = ColumnDataSource(data=data)
        p1=p.vbar(x=dodge('date_str', -0.25, range=p.x_range), top='mean_temp', width=0.1, source=source, color='#3288bd')
        p2=p.vbar(x=dodge('date_str',  -0.15,  range=p.x_range), top='max_temp', width=0.1, source=source, color='#99d594')
        p3=p.vbar(x=dodge('date_str',  -0.05, range=p.x_range), top='min_temp', width=0.1, source=source, color='#e6f598')
        p4=p.vbar(x=dodge('date_str', 0.05, range=p.x_range), top='humidity', width=0.1, source=source, color='#fee08b')
        p5=p.vbar(x=dodge('date_str',  0.15,  range=p.x_range), top='mean_rain_fall', width=0.1, source=source, color='#fc8d59')
        p6=p.vbar(x=dodge('date_str',  0.25, range=p.x_range), top='mean_wind', width=0.1, source=source, color='#d53e4f')    
        p7=p.line(histCases['date_str'], histCases['cases'], color='navy', alpha=0.5, line_width=3)
        p8=p.line(predCases['date_str'], predCases['cases'], color='red', alpha=0.5, line_width=3)
    
        legend = Legend(items=[
            ("Actual Cases", [p7]),
            ("Predicted Cases", [p8]),
            ("Mean Temp" , [p1]),
            ("Max Temp" , [p2]),
            ("Min Temp" , [p3]),
            ("Humidity" , [p4]),
            ("Mean Rain Fall" , [p5]),
            ("Mean Wind" , [p6]),
            ], location="top_left")
    else:
        p1=p.line(histCases['date_str'], histCases['cases'], color='navy', alpha=0.5, line_width=3)
        p2=p.line(predCases['date_str'], predCases['cases'], color='red', alpha=0.5, line_width=3)
    
        legend = Legend(items=[
            ("Actual Cases", [p1]),
            ("Predicted Cases", [p2])
            ], location="top_left")
        
    startDate_Formatted =  startDate[8:10] + "-" + startDate[5:7] + "-" + startDate[0:4]
    endDate_Formatted =  endDate[8:10] + "-" + endDate[5:7] + "-" + endDate[0:4]
    p.xaxis.axis_label = 'Date ('+startDate_Formatted+' to '+endDate_Formatted+')'
    p.yaxis.axis_label = 'Number of cases'
    legend.click_policy="hide"
    p.add_layout(legend, 'right')

    show(p)
    return components(p)

####################################################
path = '/home/ai-user/Documents/Demo'
os.chdir(path)

predCases=getPredDengueCases('2020-10-01', '2020-10-05') # Simulate Pred cases

# To show shorter date ranges, we can show weather conditions
script, div = generateGraphForActualAndPredictedDengueCases(
    '2020-10-01',   # startDate YYYY-MM-DD
    '2020-10-10',   # endDate YYYY-MM-DD
    #'2020-10-01',  # startDate YYYY-MM-DD
    #'2020-10-05',  # endDate YYYY-MM-DD
    predCases,      # List of Predicted Cases
    bool(True))     # Show weather conditions

# To show longer date ranges, it is best to hide weather conditions
script, div = generateGraphForActualAndPredictedDengueCases(
    '2020-09-01',   # startDate YYYY-MM-DD
    '2020-11-30',   # endDate YYYY-MM-DD
    #'2020-10-01',  # startDate YYYY-MM-DD
    #'2020-10-05',  # endDate YYYY-MM-DD
    predCases,      # List of Predicted Cases
    bool(False))     # Hide weather conditions

   
####################################################


