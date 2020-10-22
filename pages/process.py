'''
blog space for 
collaborative and 
model development process

RJProcess
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
            ## Methodology of the Team: 
            # 
            Initial exploration of our AirBnB dataset revealed 74,111 observations, with 28 features, and a target variable, log_price.

            The first steps were to prepare the dataset to fit an exploratory linear model. 

            Variables with > 5% missing data were removed.


            Variables with high cardinality or unusable variance were removed.

            Rare/ nontraditional property types were grouped together to reduce the cardinality of the property type variable.

            Log_price was exponentiated to return actual price. 


            Baseline MAE was 83.3.
            

            Linear Regression and LassoCV models were fit using Scikit-Learn. Categorical variables were one-hot encoded, missing values were imputed using the mean method, numerical variables were standardized. 

            """
        ),

    ],
)
# create footer

column2 = dbc.Col(
    [
         html.Img(src='assets/log_price_distribution.png', className='img-fluid')
    ],
)

    
layout = dbc.Row([column1, column2])