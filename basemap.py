import json
import pandas as pd
import plotly.express as px
import json

class geoindiastate:
    def __init__(self,file_Csv_etc,reference_to_map_with,What_to_plot_for,Name_of_map) -> None:

        self.file = file_Csv_etc
        self.geo_file = json.load(open("geojsondata/india_statenew.geojson","r"))
        self.loc = reference_to_map_with
        self.col = What_to_plot_for
        self.name = Name_of_map
    def showmap(self):
        fig = px.choropleth(self.file,geojson=self.geo_file,locations=self.loc,featureidkey="properties.ST_NM",color=self.col,template="seaborn")
        fig.update_geos(fitbounds="locations", visible=False)
        fig.update_layout(height=800,title_text= self.name)
        fig.update_traces(marker_line_width=1, marker_opacity=1,marker_line_color = "white")
        return fig.show()
    

