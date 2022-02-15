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

# >


# function <
def feedFunction(title: str, data: dict):
    '''  '''

    # output <
    return [

        html.H1(subject)

    for subject, information in data.items()]

    # >

# >
