''' 
houses each team member's
link to personal GitHub io or
website or blog space

RJProctor
'''
# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## The Team: 
            Select a link to learn more about each of our 
            team members.    



            """

            html.Label(['Debbie Cohen ', html.A('link', href='/link-location')])
            html.Label(['Moe Fa ', html.A('link', href='/link-location')])
            html.Label(['Eduardo Padilla ', html.A('link', href='/link-location')])
            html.Label(['Jeannine Proctor ', html.A('link', href='/proctor-rebecca.github.io')])
        ),

    ],
)

layout = dbc.Row([column1])





