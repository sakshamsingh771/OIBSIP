import streamlit as st
import plotly.express as px
from utils.preprocessing import load_data

df1, df2 = load_data()

state = st.selectbox(
    "Select State",
    df1["Region"].unique()
)

filtered = df1[df1["Region"] == state]

fig = px.line(
    filtered,
    x="Date",
    y="Estimated Unemployment Rate (%)",
    title=f"{state} Unemployment Trend"
)

st.plotly_chart(fig)