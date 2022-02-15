# import <
from os import listdir
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from frontend.layout.feed import feedFunction
from frontend.layout.aboutMe import aboutMeLayout
from frontend.layout.myServer import myServerLayout
from frontend.layout.myProject import myProjectLayout
from backend.utility import application, jsonLoad, realpath

# >


# global <

frameData = jsonLoad(file ='/frontend/data/frame.json')
frameStyle = jsonLoad(file ='/frontend/resource/frame.json')

# >


# frame <
frameLayout = dbc.Container(

    fluid = True,
    style = frameStyle['containerStyle'],
    children = [

        dcc.Location(id = 'frameLocationId'),

        # header <
        dbc.Row(

            id = 'headerRowId',
            justify = 'center',
            style = frameStyle['rowStyle'],
            children = [

                html.Img(

                    src = frameData['headerImgSrc'],
                    style = frameStyle['headerImgStyle']

                )

            ]

        ),

        # >

        # menu <
        dbc.Row(

            id = 'menuRowId',
            justify = 'center',
            style = frameStyle['rowStyle'],
            children = [

                dbc.ButtonGroup(

                    children = [

                        dbc.Button(

                            id = key,
                            n_clicks = 0,
                            outline = True,
                            href = key.replace('ButtonId', ''),
                            children = [

                                html.Img(

                                    src = image,
                                    style = frameStyle['menuImgStyle']

                                )

                            ]

                        )

                    for key, image in frameData['menuButtonGroupValue'].items()]

                )

            ]

        ),

        # >

        # body <
        dbc.Row(

            id = 'bodyRowId',
            justify = 'center',
            style = frameStyle['bodyRowStyle']

        ),

        # >

        # footer <
        dbc.Row(

            id = 'footerRowId',
            justify = 'center',
            style = frameStyle['rowStyle'],
            children = [

                # image <
                dbc.Col(

                    width = 'auto',
                    children = [

                        html.A(

                            href = link,
                            children = [

                                html.Img(

                                    src = image,
                                    style = frameStyle['footerImgStyle']

                                )

                            ]

                        )

                    ]

                )

                # >

            for link, image in frameData['footerRowValue'].items()]

        )

        # >

    ]

)

# >


# callback <
@application.callback(Output('bodyRowId', 'style'),
                      Output('bodyRowId', 'children'),
                      Input('frameLocationId', 'pathname'))
def frameCallback(pathname: str):
    '''  '''

    # local <
    path = '/'.join(realpath.split('/')[:-2]) + '/frontend/data/feed'
    feed = {t : jsonLoad(f'/frontend/data/feed/{t}') for t in listdir(path)}
    layoutDict = {

        '/' : (frameStyle['rowStyle'], aboutMeLayout),
        '/aboutMe' : (frameStyle['rowStyle'], aboutMeLayout),
        '/myServer' : (frameStyle['bodyRowStyle'], myServerLayout),
        '/myProject' : (frameStyle['bodyRowStyle'], myProjectLayout)

    }

    # >

    # if (page) <
    # elif (feed) <
    if (pathname in layoutDict.keys()): return layoutDict[pathname]
    elif ((pathname.replace('/', '') + '.json') in feed.keys()):

        # output <
        return (

            frameStyle['feedRowStyle'],
            feedFunction(

                title = pathname.replace('/', ''),
                data = feed[pathname.replace('/', '') + '.json']

            )

        )

        # >

    # >

# >
