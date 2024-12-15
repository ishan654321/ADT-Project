from cost_of_living import CostofLiving
from Corruption import Corruption
from gdp import GDP
from home import home
from tourism import Tourism
from unemployment import Unemployment
from references import Ref
import streamlit as st
import streamlit as st
from sqlconnect import main2

st.set_page_config(page_title='ADT Project')

# Sidebar with navigation buttons
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("Home","Cost of Living Analysis", "Corruption Analysis", "GDP Analysis","Tourism Analysis","Unemployment Analysis","References","CRUD"))


# Main content based on the selected page
if page == "Home":
    st.title("Home")
    home()

elif page == "Cost of Living Analysis":
    st.title("Cost of Living Analysis")
    CostofLiving()

elif page == "Corruption Analysis":
    st.title("Corruption Analysis")
    Corruption()

elif page == "GDP Analysis":
    st.title("GDP Analysis")
    GDP()

elif page=="Tourism Analysis":
    st.title("Tourism Analysis")
    Tourism()

elif page=="Unemployment Analysis":
    st.title("Unemployment Analysis")
    Unemployment()

elif page=="References":
    st.title("References")
    Ref()

elif page=="CRUD":
    st.title("CRUD Operations")
    main2()