# Project Fenaverat by Alex Arbuckle #


# import <
from backend.utility import application
from frontend.layout.frame import bodyLayout

# >
from backend.utility import realpath

# main <
if (__name__ == '__main__'):

    server = application.server
    application.layout = bodyLayout
    application.run_server(debug = True)

# >
