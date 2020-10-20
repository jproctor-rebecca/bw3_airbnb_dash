'''
interactive vizualization
for main page

RJProctor
'''

# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## What Price Is Right?

            Using historical booking data from AirBnB, this AirBnB Optimal Price generator will allow a you to predict the trends for optimal pricing for a property based on variables such as location, time of year and other considerations. 
            
            You will be able to manage multiple properties at different locations and be able to make adjustments to your expectations for booking, as well as what you should be charging at your own AirBnB property.
            """
        ),
        dcc.Link(dbc.Button('For Right Price...', color='primary'), href='/predictions')
    ],
    md=4,
)

gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])