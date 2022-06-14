import pandas as pd

df = pd.read_excel("savedddata/datafiles/literacy.xlsx")
df.to_csv("savedddata/datafiles/literacy.csv")