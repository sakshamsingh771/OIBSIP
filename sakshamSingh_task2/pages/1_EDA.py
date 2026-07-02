import streamlit as st
import pandas as pd
import plotly.express as px
from utils.preprocessing import load_data

df1, df2 = load_data()

st.title("Exploratory Data Analysis")

st.write(df1.head())

st.subheader("Dataset Information")

st.write(df1.describe())

fig = px.histogram(
    df1,
    x="Estimated Unemployment Rate (%)",
    nbins=20,
    title="Distribution of Unemployment Rate"
)

st.plotly_chart(fig)