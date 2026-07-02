import pandas as pd


def load_data():

    df1 = pd.read_csv("data/Unemployment in India.csv")
    df2 = pd.read_csv("data/Unemployment_Rate_upto_11_2020.csv")

    df1.columns = df1.columns.str.strip()
    df2.columns = df2.columns.str.strip()

    df1["Date"] = pd.to_datetime(df1["Date"])
    df2["Date"] = pd.to_datetime(df2["Date"])

    return df1, df2    
    