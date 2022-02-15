# import <
from dash import html, dcc
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from backend.utility import application, jsonLoad, jsonDump

# >


# global <
myServerData = jsonLoad(file = '/frontend/data/myServer.json')
myServerStyle = jsonLoad(file = '/frontend/resource/myServer.json')

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
def myServerCallabck(*args):
    '''  '''

    # build server <
    # filter server <
    server = jsonLoad(file = '/frontend/data/myServer.json')
    server = {k : v for k, v in server.items() if (v['hide'] is False)}

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

                    myServerFunction(node = node, serverData = server)

                for node in col]

            )

        for col in board]

    )

    # >

# >


# function <
def myServerFunction(node: str, serverData: dict):
    '''  '''

    # output <
    return (

        # card <
        dbc.Card(

            style = myServerStyle['cardStyle'],
            children = [

                # header <
                dbc.CardHeader(

                    style = myServerStyle['cardChildrenStyle'],
                    children = cardHeaderFunction(node, serverData)

                ),

                # >

                # body <
                dbc.CardBody(

                    style = myServerStyle['cardChildrenStyle'],
                    children = cardBodyFunction(node, serverData)

                )

                # >

            ]

        )

        # >

    )

    # >


def cardHeaderFunction(node: str, serverData: dict):
    '''  '''

    # output <
    return (

        html.H4(node)

    )

    # >


def cardBodyFunction(node: str, serverData: dict):
    '''  '''

    # output <
    return (



    )

    # >

# >
