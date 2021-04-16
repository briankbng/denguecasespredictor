# -*- coding: utf-8 -*-

###################################################################################
# Installation
###################################################################################
# pip install streamlit
# pip install altair vega_datasets (Note: No need to run this)

###################################################################################
# streamlit run /home/ai-user/Documents/Demo/generate_graph.py

import os
import numpy as np
import pandas as pd
import streamlit as st
import altair as alt

st.write("""
# Dengue Predictor
Prediction Date Range: *world!* to *world!*
""")

path = '/home/ai-user/Documents/Demo'
os.chdir(path)
data2015=pd.read_csv("Dengue Cases 2015.csv", header=0, parse_dates=['Date'])
#data2015.info()
pred2015=pd.read_csv("Prediction 2015.csv", header=0, parse_dates=['Date'])
#pred2015.info()
data2016=pd.read_csv("Dengue Cases 2016.csv", header=0, parse_dates=['Date'])
#data2016.info()

data2015 = data2015.set_index('Date')
pred2015 = pred2015.set_index('Date')
data2016 = data2016.set_index('Date')

#st.line_chart(data2015)
#st.line_chart(pred2015)

result = data2015.join(pred2015, how='outer', on='Date', lsuffix='_Actual', rsuffix='_Predicted')
#result
st.line_chart(result)

# ***************************************
st.write("Chart 2")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Actual', 'Predicted', 'Rainfall'])
st.line_chart(chart_data)

# ***************************************
st.write("Chart 3")
df = pd.DataFrame({
    'name': ['tom', 'dominik', 'patricia'],
    'age': [20, 30, 40],
    'salary': [100, 200, 300]
})

a = alt.Chart(df).mark_area(opacity=1).encode(
    x='name', y='age')

b = alt.Chart(df).mark_line(opacity=0.6).encode(
    x='name', y='salary')

c = alt.layer(a, b)

st.altair_chart(c, use_container_width=True)

