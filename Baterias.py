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
                     {"label": "A", "value": 'v_faseA'},
                     {"label": "B", "value": 'v_faseB'},
                     {"label": "C", "value": 'v_faseC'}],
                 multi=False,
                 placeholder="Futuramente vai fazer algo.",
                 # value=2015,
                 style={'width': "40%", 'text-align': 'start'}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),
])

df = pd.read_csv('https://raw.githubusercontent.com/Monitoramento-de-Ativos-PIBIT-2021/Baterias/main/csv_baterias_oneline.csv')


@app.callback(
    Output("graph", "figure"),
    [Input(component_id='slct_qualquercoisa', component_property='value')])

def baterry(none):
    fig = make_subplots(rows=2,
                        cols=2,
                        start_cell="bottom-left",
                        vertical_spacing=0.25,
                        horizontal_spacing=0.05,
                        subplot_titles=('Temperatura', 'Carga e Descarga', 'Tensão', 'Corrente'),
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
        go.Scatter(x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ], y=[13, 12.8, 12.5,12, 11.7, 11.1,11, 11.5, 11.9,12, 12.2, 12.3],name="CARGA E DESCARGA"),

        row=1, col=2)

    fig.update_layout(
        width=1100,
        height=700,
        paper_bgcolor="LightSteelBlue",
    )

    return fig

app.run_server(debug=True)
