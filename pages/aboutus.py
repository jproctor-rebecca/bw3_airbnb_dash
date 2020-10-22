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
    [   html.Img(src='assets/lambda.pnd', className='img-fluid')
        [Graphic Courtesy of](https://lambdaschool.com/)
        dcc.Markdown(
            """
        
            ## The Team: 
            Select a link to learn more about each of our 
            team members.    



            """
# create footer
column1 = dbc.Div(
    [
            dcc.Markdown(
            '''
            ##Debbie Cohen
            https://github.com/dscohen75/dscohen75.github.io
            https://medium.com/@debbiecohen_22419
            
            ##Moe Fa
            

            ##Eduardo Padilla
            https://medium.com/@eprecendez

            ##R. Jeannine Proctor
            https://jproctor-rebecca.github.io/
            https://medium.com/@jproctor.m.ed.tn


            ##Code Review Team Members:
            Taylor Curran
            Regina Dircio
            Robert Guffrie
            Ryan Herr
            Brendon Hoss
            Anika Nacey
            Thomas Phillips
            Raymond Tan
            Rebecca Duke-Wiesenberg
            

            
            
            '''
            , 
            className='lead',
            )
        ]
    )
    




layout = dbc.Row([column1])





