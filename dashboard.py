import pathlib
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

def hex_to_ascii(s):
    try:
        return bytearray.fromhex(s).decode()
    except ValueError:
        print('error')
        return None    
    
app_path = str(pathlib.Path(__file__).parent.resolve())

keepCol = ['Time', 'Data']
f = pd.read_csv("dataset.csv", index_col = False, header = 0)[keepCol]
df = pd.DataFrame({"Time": f['Time'], "Temperature": f['Data'].apply(hex_to_ascii)})

app = dash.Dash(__name__, url_base_pathname='/dashboard/')
server = app.server

theme = {
    'background': '#FFFFFF',
    'text': '#1A78C9'
}

def build_banner():
    return html.Div(
        className='col-sm-10 row banner',
        children=[
            html.Div(
                className='banner-text',
                children=[
                    html.H5('Temperature'),
                ],
            ),
        ],
    )

def build_graph():
    return dcc.Graph(
        id='basic-interactions',
        figure={
            'data': [
                {
                    'x': df['Time'][:50],
                    'y': df['Temperature'][:50],
                    'name': 'Temperature',
                    'marker': {'size': 20}
                }
            ],
            'layout': {
                'plot_bgcolor': theme['background'],
                'paper_bgcolor': theme['background'],
                'font': {
                    'color': theme['text']
                }
            }
        }
    )


app.layout = html.Div(
    className='big-app-container',
    children=[
        build_banner(),
        html.Div(
            className='app-container',
            children=[
                build_graph(),
            ]
        )
    ]
)
