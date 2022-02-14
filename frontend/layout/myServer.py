# import <
from dash import html, dcc
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from backend.utility import application, jsonLoad, jsonDump

# >


# global <


# >


# layout <
myServerLayout = (

    # board <
    dbc.Row(

        justify = 'center',
        id = 'myServerBoardRowId'

    )

    # >

)

# >


# callback <
@application.callback(Output('myServerBoardRowId', 'children'),
                      Input('myServerBoardRowId', 'children'))
def myServerCallabck():
    '''  '''

    # build server <
    # filter server <
    server = jsonLoad(file = '/frontend/data/myServer.json')
    server = {k : v for k, v in server.items() if (v['hide'] is True)}

    # >

    # build board from server <
    board = ([], [], [])
    [board[c % len(board)].append(node) for c, node in enumerate(server)]

    # >

    # output <
    return (

        [

            dbc.Col(

                children = [



                ]

            )

        for col in board]

    )

    # >

# >


# function <


# >
