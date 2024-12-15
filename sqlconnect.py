import mysql.connector
from mysql.connector import Error
import streamlit as st
import pandas as pd
import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


def create_connection():
    """Establishes a connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        if connection.is_connected():
            print("Connection to MySQL database was successful!")
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# Fetch Data from Table
def fetch_data(query):
    conn = create_connection()
    if conn:
        try:
            df = pd.read_sql(query, conn)
            conn.close()
            return df
        except Exception as e:
            st.error(f"Error fetching data: {e}")
    return None


# Perform CRUD Operation
def execute_query(query, params=None):
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            st.error(f"Error executing query: {e}")
    return False


def update_data(table_name, set_column, set_value, condition_column, condition_value):
    conn = create_connection()  # Use MySQL connection
    if conn:
        try:
            cursor = conn.cursor()
            
            # SQL query to update data
            query = f"""
            UPDATE {table_name}
            SET {set_column} = %s
            WHERE {condition_column} = %s;
            """
            
            # Execute the query
            cursor.execute(query, (set_value, condition_value))
            conn.commit()

            if cursor.rowcount > 0:
                return f"Successfully updated {cursor.rowcount} row(s) in the '{table_name}' table."
            else:
                return f"No rows matched the condition in the '{table_name}' table."
        except Error as e:
            return f"An error occurred: {e}"
        finally:
            conn.close()

# Main CRUD Function
def main2():
    # App Header
    #st.title("CRUD Operations")
    st.sidebar.header("CRUD Options")
    
    # Sidebar Navigation
    options = ["View Data", "Add Data", "Update Data", "Delete Data", "Run Custom Query"]
    choice = st.sidebar.selectbox("Choose an option", options)

    # Table Options
    table_names = ["Country_GDP", "tourism_data", "unemployment_data", "cost_of_living_data"]

    # View Data
    if choice == "View Data":
        st.header("View Data")
        selected_table = st.selectbox("Select a table to view", table_names)
        query = f"SELECT * FROM {selected_table}"
        df = fetch_data(query)
        if df is not None:
            st.dataframe(df)

    # Add Data
    elif choice == "Add Data":
        st.header("Add Data")
        selected_table = st.selectbox("Select a table to add data", table_names)

        if selected_table == "Country_GDP":
            number = st.number_input("Number", min_value=1, step=1)
            country = st.text_input("Country")
            gdp_ppp = st.number_input("GDP (PPP) 2022", min_value=0.0, step=0.1)
            if st.button("Add Country GDP Data"):
                query = "INSERT INTO Country_GDP (Number, Country, GDP_PPP_2022) VALUES (%s, %s, %s)"
                params = (number, country, gdp_ppp)
                if execute_query(query, params):
                    st.success("Data added successfully!")

        elif selected_table == "tourism_data":
            country = st.text_input("Country")
            tourists = st.number_input("Tourists (in millions)", min_value=0.0, step=0.1)
            receipts = st.number_input("Receipts (in billions)", min_value=0.0, step=0.01)
            receipts_per_tourist = st.number_input("Receipts Per Tourist", min_value=0, step=1)
            percentage_gdp = st.number_input("Percentage of GDP", min_value=0.0, step=0.1)
            if st.button("Add Tourism Data"):
                query = "INSERT INTO tourism_data (country, tourists_in_millions, receipts_in_billions, receipts_per_tourist, percentage_of_gdp) VALUES (%s, %s, %s, %s, %s)"
                params = (country, tourists, receipts, receipts_per_tourist, percentage_gdp)
                if execute_query(query, params):
                    st.success("Data added successfully!")

        elif selected_table == "unemployment_data":
            country = st.text_input("Country")
            unemployment_rate = st.number_input("Unemployment Rate", min_value=0.0, step=0.1)
            if st.button("Add Unemployment Data"):
                query = "INSERT INTO unemployment_data (country, unemployment_rate) VALUES (%s, %s)"
                params = (country, unemployment_rate)
                if execute_query(query, params):
                    st.success("Data added successfully!")

        elif selected_table == "cost_of_living_data":
            country = st.text_input("Country")
            cost_index = st.number_input("Cost Index", min_value=0.0, step=0.1)
            monthly_income = st.number_input("Monthly Income", min_value=0.0, step=0.01)
            purchasing_power_index = st.number_input("Purchasing Power Index", min_value=0.0, step=0.1)
            if st.button("Add Cost of Living Data"):
                query = "INSERT INTO cost_of_living_data (country, cost_index, monthly_income, purchasing_power_index) VALUES (%s, %s, %s, %s)"
                params = (country, cost_index, monthly_income, purchasing_power_index)
                if execute_query(query, params):
                    st.success("Data added successfully!")

    # Update Data
    elif choice == "Update Data":
        st.header("Update Data")
        st.info("Update records in the database by specifying the table and conditions.")
        table_names2 = ["Country_GDP", "tourism_data", "unemployment_data", "cost_of_living_data"]
        selected_table2 = st.selectbox("Select a table", table_names2)
        # Input fields for update operation
        # table_name = st.text_input("Enter Table Name")
        set_column = st.text_input("Enter Column to Update")
        set_value = st.text_input("Enter New Value for the Column")
        condition_column = st.text_input("Enter Condition Column (e.g., Primary Key or Unique Identifier)")
        condition_value = st.text_input("Enter Value of the Condition Column")
        
        if st.button("Update Record"):
            if not all([selected_table2, set_column, set_value, condition_column, condition_value]):
                st.warning("Please fill out all fields to update data.")
            else:
                try:
                    # Update function call
                    result = update_data(
                        selected_table2,
                        set_column,
                        set_value,
                        condition_column,
                        condition_value
                    )
                    st.success(result)
                except Exception as e:
                    st.error(f"Error: {e}")

    # Delete Data
    elif choice == "Delete Data":
        st.header("Delete Data")
        selected_table = st.selectbox("Select a table to delete data from", table_names)
        primary_key = st.text_input(f"Enter Primary Key value for table `{selected_table}`")
        if st.button("Delete Data"):
            if selected_table == "Country_GDP":
                query = "DELETE FROM Country_GDP WHERE Country = %s"
            elif selected_table == "tourism_data":
                query = "DELETE FROM tourism_data WHERE country = %s"
            elif selected_table == "unemployment_data":
                query = "DELETE FROM unemployment_data WHERE country = %s"
            elif selected_table == "cost_of_living_data":
                query = "DELETE FROM cost_of_living_data WHERE country = %s"
            else:
                st.error("Invalid table selected.")
                query = None

            if query:
                params = (primary_key,)
                if execute_query(query, params):
                    st.success("Data deleted successfully!")

    # Run Custom Query
    elif choice == "Run Custom Query":
        st.header("Run Custom Query")
        custom_query = st.text_area("Enter your SQL query")
        if st.button("Execute Query"):
            df = fetch_data(custom_query)
            if df is not None:
                st.dataframe(df)

