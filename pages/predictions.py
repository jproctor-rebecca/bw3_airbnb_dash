'''
user interface for
predictive model
(cleaned data developed by MFa
and DCohen)
(baseline predictive model
developed by DCohen, MFa 
and RJProctor)

RJProctor
'''

# Imports from 3rd party libraries
import dash
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
from datetime import date
import re


# Imports from this application
from app import app
from joblib import load

pipeline = load('assets/pipeline.joblib')


# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        
        html.Img(src='assets/AirBnB_1.jpg', className='img-fluid'),
        dcc.Markdown(
            '''
        
            ## Predictions

            Complete the Form on this page to predict the price of 
            an AirBnB or multiple types of AirBnBs.

            When you have selected all of your responses, select the 
            'Submit' button below to retriev your prediction(s).

            Have fun!

            '''
        ),
        # '''
        # submit button for prediction
        # '''
        [
        html.Button(id='prediction-content', n_clicks=0, children='Submit'),
        dbc.Button('Submit', id='Submit', color='primary'),
        html.Div(id='prediction-content', children= 'options'),
        ],
        
        [
            html.H2('Expected Rental Price: ', className='mb-5'), 
            html.Div(id='prediction-content', className='lead')
        ],

    ],
    md=4,
)


column2 = dbc.Col(
    [
    dcc.Markdown('## Numerical Features ', className='mb-5'),
    # '''
    # # of people the booking accommodates
    # 'accomodates'
    # 1-16

    # '''
    dcc.Markdown('Accomodates: '),
    dcc.Slider(
            id='accomodates', 
            min=1, 
            max=16, 
            step=1, 
            value=4, 
            marks={n: str(n) for n in range(1, 16, 4)}, 
            className='mb-5', 
        ), 

    # '''
    # # of bedrooms
    # 'bedrooms'
    # 0-10

    # '''
    dcc.Markdown('Bedrooms: '),
    dcc.Slider(
            id='bedrooms', 
            min=0, 
            max=10, 
            step=1, 
            value=3, 
            marks={n: str(n) for n in range(0, 10, 2)}, 
            className='mb-5', 
        ), 
    # '''
    # # of beds
    # 'beds'
    # 0-18

    # '''
    dcc.Markdown('Beds: '),
    dcc.Slider(
            id='beds', 
            min=0, 
            max=18, 
            step=1, 
            value=2, 
            marks={n: str(n) for n in range(0, 18, 3)}, 
            className='mb-5', 
        ), 
    # '''
    # # of bathrooms
    # 'bathrooms'
    # 0-8

    # '''
    dcc.Markdown('Bedrooms: '),
    dcc.Slider(
            id='bathrooms', 
            min=0, 
            max=8, 
            step=1, 
            value=2, 
            marks={n: str(n) for n in range(0, 8, 2)}, 
            className='mb-5', 
        ), 
    # '''
    # # of reviews for the host
    # 'number_of_reviews'
    # 0-605

    # '''
    dcc.Markdown('Host Reviews: '),
    dcc.Slider(
            id='reviews', 
            min=0, 
            max=605, 
            step=5, 
            value=75,
            marks={n: str(n) for n in range(0, 605, 25)}, 
            className='mb-5', 
        ), 
    ],
md=4,
)


