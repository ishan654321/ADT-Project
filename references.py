import streamlit as st
def Ref():
    st.markdown('We have created project using MySQL Workbench(8.0 CE), VSCode, Python 3.10.2 and various libraries of python like pandas, sqlite3, plotly and streamlit framework.')
    st.markdown('''References
	Frameworks and Tools:
	\nStreamlit Documentation
	\nSQLite Documentation
	\n<a href="https://dev.mysql.com/doc/" target="_blank">MySQL Documentation</a>\n
	\nLibraries:
	pandas for data manipulation.
	plotly for visualizations.\n
                                
	\nCommunity Resources:
	Stack Overflow discussions on database queries and Streamlit components.\n
                
	\nData: 
	\n<a href="https://www.worldometers.info/gdp/gdp-per-capita/" target="_blank">GDP Per Capita</a>
    \nTourism <a href="https://en.wikipedia.org/wiki/World_Tourism_rankings" target="_blank">[1]</a><a href="https://www.unwto.org/tourism-data/un-tourism-tourism-dashboard" target="_blank">[2]</a>
	\n<a href="https://www.transparency.org/en/cpi/2023" target="_blank">Corruption</a>
''',unsafe_allow_html=True)