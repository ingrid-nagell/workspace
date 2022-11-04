import pandas as pd
df = pd.read_csv("./python_bootcamp/boot25_pandas/weather_data.csv", sep=",")

print(df["temp"].max())