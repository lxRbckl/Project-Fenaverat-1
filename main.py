# Project Fenaverat by Alex Arbuckle #


# import <
from backend.utility import application
from frontend.layout.frame import frameLayout

# >


# main <
if (__name__ == '__main__'):

    server = application.server
    application.layout = frameLayout
    application.run_server(debug = True)

# >
