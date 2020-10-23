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
            Initial exploration of our AirBnB dataset reveals 74,111 observations, with 28 features, and a target variable, log_price.

            The first step is to prepare the dataset to fit an exploratory linear model. 

            Variables with > 5% missing data are removed.


            Variables with high cardinality or unusable variance are removed.

            Rare/nontraditional property types are grouped together to reduce the cardinality of the property type variable.

            Log_price is exponentiated to return actual price. 


            

            Categorical variables were one-hot encoded, missing values are imputed using the mean method, numerical variables were standardized. 

            The AirBnB city data is then passed through each of the following algorithms:
            
            Linear Regression, LassoCV, Decision Tree Regressor, XGBmodels, and LightGBM Regressor (LGBMR), until we decide on LGBMR as the best model for this dataset.

            Natural language processing (NLP) is performed on the data before it is passed through the final model (LGBMR).
            
            Feature importance and model hyperparameter tuning is performed on the model, leaving us with ten most important features/parameters to pass through the application for the end user to consider when they 'predict' their price.   

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