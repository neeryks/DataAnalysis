
import pandas as pd
from baseplot import geoindiastate as gis
from tkinter import filedialog as fd
import time

class PlotMaker:
    def __init__(self) -> None:
        pass

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
    
    def choromap(self,Name_of_Choroplot,reference_column,color_column):
        fig = gis(self.file_selector(),Name_of_Choroplot).showmap(reference_column,color_column)
        return fig
    
    def barmap(self,Name_of_bar_plot,Xaxis,Yaxis):
        fig = gis(self.file_selector(),Name_of_bar_plot).barplot(Xaxis,Yaxis)
        return fig
    
    def scattermap(self,Name_of_scatter_plot,Xaxis,Yaxis):
        fig = gis(self.file_selector(),Name_of_scatter_plot).scatterplot(Xaxis,Yaxis)
        return fig

