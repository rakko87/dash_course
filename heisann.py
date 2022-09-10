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
                dbc.Col([
                    dbc.FormFloating([
                        dbc.Input(placeholder="Hva heter du?", id="navn"),
                        dbc.Label("Hva heter du?"),
                    ]),
                    dbc.FormFloating([
                        dbc.Input(placeholder="Hvor bor du?", id="bosted"),
                        dbc.Label("Hvor bor du?"),
                    ])
                ], xs=12, lg=6),
                dbc.Col(dbc.Button("OK", id="ok-knapp", color="success"), xs=12, lg=6),
                dbc.Col(dcc.Markdown(children="Hei på deg!", id="hilsen"), xs=12, lg=6),
                dbc.Col(dcc.Markdown(children="Hi there!", id="greeting"), xs=12, lg=6),
            ]),
        ]),
    ]
)

@app.callback(
    Output("hilsen", "children"),
    Output("greeting", "children"),
    Input("ok-knapp", "n_clicks"),
    State("navn", "value"),
    State("bosted", "value"),
    prevent_initial_call=True,
)
def si_hei(_antall_klikk, navn, sted):
    if sted:
        return f"Hei {navn} i {sted}", f"Hi {navn} in {sted}"
    else:
        return f"Hei {navn}", f"Hi {navn}"


@app.callback(
    Output("hilsen", "style"),
    Input("navn", "value")    
)
def fargelegg_hilsen(navn):
    if navn == "Geir":
        return {"color": "red"}
    return None


app.run_server(debug=True)
