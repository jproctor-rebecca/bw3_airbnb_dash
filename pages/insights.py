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
            To determine which model would perform best, we test several with our data prior to applying one in the application.
            We test the mathematical algorithms:
            Linear Regression, LassoCV, Decision Tree Regressor, XGBoost, and LightGBM Regressor (LGBMR). 
            For performance metrics, linear regression and LassoCV perform nearly equivalently, both returning MAEs between 56 and 58 for both training and validation data sets. 
            LightGBM is a gradient boosting framework that uses a tree-based algorithm. 
            The LGBMR is most similar to the popular ML algorithm that is XGBoost. 
            The biggest difference being that while XGBoost splits the tree nodes one level at a time, the LGBMR splits one node at a time. 
            LGBM also boasts more parameters, much faster speed, all with comparable accuracy metrics.

            As we look at feature importance we discover that some are more useful than others. 
            Feature importance shows the value of each feature as it relates to the optimal price for a given Airbnb property. Some of the new created features that were not so evident in the base model include features such as: strict and super_strict_60. This makes sense because it shows that the cancellation policy is very telling when it come to predicting an Airbnb price. A super strict 60 day policy on an Airbnb would certainly imply a higher demand than properties with a much more lenient cancellation policy.
            The plot aside shows the top 30% of the most influential features in each of these models’ fit, and their coefficients. 
            We see cancellation policy and room type as being very influential on the rental price. 
            This makes sense because it shows that the cancellation policy is very telling when it come to predicting an Airbnb price. 
            A super strict 60 day policy on an Airbnb would certainly imply a higher demand than properties with a much more lenient cancellation policy.

            
    
            
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