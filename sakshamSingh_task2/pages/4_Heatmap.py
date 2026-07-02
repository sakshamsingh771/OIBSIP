import streamlit as st
import plotly.express as px
from utils.preprocessing import load_data

df1, df2 = load_data()

state_avg = df2.groupby(
    "Region"
)["Estimated Unemployment Rate (%)"].mean().reset_index()

fig = px.bar(
    state_avg,
    x="Region",
    y="Estimated Unemployment Rate (%)",
    title="Average State-wise Unemployment"
)

st.plotly_chart(fig)