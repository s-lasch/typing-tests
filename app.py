import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
from jupyter_dash import JupyterDash
from dash import Dash, callback, html, dcc, Input, Output

import plots # from this repo


# collect data and create default plots
df = pd.read_csv("results.csv")

pie = plots.pie(df)
wpm = plots.box(df, 'wpm', 'wpm')
sun = plots.sun(df)

# create app
app = JupyterDash('Monkeytype Visualizations')
server = app.server

# create HTML layout
app.layout = html.Div(id='content', children=[
    html.Div(id='header', children=[
        dcc.Markdown('''
        # **Monkeytype Data Visualization**
        ### **Data:** 
        Obtained from https://monkeytype.com
        ''')
    ]),
    html.Hr(),
    dcc.Graph(id='pie', figure=pie),
    html.Div(id='boxplot', children=[
        dcc.Graph(id='box', figure=wpm),
        dcc.Dropdown(id='box-type',
                     options=[{'label':col, 'value':col} for col in df.columns[2:6]],
                     value='wpm'),
        html.Br(),
        html.Br()
    ]),
    dcc.Graph(id='sun-burst', figure=sun)
])

# callback function
@app.callback(
    Output('box', 'figure'),
    Input('box-type', 'value'))
def update_boxes(col):
    title = 'raw wpm' if col == 'rawWpm' else col
    title = 'accuracy' if col == 'acc' else title
    return plots.box(df, title, col)


# run the application
if __name__ == '__main__':
    app.run_server(debug=False)