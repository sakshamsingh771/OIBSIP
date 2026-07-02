import streamlit as st
import plotly.express as px
from utils.preprocessing import load_data

df1, df2 = load_data()

st.title("Covid-19 Impact")

monthly = df2.groupby("Date")[
    "Estimated Unemployment Rate (%)"
].mean().reset_index()

fig = px.line(
    monthly,
    x="Date",
    y="Estimated Unemployment Rate (%)",
    title="Unemployment During Covid"
)

st.plotly_chart(fig)