import pandas as pd
from basemap import geoindiastate as gis
from tkinter import filedialog as fd
import time


print("Select The File ")
time.sleep(3)
file = fd.askopenfilename()
file_ext = file.split(".")[-1]

print(f'You selected a "{file_ext}" file')

ext_dict = {
            "csv":pd.read_csv,
            "xlsx":pd.read_excel,
            "json":pd.read_json,
            "sql":pd.read_sql}
df = ext_dict[file_ext](file)
attl = []
print("Column Names :")
for x in df.columns:
    print(x)
att_list = ["reference column name","plot for column name","name of map"]
for attributes in att_list:
    att = input(f'Enter {attributes}: ')
    attl.append(att)
fig = gis(df,attl[0],attl[1],attl[2])
fig.showmap()



