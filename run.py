'''
locates and runs Python modules
without importing them in the
command line in the Python module
namespace rather than in the 
filesystem

RJProctor
'''


# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pages import index, predictions, insights, process, graphs


# Imports from this application
from app import app, server
from pages import index, predictions, insights, process

# Navbar docs: https://dash-bootstrap-components.opensource.faculty.ai/l/components/navbar
navbar = dbc.NavbarSimple(
    brand='What Price Is Right?',
    # creates routes to pages
    brand_href='/', 
    children=[
        # user interface for model
        dbc.NavItem(dcc.Link('Predictions', href='/predictions', className='nav-link')),
         # blog space - insights on model prediction 
        dbc.NavItem(dcc.Link('Insights', href='/insights', className='nav-link')),
        # blog space - insights on collaborative & model creation process
        dbc.NavItem(dcc.Link('Process', href='/process', className='nav-link')),
        # blog space - additional graphs on model prediction or collaborative process   
        dbc.NavItem(dcc.Link('Visualizations', href='/graphs', className='nav-link')),
        # blog space - housing links to each project team members GitHub.io/website/personal blog
        dbc.NavItem(dcc.Link('The Team', href='/aboutus', className='nav-link')),
    ],
    # doesn't move
    sticky='top',
    # AirBnB color scheme
    color='primary',
    # white/grey lettering on primary background
    light=False, 
    dark=True
)


# create footer
footer = dbc.Container(
    dbc.Row(
        dbc.Col(
            html.P(
                [
                    html.Span('DCohen', className='mr-2'), 
                    html.Span(' MFa', className='mr-2'), 
                    html.Span(' EPadilla', className='mr-2'), 
                    html.Span(' RJProctor', className='mr-2'), 
                    html.A(html.I(className='fas fa-envelope-square mr-1'), href='mailto:<jproctor.m.ed.tn@gmail>.com'), 
                    html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/<jproctor-rebecca>/<bw3_airbnb_dash>'), 
                   ], 
                className='lead'
            )
        )
    )
)

# create layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False), 
    navbar, 
    dbc.Container(id='page-content', className='mt-4'), 
    html.Hr(), 
    footer
])


# URL Routing for Multi-Page Apps
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return index.layout
    elif pathname == '/predictions':
        return predictions.layout
    elif pathname == '/insights':
        return insights.layout
    elif pathname == '/process':
        return process.layout
    elif pathname == '/pagename':
        return pagename.layout
    else:
        return dcc.Markdown('## Page not found')

# Run app server: https://dash.plot.ly/getting-started
if __name__ == '__main__':
    app.run_server(debug=True)