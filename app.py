from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objects as go

import dash 
from dash import dcc, html, Input, Output, State, no_update
import dash_bootstrap_components as dbc

import dataFile as getData
import GetICCValues as iccValues

external_stylesheets = [dbc.themes.BOOTSTRAP, "assets/segmentation-style.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server
app.title = "qEEGViz"

button_github = dbc.Button(
    "View on Github",
    id="gh-link",
    outline=True,
    href="https://github.com/akarshijain/EEGFeatureReliability/blob/main/app.py",
    style={"color": "white", "border": "solid 1px white"},
)

header = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        html.Img(
                            id="brain-logo",
                            src="https://www.neurensics.com/hubfs/eeg.png", 
                            style={"background":"transparent", "height":"80px",},
                        ),
                        md="auto",
                        align='center',
                    ),
                ]
            ),
            
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Div(
                                dash.html.Center(
                                    [
                                        html.Br(),
                                        html.H2("qEEGViz"),
                                        html.P("A Visualisation Tool for Quantitative EEG Features"),
                                    ],
                                    style={"color":"white"},
                                    id="app-title",
                                ),
                            )
                        ],
                        md=True,
                        align="center",
                    ),
                ],
            ),

            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.NavbarToggler(id="navbar-toggler"),
                            dbc.Collapse(
                                dbc.Nav(
                                    [
                                        dbc.NavItem(button_github),
                                        html.Img(src="https://cdn0.iconfinder.com/data/icons/octicons/1024/mark-github-512.png", style={"height":"45px", "padding":"7px", "filter":"invert(100%)", "position":"relative", "top":"-4px"}),
                                    ],
                                    navbar=True,
                                ),
                                id="navbar-collapse",
                                navbar=True,
                            ),
                        ],
                        align='center',
                        md=True,
                    ),
                ],
                align="center",
            ),
        ],
        fluid=True,
    ),
    dark=True,
    color="#0E2433",
    sticky="top",
)

files = dbc.Col(
    [
        dbc.Card(
            id="files-card",
            children=[
                dbc.CardHeader("Upload Files", style={"background-color": "#C8DFEA", "font-weight": "bold"}),
                dbc.CardBody(
                    dash.html.Center([
                        dcc.Upload(
                            id="file-upload",
                            children=html.Div(
                                [
                                    "Drag and Drop or ", html.A("Select a Folder")
                                ]
                            ),
                            style={
                                'width': "60%",
                                'height': '40px',
                                'lineHeight': '40px',
                                'borderWidth': '1px',
                                'borderStyle': 'dashed',
                                'borderRadius': '3px',
                                'textAlign': 'center',
                                'margin': '10px'
                            },
                            multiple=True
                        ),
                        html.Div(['Accepted format: .bin'], style={"font-size": "4px", "color": "grey"}),
                    ]) 
                )
            ],
            style={"width": "auto"},
        )
    ]
)

parameters = dbc.Col(
    [
        dbc.Card(
            id="parameters-card",
            children=[
                dbc.CardHeader("Select Parameters", style={"background-color": "#C8DFEA", "font-weight": "bold"}),
                dbc.CardBody(
                    #dash.html.Center(
                        [
                            dbc.Row(
                                [
                                    dbc.Col(
                                        html.Div(
                                            [
                                                html.P("Feature Name:"),
                                                dcc.Dropdown(
                                                    id='featureName',
                                                    options = [{'label':"Absolute Power Feature", 'value':'AbsolutePowerFeature'},
                                                                {'label':"Relative Power Feature", 'value':'RelativePowerFeature'}],
                                                    #value = 'AbsolutePowerFeature',
                                                    multi=False,
                                                ),
                                            ]
                                        ),
                                        width=4
                                    ),

                                    dbc.Col(
                                        html.Div(
                                            [
                                                html.P("Reference:"),
                                                dcc.Dropdown(
                                                    id='referenceName',
                                                    options = [{'label':"Default Reference", 'value':'defaultReference'},
                                                                {'label':"Average Reference", 'value':'avgReference'},
                                                                {'label':"Cz Reference", 'value':"czReference"}],
                                                    #value = 'defaultReference',
                                                    multi = False), 
                                            ]
                                        ),
                                        width=4
                                    ),

                                    dbc.Col(
                                        html.Div(
                                            [
                                                html.P("Epoch Length:"),
                                                dcc.Checklist(
                                                    id="epochList",
                                                    options=
                                                    [
                                                        {'label': ' 1 second ', 'value': 1},
                                                        {'label': ' 2 seconds ', 'value': 2},
                                                        {'label': ' 4 seconds ', 'value': 4},
                                                        {'label': ' 8 seconds ', 'value': 8},
                                                        {'label': ' 16 seconds ', 'value': 16},
                                                        {'label': ' 32 seconds ', 'value': 32},
                                                    ],
                                                    #value=[1, 2, 4],
                                                labelStyle={"width": '50%', 'display': "inline-block"}
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ]
                    #)
                )
            ],
            style={"width": "100%"},
        )
    ]
)

app.layout = (
    html.Div(
        [
            header,
            html.Br(),
            dbc.Container(
                [
                    dbc.Row(files),
                    html.Br(),
                    dbc.Row(parameters),
                    html.Br(),
                    dcc.RadioItems(
                        id='graph-choice',
                        options=[
                            {'label': ' Line Graph', 'value': 'one_dim'},
                            {'label': ' Topographical Map', 'value': 'two_dim'},
                            {'label': ' 3D Brain Viewer (Beta Version)', 'value': 'three_dim'},
                        ],
                        #value='one_dim',
                        #inline=True,
                        labelStyle={'display': 'block'}
                    ),
                    html.Br(),
                    dbc.Button(
                        "Create Graph",
                        id="submit-button",
                        style={"color": "black", "border": "solid 1px black", "background":'transparent'},
                    ),
                    html.Div(
                        [
                            dbc.Spinner(
                                dcc.Graph(id='eegFeatureVisual', style={'height': '80vh'}),
                                color="primary"
                            )
                        ]
                    ),
                ],
                fluid=True,
            ), 
        ]
    )
)

@app.callback(Output('eegFeatureVisual','figure'),
              Input('submit-button','n_clicks'),
              State('file-upload', 'filename'),
              State('featureName','value'),
              State('referenceName', 'value'),
              State('epochList', 'value')
            )

# @app.callback(
#     Output("navbar-collapse", "is_open"),
#     [Input("navbar-toggler", "n_clicks")],
#     [State("navbar-collapse", "is_open")],
# )
# def toggle_navbar_collapse(n, is_open):
#     if n:
#         return not is_open
#     return is_open


def update_graph(n, subjectList, featureName, referenceName, epochList):

    if n is None:
        return no_update

    featureList = getData.getFeatureList(featureName)
    numFeatures = len(featureList)
    numEpochs = len(epochList)

    iccValuesArr = iccValues.getICCValues(subjectList, featureName, referenceName, epochList)
    fig = make_subplots(rows=numFeatures, cols=numEpochs)

    for epoch in range(0, numEpochs):
        for feature in range(0, numFeatures):
            fig.add_trace(go.Scatter(y=iccValuesArr[epoch][feature]),
            row=feature+1, col=epoch+1)
            fig.update_layout(height = 1000, width = 1500)

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)