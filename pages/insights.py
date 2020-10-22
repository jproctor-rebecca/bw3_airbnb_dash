'''
blog space for insights 
on model predictions

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
            ## Insights from the Team: 
            # 
            For performance metrics, linear regression and LassoCV performed nearly equivalently, both returning MAEs between 56 and 58 for both training and validation data sets. 

            The plot below shows the top 30% of the most influential features in each of these models’ fit, and their coefficients. The linear regression model showed city, cancellation policy and room type as being the most influential on the rental price. The LassoCV model, after performing its own feature selection process, returned a room type of “entire apartment” as the most influential factor on the price, followed by the number of people accommodated and the number of bedrooms and bathrooms, and being in the city of San Francisco.
    
            """
        ),

    ],
)
# create footer

column2 = dbc.Col(
    [
         html.Img(src='assets/LCV_feature_importance.png', className='img-fluid')
    ],
)

    
layout = dbc.Row([column1, column2])