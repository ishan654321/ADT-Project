import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

df_gdp=pd.read_csv('df_gdp.csv')

def GDP():
    
    # Line Chart for GDP per Capita
    fig_line = px.line(
        df_gdp,
        x="Country",
        y="GDP_PPP_2022",
        title="GDP per Capita by Country (Line Chart)",
        labels={"gdp_per_capita": "GDP per Capita (USD)", "country": "Country"},
        markers=True,  # Adds markers at each data point
    )

    # Adjust layout for line chart
    fig_line.update_layout(
        xaxis_title="Country",
        yaxis_title="GDP per Capita (USD)",
        template="plotly_white",
        margin=dict(l=50, r=50, t=50, b=50),
    )

    # Display the line chart in Streamlit
    st.plotly_chart(fig_line, use_container_width=True)