column3 = dbc.Col(
    [
        dcc.Markdown('## Non-numerical Features ', className='mb-5'),
        # '''
        # city
        # array(['NYC', 'SF', 'DC', 'LA', 'Chicago', 'Boston'], dtype=object)

        # '''
        dcc.Markdown('City: '),
        html.Div([
            html.Label(
                [
                    'Select a Single City or Multiple Cities',
                    dcc.Dropdown(
                        id='city', multi=True,
                        options=[
                            {'label': 'New York City', 'value': 'NYC'},
                            {'label': 'Montréal', 'value': 'MTL'},
                            {'label': 'San Francisco', 'value': 'SF'},
                            {'label': 'Washington, DC', 'value': 'DC'},
                            {'label': 'Los Angeles', 'value': 'LA'},
                            {'label': 'Boston', 'value': 'Boston'}
                            ]
                        ),
                ] 
            )]
        ),
        # '''
        # property type
        # array(['Apartment', 'House', 'Condominium', 'Loft', 'Townhouse', 'Hostel',
        #    'Guest suite', 'Bed & Breakfast', 'Bungalow', 'Guesthouse', 'Dorm',
        #    'Other', 'Camper/RV', 'Villa', 'Boutique hotel', 'Timeshare',
        #    'In-law', 'Boat', 'Serviced apartment', 'Castle', 'Cabin',
        #    'Treehouse', 'Tipi', 'Vacation home', 'Tent', 'Hut',
        #    'Casa particular', 'Chalet', 'Yurt', 'Earth House',
        #    'Parking Space', 'Train', 'Cave', 'Lighthouse', 'Island'],

        # '''
        dcc.Markdown('Property Type: '),
        html.Div([
            html.Label(
                [
                    'Select a Single Property Type or Multiple Property Types',
                    dcc.Dropdown(
                        id='properties', multi=True,
                        options=[
                            {'label': 'Camper/RV', 'value': 'Camper/RV'},
                            {'label': 'Condominium', 'value': 'Condominium'},
                            {'label': 'Apartment', 'value': 'Apartment'},
                            {'label': 'Bungalow', 'value': 'Bungalow'},
                            {'label': 'Bed & Breakfast', 'value': 'Bed & Breakfast'},
                            {'label': 'House', 'value': 'House'},
                            {'label': 'Loft', 'value': 'Loft'},
                            {'label': 'Townhouse', 'value': 'Townhouse'},
                            {'label': 'Hostel', 'value': 'Hostel'},
                            {'label': 'Guest suite', 'value': 'Guest suite'},
                            {'label': 'Guesthouse', 'value': 'Guesthouse'},
                            {'label': 'Dorm', 'value': 'Dorm'},
                            {'label': 'Other', 'value': 'Other'},
                            {'label': 'Villa', 'value': 'Villa'},
                            {'label': 'Boutique hotel', 'value': 'Boutique hotel'},
                            {'label': 'Timeshare', 'value': 'Timeshare'},
                            {'label': 'In-law', 'value': 'In-law'},
                            {'label': 'Boat', 'value': 'Boat'},
                            {'label': 'Serviced apartment', 'value': 'Serviced apartment'},
                            {'label': 'Castle', 'value': 'Castle'},
                            {'label': 'Cabin', 'value': 'Cabin'},
                            {'label': 'Treehouse', 'value': 'Treehouse'},
                            {'label': 'Tipi', 'value': 'Tipi'},
                            {'label': 'Vacation home', 'value': 'Vacation home'},
                            {'label': 'Tent', 'value': 'Tent'},
                            {'label': 'Hut', 'value': 'Hut'},
                            {'label': 'Casa particular', 'value': 'Casa particular'},
                            {'label': 'Chalet', 'value': 'Chalet'},
                            {'label': 'Yurt', 'value': 'Yurt'},
                            {'label': 'Earth House', 'value': 'Earth House'},
                            {'label': 'Parking Space', 'value': 'Parking Space'},
                            {'label': 'Train', 'value': 'Train'},
                            {'label': 'Cave', 'value': 'Cave'},
                            {'label': 'Lighthouse', 'value': 'Lighthouse'},
                            {'label': 'Island', 'value': 'Island'},
                            ]
                        ),
                ] 
            )]
        ),
        # '''
        # room type
        # array(['Entire home/apt', 'Private room', 'Shared room'], dtype=object)
        
        # '''
        dcc.Markdown('Room Type: '),
            html.Div([
            html.Label(
                [
                    'Select a Single Room Type or Multiple Room Types',
                    dcc.Dropdown(
                        id='room', multi=True,
                        options=[
                            {'label': 'Entire Home or Apartment', 'value': 'Entire home/apt'},
                            {'label': 'Private Room', 'value': 'Private room'},
                            {'label': 'Shared Room', 'value': 'Shared room'}
                            ]
                        ),
                ] 
            )]
        ),
        # '''
        # cancellation policy
        # array(['strict', 'moderate', 'flexible', 'super_strict_30',
        #    'super_strict_60'], dtype=object)

        # '''
        dcc.Markdown('Cancellation Policy: '),
            html.Div([
            html.Label(
                [
                    'Select a Single Cancellation Policy or Multiple Cancellation Policies',
                    dcc.Dropdown(
                        id='cancellation', multi=True,
                        options=[
                            {'label': 'Flexible', 'value': 'flexible'},
                            {'label': 'Moderate', 'value': 'moderate'},
                            {'label': 'Strict', 'value': 'strict'},
                            {'label': 'Super Strict (30)', 'value': 'super_strict_30'},
                            {'label': 'Super Strict (60)', 'value': 'super_strict_60'},
                            ]
                        ),
                ],
            )]
        ),
        # '''
        # cleaning fee
        # array([ True, False])

        # '''
        
        dcc.Markdown('Cleaning Fee Included: '),
        html.Div([
            html.Label(
                [
                    'Select a True if the Cleaning Fee is Include in the Rental Price',
                    dcc.Dropdown(
                        id='cleaning', multi=False,
                        options=[
                            {'label': 'True', 'value': 'True'},
                            {'label': 'False', 'value': 'False'},
                            ]
                        ),
                ] 
            )])
    ],  
md=4,
)

