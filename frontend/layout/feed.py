# import <
import dash_daq as daq
from dash import html, dcc
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from backend.utility import application, jsonLoad, jsonDump

# >


# global <
feedStyle = jsonLoad(file = '/frontend/resource/feed.json')
myProjectStyle = jsonLoad(file = '/frontend/resource/myProject.json')

# >


# function <
def feedFunction(title: str, data: dict):
    '''  '''

    # local <
    feed = []

    # >

    # build feed <
    for subject, article in data.items():

        # if (header or image) <
        # else (anything) <
        if (subject in myProjectStyle['subjectFilter']): feed.append(imageFunction(article))
        else: feed.append(markdownFunction(subject, article))

        # >

    # >

    # output <
    return (

        dbc.Card(

            style = feedStyle['cardStyle'],
            children = [post for post in feed]

        )

    )

    # >


def imageFunction(article: str):
    '''  '''

    # output <
    return (

        dbc.CardImg(

            src = article,
            style = feedStyle['cardImgStyle']

        )

    )

    # >


def markdownFunction(subject: str, article: list):
    '''  '''

    # output <
    return (

        dbc.CardBody(

            style = feedStyle['cardBodyStyle'],
            children = [

                # subject <
                # article <
                html.H3(subject),
                html.Small(dcc.Markdown([i for i in article]))

                # >

            ]

        )

    )

    # >

# >
