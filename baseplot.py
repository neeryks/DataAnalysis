import json
import plotly.express as px

class geoindiastate:
    def __init__(self,file_Csv_etc,Name_of_map_or_graph) -> None:
        self.file = file_Csv_etc
        self.geo_file = json.load(open("geojsondata/india_statenew.geojson","r"))
        self.name = Name_of_map_or_graph

    def showmap(self,reference_to_map_with,What_to_plot_for):
        fig = px.choropleth(self.file,geojson=self.geo_file,locations=reference_to_map_with,featureidkey="properties.ST_NM",color=What_to_plot_for,template="seaborn")
        fig.update_geos(fitbounds="locations", visible=False)
        fig.update_layout(height=800,title_text= self.name)
        fig.update_traces(marker_line_width=1, marker_opacity=1,marker_line_color = "white")
        return fig.show()

    def barplot(self,xaxis,yaxis):
        fig = px.bar(self.file,x=xaxis,y=yaxis)
        return fig.show()

    def scatterplot(self,xaxis,yaxis):
        fig = px.scatter(self.file,x=xaxis,y=yaxis)
        return fig.show()
    

