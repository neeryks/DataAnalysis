from dash import Dash,html,dcc
from plotmaker import PlotMaker

app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children="Data Analysis Demo Application"),
    html.Div(children="Choropleth MAP Application Intergration Unemployment Data"),
    dcc.Graph(id="Choropleth Graph",figure= PlotMaker().choromap("Unemployment Data India","States","Unemployment")),
    html.Div(children="Choropleth MAP Application Intergration Population Data"),
    dcc.Graph(id="Choropleth Graph",figure= PlotMaker().barmap("Population Data India","State","StateWise Population (Crore)")),
    html.Div(children="Choropleth MAP Application Intergration Literacy Data"),
    dcc.Graph(id="Choropleth Graph",figure= PlotMaker().scattermap("Population Data India","States","Literacy"))

])

if __name__ == "__main__":
    app.run_server(debug=True)