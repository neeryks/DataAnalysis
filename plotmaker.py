
import pandas as pd
from baseplot import geoindiastate as gis
from tkinter import filedialog as fd
import time

class PlotMaker:

    def file_selector(self):
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
        return df
    
    def plot_maker(self):
        Choose_plot = input("Enter Plot Type: ")
        choice_df = {
            "choropleth":gis(self.file_selector(),input("Name of Choropleth Plot: ")).showmap(input("reference Column: "),input("What to plot for : ")),
            "bar":gis(self.file_selector(),input("Name of Bar Plot: ")).barplot(input("X-Axis: "),input("Y-Axis: ")),
            "scatter":gis(self.file_selector(),input("Name of Scatter Plot: ")).scatterplot(input("X-Axis: "),input("Y-Axis: "))}
        figure = choice_df[Choose_plot]
        return figure

plot = PlotMaker()
plot.plot_maker()
