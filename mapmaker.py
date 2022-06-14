from turtle import end_fill
import pandas as pd
from basemap import geoindiastate as gis
from tkinter import filedialog as fd
import time


print("Select The File ")
time.sleep(2)
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
for x in enumerate(df.columns):
    print(f'{x[0]}: {x[1]}',end="\t")
print("<====CHOOSE FROM COLUMN NAMES")
choice = input(f'Plot-type: ')
if choice == "map":
    att_list = ["reference column name","plot for column name","name of map"]
    for attributes in att_list:
        att = input(f'Enter {attributes}: ')
        attl.append(att)
    fig = gis(df,attl[2])
    fig.showmap(attl[0],attl[1])
elif choice == "bar":
    wrd = input("Enter name of map ")
    fig = gis(df,wrd)
    fig.barplot(input("Enter X Axis "),input("Enter Y Axis "))



