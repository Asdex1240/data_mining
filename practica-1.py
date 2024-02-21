import pandas as pd
from tabulate import tabulate
file = 'athlete_events.csv'

df = pd.read_csv(file)

df_cleaned = df.dropna(subset=['Height'])

print(df_cleaned)
