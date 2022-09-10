import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import html, dcc, Input, Output

app = dash.Dash(external_stylesheets=[dbc.themes.FLATLY])

data = px.data.iris()

# data = pd.read_csv("filnavn.csv")
kolonner = data.columns
kolonne_valg = [
    {"label": "Bergbladlengde", "value": "sepal_length"},
    {"label": "Bergbladbredde", "value": "sepal_width"},
    {"label": "Kronbladlengde", "value": "petal_length"},
    {"label": "Kronbladbredde", "value": "petal_width"},
]

app.layout = html.Div([
    dbc.NavbarSimple(brand="IRIS", color="dark", dark=True),
    dbc.Container([
        dbc.FormFloating([
            dbc.Select(id="x-akse", options=kolonne_valg, value="sepal_length"),
            dbc.Label("X-akse"),
        ]),
        dbc.FormFloating([
            dbc.Select(id="y-akse", options=kolonne_valg, value="sepal_width"),
            dbc.Label("Y-akse"),
        ]),
        dcc.Graph(id="figur"),
        dcc.Markdown(id="info"),
    ])
])

@app.callback(
    Output("info", "children"),
    Input("figur", "selectedData")
)
def vis_info(info):
    if info:
        idx = info["points"][0]["pointIndex"]
        return str(data.iloc[idx])


@app.callback(
    Output("figur", "figure"),
    Input("x-akse", "value"),
    Input("y-akse", "value"),
    prevent_initial_call=False
    )
def oppdater_figur(x_akse, y_akse):
    return px.scatter(data, x=x_akse, y=y_akse, color="species")


app.run_server(debug=True)
