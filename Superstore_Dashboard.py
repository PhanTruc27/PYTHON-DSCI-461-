import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Superstore", page_icon = ":bar_chart:", layout="wide")
st.write("Let's buil the first streamlit dashboard together")
st.title("Let's build the first Streamlit dashboard together")


st.title("📊 Dashboard: Superstore")

fl = st.file_uploader("📁 Upload a file", type=["csv", "txt"])

if fl is not None:
    st.write("Uploaded file:", fl.name)
    df = pd.read_csv(fl, encoding="ISO-8859-1")
else:
    df = pd.read_csv(
        r"C:\Users\HP\Desktop\PYTHON DSCI 461\streamlit\Sample - Superstore.csv",
        encoding="ISO-8859-1"
    )

st.dataframe(df)

#Filter data by time
#create two columns

col1, col2 = st.columns(2)
df['Order Date'] = pd.to_datetime(df['Order Date'])


#get the min and max date
# get the min and max date
startDate = pd.to_datetime(df['Order Date']).min()
endDate = pd.to_datetime(df['Order Date']).max()

with col1:
    date1 = pd.to_datetime(
        st.date_input("Start date", startDate)
    )

with col2:
    date2 = pd.to_datetime(
        st.date_input("End date", endDate)
    )

# filter dataframe
df = df[
    (df['Order Date'] >= date1) &
    (df['Order Date'] <= date2)
].copy()
