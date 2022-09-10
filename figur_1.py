import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import html, dcc

app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])

data = px.data.iris()

# data = pd.read_csv("filnavn.csv")
kolonner = data.columns

figur = px.scatter(data, x=kolonner[0], y=kolonner[1])

app.layout = html.Div([
    dcc.Graph(figure=figur)
])

app.run_server(debug=True)
