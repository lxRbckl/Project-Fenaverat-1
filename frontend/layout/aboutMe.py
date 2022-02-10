# import <
import dash_daq as daq
from dash import html, dcc
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from backend.utility import application, jsonLoad, jsonDump

# >


# global <
aboutMeData = jsonLoad(file = '/frontend/data/aboutMe.json')
aboutMeStyle = jsonLoad(file = '/frontend/resource/aboutMe.json')

# >


# layout <
aboutMeLayout = (

    dbc.Row(

        children = [

            # image <
            dbc.Col(

                width = 'auto',
                children = [

                    dbc.Card(

                        style = aboutMeStyle['imageCardStyle'],
                        children = [

                            dbc.CardImg(

                                src = aboutMeData['imageCardImgSrc'],
                                style = aboutMeStyle['imageCardImgStyle']

                            )

                        ]

                    ),

                ]

            ),

            # >

            # biography <
            dbc.Col(

                children = [

                    dbc.Card(

                        style = aboutMeStyle['biographyCardStyle'],
                        children = [

                            dbc.CardBody(

                                children = [

                                    # header <
                                    # body <
                                    html.H4(aboutMeData['biographyH4Children']),
                                    html.P(aboutMeData['biographyPChildren'])

                                    # >

                                ]

                            )

                        ]

                    )

                ]

            )

            # >

        ]

    ),

    dbc.Row(

        # graph <
        children = [

            # update <
            dcc.Interval(

                n_intervals = 0,
                id = 'updateIntervalId',
                interval = (3600 * 1000)

            ),

            # >

            # language <
            dbc.Col(

                style = aboutMeStyle['graphColStyle'],
                children = [

                    dbc.Card(

                        style = aboutMeStyle['graphCardStyle'],
                        children = [

                            # header <
                            # body <
                            dbc.CardBody(

                                style = aboutMeStyle['graphHeaderStyle'],
                                children = [

                                    # title <
                                    # status <
                                    html.H6('Languages'),
                                    daq.Indicator(

                                        color = aboutMeStyle['statusIndicatorColor'],
                                        size = 10

                                    ),

                                    # >

                                    # graph <
                                    dcc.Graph(id = 'languageGraphId'),

                                    # >

                                    # tooltip <
                                    dbc.Tooltip(

                                        children = 'Updated Hourly',
                                        target = 'languageGraphId',
                                        placement = 'top'

                                    )

                                    # >

                                ]

                            ),

                            # >

                        ]

                    )

                ],

            # >

            ),

            # >

            # topic <
            dbc.Col(

                style = aboutMeStyle['graphColStyle'],
                children = [

                    dbc.Card(

                        style = aboutMeStyle['graphCardStyle'],
                        children = [

                            dbc.CardBody(

                                style = aboutMeStyle['graphHeaderStyle'],
                                children = [

                                    # title <
                                    # status <
                                    html.H6('Topics'),
                                    daq.Indicator(

                                        color = aboutMeStyle['statusIndicatorColor'],
                                        size = 10

                                    ),

                                    # >

                                    # graph <
                                    dcc.Graph(id = 'topicGraphId'),

                                    # >

                                    # tooltip <
                                    dbc.Tooltip(

                                        children = 'Updated Hourly',
                                        target = 'topicGraphId',
                                        placement = 'top'

                                    )

                                    # >
                                ]

                            )

                        ]

                    )

                ]

            ),

            # >

        ]

        # >

    )

)

# >


# callback <
@application.callback(Output('topicGraphId', 'figure'),
                      Output('languageGraphId', 'figure'),
                      Input('updateIntervalId', 'n_intervals'))
def aboutMeCallback(*args):
    '''  '''

    # global <
    global aboutMeData
    aboutMeData = jsonLoad(file = '/frontend/data/aboutMe.json')

    # >

    # get topic and language <
    # iterate (user) <
    topicList = aboutMeData['bonusTopic']
    languageList = aboutMeData['bonusLanguage']
    for user in aboutMeData['users']:

        topicList.extend(aboutMeData[user]['topic'])
        languageList.extend(aboutMeData[user]['language'])

    # >

    # get topic and language figure <
    topicGraph = aboutMeFunction(topicList)
    languageGraph = aboutMeFunction(languageList)

    # >

    # output <
    return (topicGraph, languageGraph)

    # >

# >


# function <
def aboutMeFunction(*args):
    '''  '''

    # iterate (arg) <
    dictVariable = {}
    for i in args[0]:

        # if (element in dict then increment) <
        # else (element not in dict then initialize) <
        if (i in dictVariable.keys()): dictVariable[i] += 1
        else: dictVariable[i] = 1

        # >

    # >

    # figure <
    figure = {

        'data' : [

            go.Pie(

                hole = 0.4,
                textinfo = 'label',
                hoverinfo = 'none',
                showlegend = False,
                textposition = 'inside',
                insidetextorientation = 'radial',
                labels = list(dictVariable.keys()),
                values = list(dictVariable.values()),
                marker = {

                    'colors' : [aboutMeStyle['figureColors'] for i in dictVariable.keys()],
                    'line' : aboutMeStyle['figureLine']

                }

            )

        ],

        'layout' : aboutMeStyle['figureLayout']

    }

    # >

    # output <
    return figure

    # >

# >
