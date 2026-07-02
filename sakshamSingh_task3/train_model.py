import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load Dataset
df = pd.read_csv("data/car data.csv")

# Create Age Column
df["Car_Age"] = 2026 - df["Year"]

# Drop unnecessary columns
df.drop(["Car_Name", "Year"], axis=1, inplace=True)

# Convert categorical columns
df = pd.get_dummies(
    df,
    columns=["Fuel_Type", "Selling_type", "Transmission"],
    drop_first=True
)

# Features and Target
X = df.drop("Selling_Price", axis=1)
y = df["Selling_Price"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Save Model
joblib.dump(model, "model/car_price_model.pkl")

# Save Columns
joblib.dump(X.columns.tolist(), "model/model_columns.pkl")

print("Model Saved Successfully")