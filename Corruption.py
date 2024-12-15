import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

df_income_corruption=pd.read_csv('df_income_corruption.csv')

def Corruption():
    
    df_income_corruption
    fig4 = px.box(
    df_income_corruption,
    x="corruption_index",
    title="Distribution of Annual Income by Corruption Index",
    labels={
        "corruption_index": "Corruption Index",
    },
)

    # Adjust layout
    fig4.update_layout(
    xaxis_title="Corruption Index",
    template="plotly_white",
    margin=dict(l=50, r=50, t=50, b=50),
)

    # Display the Plotly chart in Streamlit
    st.plotly_chart(fig4, use_container_width=True)