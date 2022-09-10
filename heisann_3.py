import pathlib 

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, State

app = dash.Dash(external_stylesheets=[dbc.themes.PULSE])

app.layout = html.Div(
    [
        dbc.NavbarSimple(brand="Velkommen til Dashkurs", color="dark", dark=True),
        dbc.Container([
            dbc.Row([
                dcc.Markdown(pathlib.Path("intro.md").read_text(encoding="utf-8")),
                dbc.Col(
                    dbc.FormFloating([
                        dbc.Input(placeholder="Hva heter du?", id="navn"),
                        dbc.Label("Hva heter du?"),
                    ]),
                    xs=12, lg=6),
                dbc.Button("OK", id="ok-knapp", color="success"),
                dbc.Col(dcc.Markdown(children="Hei på deg!", id="hilsen"), xs=12, lg=6),
            ]),
        ]),
    ]
)

@app.callback(
    Output("hilsen", "children"),
    Input("ok-knapp", "n_clicks"),
    State("navn", "value"),
    prevent_initial_call=True,
)
def si_hei(_antall_klikk, navn):
    return f"Hei {navn}"


app.run_server(debug=True)
