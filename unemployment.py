import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

df_unemployment=pd.read_csv('df_unemployment.csv')

def Unemployment():
    
    # Bar Chart: Unemployment Rate by Country (Horizontal)
    fig_bar_unemployment = px.bar(
        df_unemployment,
        x="unemployment_rate",
        y="country",
        title="Unemployment Rate by Country",
        labels={"unemployment_rate": "Unemployment Rate (%)", "country": "Country"},
        orientation="h",  # Horizontal bar chart
    )

    # Update Layout for the Bar Chart
    fig_bar_unemployment.update_layout(
        xaxis_title="Unemployment Rate (%)",
        yaxis_title="Country",
        template="plotly_white",
        margin=dict(l=100, r=50, t=50, b=50),
    )

    # Display the bar chart in Streamlit
    st.plotly_chart(fig_bar_unemployment, use_container_width=True)