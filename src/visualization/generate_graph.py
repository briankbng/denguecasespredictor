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
 
def getHistDengueCases(startDate, endDate):
    
    print ('startDate: '+startDate)
    print ('endDate  : '+endDate)
    
    path = '/home/ai-user/Documents/Demo'
    os.chdir(path)
    df=pd.read_csv("dengue_cases_2014to2018.csv", header=0, parse_dates=['date'])
    #df.info()
    newDf = (df['date'] >= startDate) & (df['date'] <= endDate)
    histCases = df.loc[newDf]
    return histCases
    
def getPredDengueCases(startDate, endDate):
    
    print ('startDate: '+startDate)
    print ('endDate  : '+endDate)
    
    path = '/home/ai-user/Documents/Demo'
    os.chdir(path)
    df=pd.read_csv("Prediction 2015.csv", header=0, parse_dates=['date'])
    #df.info()
    newDf = (df['date'] >= startDate) & (df['date'] <= endDate)
    predCases = df.loc[newDf]
    return predCases

def generateGraphForHistoricalAndPredictedDengueCases(startDate, endDate, predCases):
    histCases=getHistDengueCases(startDate, endDate)
    print('*** HistCases ***')
    print(histCases)
   
    output_file("graph.html")
    
    # create a new plot with a datetime axis type
    p = figure(plot_width=800, plot_height=300, x_axis_type="datetime")
    #p = figure(plot_width=800, plot_height=250, x_axis_type="datetime", tools='xwheel_pan', active_scroll='xwheel_pan')
    
    p.line(histCases['date'], histCases['cases'], color='navy', alpha=0.5)
    p.line(predCases['date'], predCases['cases'], color='red', alpha=0.5)
    show(p)
    return components(p)


predCases=getPredDengueCases('10-11-2015', '10-15-2015') # Simulate Pred cases
print('*** PredCases ***')
print(predCases)
print('')
script, div = generateGraphForHistoricalAndPredictedDengueCases('10-01-2015', '10-30-2015', predCases)

print('*** script ***')
print(script)
print('')

print('*** div ***')
print(div)
print('')

####################################################


