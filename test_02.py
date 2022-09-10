import pathlib 
import time
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output

app = dash.Dash()

app.layout = html.Div([
    dbc.NavbarSimple(brand=f"Velkommen {time.ctime()}",color="dark",dark=True),
    dbc.Container([
       dbc.Row([
           dbc.Col(
               dbc.FormFloating([
                   dcc.Input(placeholder="Whats on you mind?", id="id_input_text"),
                    ]),
                    xs=12,lg=6),
            dbc.Col(
                dcc.Markdown(children="Type in something above!",id="id_output_text"),
                xs=12,lg=6),
            ]),
        ]),
    ])

@app.callback(
    Output("id_output_text", "children"),
    Input("id_input_text", "value"),
    prevent_initial_call=True,
    )
def si_hei(navn):
    return f"Hei {navn}"


app.run_server(debug=True)
