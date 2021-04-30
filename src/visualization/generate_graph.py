# -*- coding: utf-8 -*-
import logging
import pandas as pd

from bokeh.plotting import figure, output_file, show
from bokeh.embed import components

from bokeh.models import ColumnDataSource
from bokeh.models import Legend
from bokeh.models import Grid
from bokeh.models import LinearAxis
from bokeh.models import HoverTool
from bokeh.transform import dodge

logging.basicConfig(level=logging.INFO)

class GenerateGraph:
    
    def __init__(self, actualDataCsv : str):
        self.ACTUAL_DATA_CSV = actualDataCsv

    def create_hover_tool(self):
        """Generates the HTML for the Bokeh's hover data tool on our graph."""
        hover_html = """
        <div>
            <span class="hover-tooltip">$x</span>
        </div>
        """
        return HoverTool(tooltips=hover_html)

    def getPredDengueCases(self, startDate, endDate):
        # Simulate the object returned from Prediction Module
        df=pd.read_csv("predicted_cases.csv", header=0, parse_dates=['date'])
        newDf = (df['date'] >= startDate) & (df['date'] <= endDate)
        predCases = df.loc[newDf]
        return predCases

    def generateGraphForActualAndPredictedDengueCases(self, startDate, endDate, predCases, displayWeather):
        print ('startDate: '+startDate)
        print ('endDate  : '+endDate)
        
        predCases['date_str']=predCases['date'].astype(str)
        # print(predCases)
        
        # Fetch Actual Weather Conditions and Cases 
        df=pd.read_csv(self.ACTUAL_DATA_CSV, header=0, parse_dates=['date'])
        df['date_str']=df['date'].astype(str)
        df.sort_values(by='date')
        newDf = (df['date'] >= startDate) & (df['date'] <= endDate)
        histCases = df.loc[newDf]
        
        # hover_tool= create_hover_tool()
        # tools = [hover_tool,]

        # create a new plot
        # output_file("graph.html")
        # p = figure(plot_width=800, plot_height=300, title="Actual Cases vs Predicted Cases", x_range=histCases['date_str'], tools=tools)
        p = figure(plot_width=1000, plot_height=400, title="Actual Cases vs Predicted Cases", x_range=histCases['date_str'])
        p.xaxis.major_label_orientation = 1.570796326794897
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
            p7=p.line(histCases['date_str'], histCases['cases'], color='navy', alpha=0.7, line_width=1.5)
            p8=p.line(predCases['date_str'], predCases['cases'], color='red', alpha=0.7, line_width=1.5)
        
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
            p1=p.line(histCases['date_str'], histCases['cases'], color='navy', alpha=0.7, line_width=1.5)
            p2=p.line(predCases['date_str'], predCases['cases'], color='red', alpha=0.7, line_width=1.5)
        
            legend = Legend(items=[
                ("Actual Cases", [p1]),
                ("Predicted Cases", [p2])
                ], location="top_left")
            
        startDate_Formatted =  startDate[8:10] + "-" + startDate[5:7] + "-" + startDate[0:4]
        endDate_Formatted =  endDate[8:10] + "-" + endDate[5:7] + "-" + endDate[0:4]

        p.xaxis.axis_label = 'Date ('+startDate_Formatted+' to '+endDate_Formatted+')'
        p.xaxis.major_label_orientation = 1

        p.yaxis.axis_label = 'Number of cases'
        legend.click_policy="hide"

        p.add_layout(legend, 'right')
        
        return p

