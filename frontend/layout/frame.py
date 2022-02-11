# import <
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from frontend.layout.aboutMe import aboutMeLayout
from frontend.layout.myServer import myServerLayout
from frontend.layout.myProject import myProjectLayout
from backend.utility import application, jsonLoad, jsonDump

# >


# global <
bodyData = jsonLoad(file = '/frontend/data/frame.json')
bodyStyle = jsonLoad(file = '/frontend/resource/frame.json')

# >


# frame <
bodyLayout = dbc.Container(

    fluid = True,
    style = bodyStyle['containerStyle'],
    children = [

        dcc.Location(id = 'frameLocationId'),

        # header <
        dbc.Row(

            id = 'headerRowId',
            justify = 'center',
            style = bodyStyle['rowStyle'],
            children = [

                html.Img(

                    src = bodyData['headerImgSrc'],
                    style = bodyStyle['headerImgStyle']

                )

            ]

        ),

        # >

        # menu <
        dbc.Row(

            id = 'menuRowId',
            justify = 'center',
            style = bodyStyle['rowStyle'],
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
                                    style = bodyStyle['menuImgStyle']

                                )

                            ]

                        )

                    for key, image in bodyData['menuButtonGroupValue'].items()]

                )

            ]

        ),

        # >

        # body <
        dbc.Row(

            id = 'bodyRowId',
            justify = 'center',
            style = bodyStyle['rowStyle']

        ),

        # >

        # footer <
        dbc.Row(

            id = 'footerRowId',
            justify = 'center',
            style = bodyStyle['rowStyle'],
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
                                    style = bodyStyle['footerImgStyle']

                                )

                            ]

                        )

                    ]

                )

                # >

            for link, image in bodyData['footerRowValue'].items()]

        )

        # >

    ]

)

# >


# callback <
@application.callback(Output('bodyRowId', 'children'),
                      Input('frameLocationId', 'pathname'))
def frameCallback(path: str):
    '''  '''

    # local <
    layoutDict = {

        '/aboutMe' : aboutMeLayout,
        '/myServer' : myServerLayout,
        '/myProject' : myProjectLayout

    }

    # >

    # output <
    return layoutDict[path]

    # >

# >
