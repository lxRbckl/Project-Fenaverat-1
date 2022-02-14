# import <
from os import listdir
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from backend.utility import application, jsonLoad, jsonDump, realpath

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
    myProjectData = jsonLoad(file = '/frontend/data/myProject.json')
    path = '/'.join(realpath.split('/')[:-2]) + '/frontend/data/feed'
    feed = {t : jsonLoad(f'/frontend/data/feed/{t}') for t in listdir(path)}

    # >

    # build data <
    # filter data <
    project = {t : f for u in myProjectData.keys() for t, f in myProjectData[u]['project'].items()}
    project = {t : f for t, f in project.items() if (f['hide'] is False)}

    # >

    # build queue from data <
    # filter queue <
    queue = [title for user in myProjectData for title in myProjectData[user]['queue'][::-1]]
    queue = [title for title in queue if (title in project.keys())][::-1]

    # >

    # build board from queue <
    [board[c % len(board)].append(title) for c, title in enumerate(queue)]

    # >

    # output <
    return (

        [

            dbc.Col(

                children = [

                    myProjectFunction(title = title, projectData = project, feedData = feed)

                for title in col]

            )

        for col in board]

    )

    # >

# >


# function <
def myProjectFunction(title: str, projectData: dict, feedData: dict):
    '''  '''

    # output <
    return (

        # card <
        dbc.Card(

            style = myProjectStyle['cardStyle'],
            children = [

                # header <
                dbc.CardHeader(

                    style = myProjectStyle['cardChildrenStyle'],
                    children = cardHeaderFunction(title, projectData, feedData)

                ),

                # >

                html.Hr(style = myProjectStyle['cardHrStyle']),

                # body <
                dbc.CardBody(

                    style = myProjectStyle['cardChildrenStyle'],
                    children = cardBodyFunction(title, projectData, feedData)

                ),

                # >

                html.Hr(style = myProjectStyle['cardHrStyle']),

                # footer <
                dbc.CardFooter(

                    style = myProjectStyle['cardChildrenStyle'],
                    children = cardFooterFunction(title, projectData, feedData)

                )

                # >

            ]

        )

        # >

    )

    # >


def cardHeaderFunction(title: str, projectData: dict, feedData: dict):
    '''  '''

    # output <
    return (

        # title <
        # description <
        html.H4(title.replace('-', ' ')),
        html.Small(html.Small(projectData[title]['description']))

        # >

    )

    # >


def cardBodyFunction(title: str, projectData: dict, feedData: dict):
    '''  '''

    # if (empty) <
    try:

        # output <
        return [

            dbc.Badge(

                children = subject,
                color = myProjectStyle['bodyBadgeColor'],
                style = myProjectStyle['bodyBadgeStyle']

            )

        for subject in feedData[f'{title}.json'].keys()]

    # >

    # else (not empty) <
    except KeyError: return None

    # >


def cardFooterFunction(title: str, projectData: dict, feedData: dict):
    '''  '''

    # output <
    return (

        dbc.Row(

            justify = 'between',
            children = [

                # feed <
                dbc.Col(

                    width = 'auto',
                    children = [

                        dbc.CardLink(

                            href = f'/{title}',
                            style = myProjectStyle['footerCardLinkStyle'],
                            children = '{} ⇾'.format(title.replace('-', ' '))

                        )

                    ]

                ),

                # >

                # link <
                dbc.Col(

                    width = 'auto',
                    children = [

                        html.A(

                            href = projectData[title]['link'],
                            children = [

                                html.Img(

                                    src = myProjectStyle['linkImgSrc'],
                                    style = myProjectStyle['linkImgStyle']

                                )

                            ]

                        )

                    ]

                )

                # >

            ]

        )

    )

    # >

# >
