import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

df_tourism=pd.read_csv('df_tourism.csv')

def Tourism():
    # 1. Bar Chart: Tourists vs Receipts
    fig_bar_tourists_receipts = px.bar(
        df_tourism,
        x="country",
        y=["tourists_in_millions", "receipts_in_billions"],
        title="Tourists vs Receipts by Country",
        labels={
            "tourists_in_millions": "Tourists (Millions)",
            "receipts_in_billions": "Receipts (Billions)",
        },
        barmode="group",  # Group the bars for comparison
    )

    # Display Bar Chart
    st.plotly_chart(fig_bar_tourists_receipts, use_container_width=True)

    # 2. Pie Chart: Percentage of GDP from Tourism
    fig_pie_gdp_percentage = px.pie(
        df_tourism,
        names="country",
        values="percentage_of_gdp",
        title="Percentage of GDP Contributed by Tourism",
        labels={"percentage_of_gdp": "Percentage of GDP"},
    )

    # Display Pie Chart
    st.plotly_chart(fig_pie_gdp_percentage, use_container_width=True)

    # 3. Scatter Plot: Tourists vs Receipts
    fig_scatter_tourists_receipts = px.scatter(
        df_tourism,
        x="tourists_in_millions",
        y="receipts_in_billions",
        title="Tourists vs Receipts by Country",
        labels={
            "tourists_in_millions": "Tourists (Millions)",
            "receipts_in_billions": "Receipts (Billions)",
        },
        color="country",  # Color by country for distinction
        hover_name="country",  # Hover over the country name
    )

    # Display Scatter Plot
    st.plotly_chart(fig_scatter_tourists_receipts, use_container_width=True)

    # 4. Bar Chart: Receipts per Tourist
    fig_bar_receipts_per_tourist = px.bar(
        df_tourism,
        x="country",
        y="receipts_per_tourist",
        title="Receipts per Tourist by Country",
        labels={"receipts_per_tourist": "Receipts per Tourist (USD)"},
    )

    # Display Bar Chart
    st.plotly_chart(fig_bar_receipts_per_tourist, use_container_width=True)

    # 5. Line Chart: Percentage of GDP from Tourism
    fig_line_gdp_percentage = px.line(
        df_tourism,
        x="country",
        y="percentage_of_gdp",
        title="Percentage of GDP from Tourism by Country",
        labels={"percentage_of_gdp": "Percentage of GDP"},
        markers=True,  # Adds markers to each data point
    )

    # Display Line Chart
    st.plotly_chart(fig_line_gdp_percentage, use_container_width=True)
