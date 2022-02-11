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
    board = ([], [], [])
    aboutMeData = jsonLoad(file = '/frontend/data/aboutMe.json')
    myProjectData = jsonLoad(file = '/frontend/data/myProject.json')
    myProjectStyle = jsonLoad(file = '/frontend/resource/myProject.json')

    # >

    # build data <
    # filter data <
    data = {t : f for u in myProjectData.keys() for t, f in myProjectData[u]['project'].items()}
    data = {t : f for t, f in data.items() if (f['hide'] is False)}

    # >

    # build queue from data <
    # filter queue <
    queue = [title for user in myProjectData for title in myProjectData[user]['queue']]
    queue = [title for title in queue if (title in data.keys())]

    # >

    # build board from queue <
    [board[c % len(board)].append(title) for c, title in enumerate(queue)]

    # >

    # output <
    return (

        # iterate (col) <
        [

            # iterate (title) <
            dbc.Col(

                children = [

                    myProjectFunction(title = title, data = data)

                for title in col]

            )

            # >

        for col in board]

        # >

    )

    # >

# >


# function <
def myProjectFunction(title: str, data: dict):
    '''  '''

    # output <
    return (

        # card <
        dbc.Card(

            style = myProjectStyle['cardStyle'],
            children = [

                dbc.CardHeader(

                    html.H4(title.replace('-', ' '))

                )

            ]

        )

        # >

    )

    # >

# >
