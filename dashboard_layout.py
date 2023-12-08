# dashboard_layout.py
from dash import html, dcc
import chart
import dashboard_callbacks

def create_layout(df):
    # Define the app layout
    layout = html.Div([
        html.Div([
            html.Label("Filter By Occupation"),
            dcc.Dropdown(
                id='occupation-filter',
                options=[{'label': occupation, 'value': occupation} for occupation in df['Occupation'].unique()],
                multi=True,
                value=df['Occupation'].unique()
            ),
            html.Div([
                html.Label("Filter By Age"),
                dcc.RangeSlider(
                    id='age-filter',
                    min=27,
                    max=60,
                    step=1,
                    marks={i: str(i) for i in range(27, 60, 2)},
                    value=[27, 60]
                ),
            ], style={'width': '100%', 'display': 'inline-block'}),
            html.Label("Filter By Gender"),
            dcc.Dropdown(
                id='gender-filter',
                options=[{'label': gender, 'value': gender} for gender in df['Gender'].unique()],
                multi=True,
                value=df['Gender'].unique()
            ),
        ], style={'width': '25%', 'float': 'left'}),

        html.Div([
            dcc.Graph(id='physical-activity-bar'),
            dcc.Graph(id='sleep-duration-bar'),
            dcc.Graph(id='stress-level-bar'),
        ], style={'width': '75%', 'float': 'right'}),
    ], style={'backgroundColor': '#d4f2e7', 'height': '100vh'})

    return layout
