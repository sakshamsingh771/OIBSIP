import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Title
st.title("🌸 Iris Flower Classification")

# Load Data
df = pd.read_csv("Iris.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

# Features and Target
X = df.drop(["Id", "Species"], axis=1)
y = df["Species"]

# Train Model
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = RandomForestClassifier()
model.fit(X_train, y_train)

# User Inputs
st.subheader("Enter Flower Measurements")

sl = st.slider("Sepal Length", 4.0, 8.0, 5.0)
sw = st.slider("Sepal Width", 2.0, 5.0, 3.0)
pl = st.slider("Petal Length", 1.0, 7.0, 4.0)
pw = st.slider("Petal Width", 0.1, 3.0, 1.0)

if st.button("Predict"):
    prediction = model.predict([[sl, sw, pl, pw]])
    st.success(f"Predicted Species: {prediction[0]}")
    