@app.callback(
    dash.dependencies.Output('prediction-content', 'children'),
    # user input options require Input dependency setting
    [
        dash.dependencies.Input('accomodates', 'search_value'),
        dash.dependencies.Input('bedrooms', 'search_value'),
        dash.dependencies.Input('beds', 'search_value'),
        dash.dependencies.Input('bathrooms', 'search_value'),
        dash.dependencies.Input('reviews', 'search_value'),
        dash.dependencies.Input('city', 'search_value'),
        dash.dependencies.Input('properties', 'search_value'),
        dash.dependencies.Input('room', 'search_value'),
        dash.dependencies.Input('cancellation', 'search_value'),
        dash.dependencies.Input('cleaning', 'value'),
    ],
    # multi input options require additional State dependency setting
    [
        dash.dependencies.State('city', 'value'),
        dash.dependencies.State('properties', 'value'),
        dash.dependencies.State('room', 'value'),
        dash.dependencies.State('cancellation', 'value'),
    ],
)
def predict(accomodates, bedrooms, beds, bathrooms, reviews, city,
            properties, room, cancellation, cleaning, search_value):
    df = pd.DataFrame(
        columns=['accomodates','bedrooms','beds', 'bathrooms', 'reviews', 'city',
            'propertiess', 'room', 'cancellation', 'cleaning', 'search_value'], 
        data=[[accomodates, bedrooms, beds,bathrooms, reviews, city,
            properties, room, cancellation, cleaning, search_value]]
    )
    y_pred = pipeline.predict(df)[0]
    return f'{y_pred}'
  

def update_output(start_date, end_date):
    string_prefix = 'You have selected: '
    if start_date is not None:
        start_date_object = date.fromisoformat(start_date)
        start_date_string = start_date_object.strftime('%B %d, %Y')
        string_prefix = string_prefix + 'Start Date: ' + start_date_string + ' | '
    if end_date is not None:
        end_date_object = date.fromisoformat(end_date)
        end_date_string = end_date_object.strftime('%B %d, %Y')
        string_prefix = string_prefix + 'End Date: ' + end_date_string
    if len(string_prefix) == len('You have selected: '):
        return 'Select a date to see it displayed here'
    else:
        return string_prefix


def update_options(search_value):
    if not search_value:
        raise PreventUpdate
    return [o for o in options if search_value in o["label"]]


def update_multi_options(search_value, value):
    if not search_value:
        raise PreventUpdate
    # Make sure that the set values are in the option list, else they will disappear
    # from the shown select list, but still part of the `value`.
    return [
        o for o in options if search_value in o["label"] or o["value"] in (value or [])
    ]


layout = dbc.Row([column1, column2, column3])

# if __name__ == '__main__':
#     app.run_server(debug=True)


