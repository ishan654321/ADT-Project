import mysql.connector
import streamlit as st

# Establish a connection to MySQL Server

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="ADT Project Database"


)
mycursor=mydb.cursor()
print("Connection Established")
