'''
user interface for
predictive model
(cleaned data developed by MFa)
(baseline predictive model
developed by DCohen 
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
        dcc.Markdown(
            """
        
            ## Predictions

            Your instructions: How to use your app to get new predictions.

            """
        ),
    ],
    md=4,
)


column2 = dbc.Col([
    dcc.Markdown('The Host has been with AirBnB: '),
    dcc.DatePickerRange(
        id='my-date-picker-range',
        min_date_allowed=date(2010, 1, 1),
        max_date_allowed=date(2030, 12, 31),
        initial_visible_month=date(2020, 1, 1),
        #end_date=date(2020, 1, 10)
    ),
    #dcc.

    html.Div(id='output-container-date-picker-range')
],
md=4,
)


column3 = dbc.Col([
    dcc.Markdown('City: '),
            html.Label(
                [
                    'Select a Single City or Multiple Cities',
                    dcc.Dropdown(
                        id="my-multi-dynamic-dropdown", multi=True,
                        options=[
                            {'label': 'New York City', 'value': 'NYC'},
                            {'label': 'Montréal', 'value': 'MTL'},
                            {'label': 'San Francisco', 'value': 'SF'}
                            {'label': 'Washington, DC', 'value': 'DC'},
                            {'label': 'Los Angeles', 'value': 'LA'},
                            {'label': 'Boston', 'value': 'Boston'}
                            ]
                        ),
                ] 
            ),
],
md=4,
)

# # other student's code for comparison
# column2 = dbc.Col(
#     [
#         dcc.Markdown('#### Strain Type'), 
#         dcc.Dropdown
#         (
#             id='ctype',
#             style= {
#             "color": "black",
#             },
#             options = [
#                 {'label': 'Indica', 'value': 'Indica'}, 
#                 {'label': 'Hybrid', 'value': 'Hybrid'}, 
#                 {'label': 'Sativa', 'value': 'Sativa'}, 
#             ], 
#             value = 'Hybrid', 
#             className='mb-5', 
#         ),
#         dcc.Markdown('#### Effect'), 
#         dcc.Dropdown
#         (
#             id='effects',
#             style= {
#             "color": "black",
#             },
#             options = [
#                 {'label': 'Happy', 'value': 'Happy'}, 
#                 {'label': 'Dry Mouth', 'value': 'Dry Mouth'}, 
#                 {'label': 'Relaxed', 'value': 'Relaxed'},
#                 {'label': 'Euphoric', 'value': 'Euphoric'}, 
#                 {'label': 'Uplifted', 'value': 'Uplifted'}, 
#                 {'label': 'Paranoid', 'value': 'Paranoid'},
#                 {'label': 'Sleepy', 'value': 'Sleepy'}, 
#                 {'label': 'Anxious', 'value': 'Anxious'}, 
#                 {'label': 'Creative', 'value': 'Creative'},
#                 {'label': 'Energetic', 'value': 'Energetic'}, 
#                 {'label': 'Hungry', 'value': 'Hungry'}, 
#                 {'label': 'Focused', 'value': 'Focused'},
#                 {'label': 'Tingly', 'value': 'Tingly'}, 
#                 {'label': 'Talkative', 'value': 'Talkative'}, 
#                 {'label': 'Horny', 'value': 'Horny'}, 
#             ], 
#             value = 'Happy', 
#             className='mb-5',
#             multi=True, 
#         ),
#         dcc.Markdown('#### Ailments'), 
#         dcc.Dropdown
#         (
#             id='ailment',
#             style= {
#             "color": "black",
#             },
#             options = [
#                 {'label': 'Stress', 'value': 'Stress'}, 
#                 {'label': 'Depression', 'value': 'Depression'}, 
#                 {'label': 'Pain', 'value': 'Pain'},
#                 {'label': 'Insomnia', 'value': 'Insomnia'}, 
#                 {'label': 'Lack Of Appetite', 'value': 'Lack Of Appetite'}, 
#                 {'label': 'Nausea', 'value': 'Nausea'},
#                 {'label': 'Inflammation', 'value': 'Inflammation'}, 
#                 {'label': 'Muscle Spasms', 'value': 'Muscle Spasms'}, 
#                 {'label': 'Seizures', 'value': 'Seizures'},
#             ], 
#             value = 'Stress', 
#             className='mb-5',
#             multi=True, 
#         ),
#         dcc.Markdown('#### Flavor'), 
#         dcc.Dropdown
#         (
#             id='flavor',
#             style= {
#             "color": "black",
#             },
#             options = [
#                 {'label': 'Earthy', 'value': 'Earthy'}, 
#                 {'label': 'Sweet', 'value': 'Sweet'}, 
#                 {'label': 'Citrus', 'value': 'Citrus'},
#                 {'label': 'Berry', 'value': 'Berry'}, 
#                 {'label': 'Pine', 'value': 'Pine'}, 
#                 {'label': 'Lemon', 'value': 'Lemon'},
#                 {'label': 'Skunk', 'value': 'Skunk'}, 
#                 {'label': 'Grape', 'value': 'Grape'}, 
#                 {'label': 'Blueberry', 'value': 'Blueberry'},
#                 {'label': 'Lime', 'value': 'Lime'}, 
#                 {'label': 'Orange', 'value': 'Orange'}, 
#                 {'label': 'Pepper', 'value': 'Pepper'},
#                 {'label': 'Ammonia', 'value': 'Ammonia'}, 
#                 {'label': 'Mango', 'value': 'Mango'}, 
#                 {'label': 'Pineapple', 'value': 'Pineapple'},
#                 {'label': 'Strawberry', 'value': 'Strawberry'}, 
#                 {'label': 'Lavender', 'value': 'Lavender'},
#                 {'label': 'Honey', 'value': 'Honey'}, 
#                 {'label': 'Coffee', 'value': 'Coffee'}, 
#                 {'label': 'Rose', 'value': 'Rose'},
#                 {'label': 'Vanilla', 'value': 'Vanilla'}, 
#                 {'label': 'Mint', 'value': 'Mint'}, 
#                 {'label': 'Apple', 'value': 'Apple'}, 
#             ], 
#             value = 'Earthy', 
#             className='mb-5',
#             multi=True, 
#         ),
#         # html.Button(id='Recommend', n_clicks=0, children='Submit'),
#         dbc.Button('Submit', id='Submit', color='primary'),
#         html.Div(id='output-state' ,children= 'recommender'),
#     ]
# ) 


@app.callback(
    dash.dependencies.Output('output-container-date-picker-range', 'children'),
    [dash.dependencies.Input('my-date-picker-range', 'start_date'),
    dash.dependencies.Input('my-date-picker-range', 'end_date')],
)
@app.callback(
    dash.dependencies.Output('my-multi-dynamic-dropdown', 'options'),
    [dash.dependencies.Input('my-dynamic-dropdown', 'search_value')],
    [dash.dependencies.State('my-multi-dynamic-dropdown', 'value')],
)

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


