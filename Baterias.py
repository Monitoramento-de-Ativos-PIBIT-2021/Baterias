#Plataforma de monitoramento de baterias
import dash
import dash_core_components as dcc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Monitoramento de Baterias! ", style={'text-align': 'center'}),
    dcc.Graph(id="graph"),
    # html.Button("Poderia fazer algo, mas não, só enfeite mesmo.", id='btn', n_clicks=0)
    dcc.Dropdown(id="slct_qualquercoisa",
                 options=[
                     {"label": "A"},
                     {"label": "B"},
                     {"label": "C"}],
                 multi=False,
                 # value=2015,
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),
])

df = pd.read_csv('https://raw.githubusercontent.com/Monitoramento-de-Ativos-PIBIT-2021/Baterias/main/csv_baterias_oneline.csv')


@app.callback(
    Output("graph", "figure"),
    [Input(component_id='slct_qualquercoisa', component_property='output_container')])

def baterry(none):
    fig = make_subplots(rows=2,
                        cols=2,
                        start_cell="bottom-left",
                        vertical_spacing=0.25,
                        horizontal_spacing=0.05,
                        subplot_titles=('Temperatura', 'Vai ser carga e desc', 'Tensão', 'Corrente'),
    )

    # tensao
    fig.add_trace(
        go.Bar(x=df['data'], y=df['tensao'], name="TENSÃO"),
        row=2, col=1)

    # corrente
    fig.add_trace(
        go.Bar(x=df['data'], y=df['corrente'], name="CORRENTE"),
        row=2, col=2)

    # temperatura
    fig.add_trace(
        go.Bar(x=df['data'], y=df['temperatura'], name="TEMPERATURA"),
        row=1, col=1)

    fig.add_trace(
        go.Scatter(x=[4000, 5000, 6000], y=[7000, 8000, 9000]),
        row=1, col=2)

    fig.update_layout(
        # width=1200,
        height=700,
        paper_bgcolor="LightSteelBlue",
    )

    return fig

app.run_server(debug=True)
