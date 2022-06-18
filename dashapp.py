from turtle import color
from dash import Dash,html,dcc
from plotmaker import PlotMaker

app = Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(children=[
    html.H1(children="Data Analysis Demo Application",style={"textAlign":"center","color":'#7FDBFF'}),
    html.Div(children="Choropleth MAP Application Intergration Unemployment Data"),
    dcc.Graph(id="Choropleth Graph",figure= PlotMaker().choromap("Unemployment Data India","States","Unemployment")),
    html.Div(children="Choropleth MAP Application Intergration Population Data"),
    dcc.Graph(id="Bar Graph",figure= PlotMaker().barmap("Population Data India","State","StateWise Population (Crore)")),
    html.Div(children="Choropleth MAP Application Intergration Literacy Data"),
    dcc.Graph(id="Scatter Graph",figure= PlotMaker().scattermap("Population Data India","States","Literacy"))

])

if __name__ == "__main__":
    app.run_server(debug=True)