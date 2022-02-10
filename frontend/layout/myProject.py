# import <
from dash import html, dcc
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from backend.utility import application, jsonLoad, jsonDump

# >


# global <
aboutMeData = jsonLoad(file = '/frontend/data/aboutMe.json')
myProjectData = jsonLoad(file = '/frontend/data/myProject.json')
myProjectStyle = jsonLoad(file = '/frontend/resource/myProject.json')

# >


# layout <
myProjectLayout = (

    # board <
    dbc.Row(

        id = 'boardRowId',
        justify = 'center'

    )

    # >

)

# >


# callback <
@application.callback(Output('boardRowId', 'children'),
                      Input('boardRowId', 'children'))
def myProjectCallback(*args):
    '''  '''

    # local <
    queue, board = [], ([], [], [])
    aboutMeData = jsonLoad(file = '/frontend/data/aboutMe.json')
    myProjectData = jsonLoad(file = '/frontend/data/myProject.json')
    style = jsonLoad(file = '/frontend/resource/myProject.json')

    # >

    # build queue from data <
    # build board from queue <
    [queue.extend(myProjectData[user]['queue']) for user in aboutMeData['users']]
    [board[c % len(board)].append(title) for c, title in enumerate(queue)]

    # >

    # output <
    return (

        # iterate (col) <
        [

            # build col <
            dbc.Col(

                align = 'center',
                children = [

                    myProjectFunction(title = title, data = myProjectData)

                for title in col]

            )

            # >

        for col in board]

        # >

    )

    # >

# >


# function <
def myProjectFunction(title, data):
    '''  '''

    return (

        html.H1(title)

    )

# >
