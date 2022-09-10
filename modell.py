import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import html, dcc, Input, Output

app = dash.Dash(external_stylesheets=[dbc.themes.FLATLY])


app.layout = html.Div([
    dbc.NavbarSimple(brand="Modell", color="dark", dark=True),
    dbc.Container([
        dcc.Slider(id="vekstrate", min=-30, max=30, value=10),
        dcc.Graph(id="befolkningsgraf"),
    ]),
])


@app.callback(
    Output("befolkningsgraf", "figure"),
    Input("vekstrate", "value"),    
)
def oppdater_befolkningsgraf(vekstrate):
    data = {"Befolkning": befolkning(100, vekstrate / 100, 200)}
    return px.line(data, range_y=(0, 200))


def befolkning(start, vekstrate, maks, antall_tidssteg=20):
    tidsserie = []
    
    nå = start
    for tidssteg in range(antall_tidssteg):
        tidsserie.append(nå)
        nå = nå + nå * vekstrate * (1 - nå/maks)

    return tidsserie

app.run_server(debug=True)
