import pathlib 

import dash
from dash import dcc, html, Input, Output

app = dash.Dash()

app.layout = html.Div(
    [
        dcc.Markdown(pathlib.Path("intro.md").read_text()),
        dcc.Input(placeholder="Hva heter du?", id="navn"),
        dcc.Markdown("Hei på deg!", id="hilsen")
    ]
)


@app.callback(
    Output("hilsen", "children"),
    Input("navn", "value"),
    )
def si_hei(navn):
    return f"Hei {navn}"


app.run_server(debug=True)
