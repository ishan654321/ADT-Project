import plotly.express as px
import streamlit as st


import pandas as pd
df_cost_of_living=pd.read_csv('df_cost_of_living.csv')
def CostofLiving():

    # Sort the DataFrame by monthly income in descending order
    df_sorted = df_cost_of_living.sort_values(by="monthly_income", ascending=False)

    # If there are more than 10 rows, select the top 10
    df_top_10 = df_sorted.head(10)

    fig = px.bar(
    df_top_10,
    x="country",
    y="monthly_income",
    title="Top 10 Countries by Monthly Income",
    labels={"monthly_income": "Monthly Income (USD)", "country": "Country"},
    text="monthly_income",
)
    fig.update_traces(texttemplate='%{text:.2s}', textposition="outside")

    # Plotting using Plotly
    fig.update_layout(
    xaxis_title="Country",
    yaxis_title="Monthly Income (USD)",
    yaxis=dict(showgrid=True),
    xaxis=dict(showgrid=False),
    template="plotly_white",
    margin=dict(l=50, r=50, t=50, b=100), 
)
    # Show the figure
    st.plotly_chart(fig, use_container_width=True)


    fig2 = px.scatter(
    df_cost_of_living,
    x="monthly_income",
    y="purchasing_power_index",
    title="Scatter Plot for Income vs Purchase Power",
    color="monthly_income",
    text="country",
    labels={
        "monthly_income": "Monthly Income (USD)",
        "purchasing_power_index": "Purchasing Power Index",
    },
    size="purchasing_power_index",
    size_max=1,
)
    fig2.update_traces(textposition="top center",
    marker=dict(opacity=0.8, line=dict(width=1, color="DarkSlateGrey")),)

    # Plotting using Plotly
    fig2.update_layout(
    xaxis_title="Monthly Income (USD)",
    yaxis_title="Purchasing Power Index",
    template="plotly_white",
    margin=dict(l=50, r=50, t=50, b=50),
)
    st.plotly_chart(fig2, use_container_width=True)

    fig3 = px.histogram(
    df_cost_of_living,
    x="purchasing_power_index",
    title="Histogram of Monthly Income vs Purchasing Power",
    labels={
        "purchasing_power_index": "Purchasing Power Index",
    },
    nbins=10,  # Number of bins for distribution
    opacity=0.7,
)
    # Plotting using Plotly
    fig3.update_layout(
    xaxis_title="Purchase Power Index",
    yaxis_title="Freqency",
    template="plotly_white",
    margin=dict(l=50, r=50, t=50, b=50),
)
    st.plotly_chart(fig3, use_container_width=True)