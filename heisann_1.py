import pathlib 

import dash
from dash import dcc, html

app = dash.Dash()

app.layout = html.Div(
    [
        dcc.Markdown(pathlib.Path("intro.md").read_text()),
    ]
)


app.run_server(debug=True)
