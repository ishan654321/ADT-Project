import streamlit as st

def home():
    st.write('This project is about analysis of economic data and performance of countries based on various parameters.')
    st.write('The purpose of this project is to create a web application for managing and analyzing economy-related data. The app is designed to facilitate updates, queries, and visualization of data for countries, including statistics such as GDP, tourism data, cost of living, corruption, and unemployment. The primary audience includes economists, students and professionals in data analysis, database management, and web development, as well as tourism researchers who require an easy-to-use tool for handling economy and tourism data.')
    st.markdown('''Functionalities
The web app includes the following functionalities:
1.	View Data: Displays all the data in an easy-to-read table format.
2.	Add Records: Allows users to insert new data in any of the tables.
3.	Update Records: Users can update existing records by specifying conditions (e.g., updating the GDP or the number of tourists for a specific country).
4.	Delete Records: Enables deletion of selected records from the database.
5.	Run Custom Query: Users can search and filter records based on their requirements.
6.	Visualization: Generates bar charts and other graphical representations for better data insights for various tables.''')