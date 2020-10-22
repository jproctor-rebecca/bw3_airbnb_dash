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
        ),

    ],
)
# create footer

column2 = dbc.Col(
    [
        dcc.Markdown(
            """
            **Debbie Cohen**

            https://github.com/dscohen75/dscohen75.github.io

            https://medium.com/@debbiecohen_22419
            
            **Moe Fa**

            ---
            
            **Eduardo Padilla**

            https://medium.com/@eprecendez

            ---

            **R. Jeannine Proctor**

            https://jproctor-rebecca.github.io/

            https://medium.com/@jproctor.m.ed.tn

            ---

            **Code Review Team Members:**

            Taylor Curran,
            Regina Dircio,
            Robert Giuffrie,
            Ryan Herr,
            Brendon Hoss,
            Anika Nacey,
            Tomas Phillips,
            Raymond Tan,
            and
            Rebecca Duke-Wiesenberg
            
            """
        ),
    ],
)
    
layout = dbc.Row([column1, column2])