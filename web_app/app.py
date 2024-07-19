import dash
from dash import dcc, html
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import joblib

# Load data
nasa_data = pd.read_csv('data/nasa_climate_data.csv')

# Load model
model = joblib.load('models/climate_change_prediction_model')

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Climate Change Impact Analysis'),

    dcc.Graph(
        id='temperature-trend',
        figure=px.line(nasa_data, x='Year', y='Temperature_Anomaly', title='Temperature Anomaly Over Years')
    ),

    html.Div([
        html.Label('Latitude:'),
        dcc.Input(id='latitude', type='number', value=0),
        html.Label('Longitude:'),
        dcc.Input(id='longitude', type='number', value=0),
        html.Label('Month:'),
        dcc.Input(id='month', type='number', value=1),
        html.Label('Year:'),
        dcc.Input(id='year', type='number', value=2023),
        html.Button('Predict', id='predict-button')
    ]),

    html.H2('Predicted Temperature:'),
    html.Div(id='predicted-temperature')
])

@app.callback(
    dash.dependencies.Output('predicted-temperature', 'children'),
    [dash.dependencies.Input('predict-button', 'n_clicks')],
    [dash.dependencies.State('latitude', 'value'),
     dash.dependencies.State('longitude', 'value'),
     dash.dependencies.State('month', 'value'),
     dash.dependencies.State('year', 'value')]
)
def predict_temperature(n_clicks, latitude, longitude, month, year):
    input_data = pd.DataFrame([[latitude, longitude, month, year]], columns=['latitude', 'longitude', 'month', 'year'])
    prediction = model.predict(input_data)
    return f'{prediction[0]}°C'

if __name__ == '__main__':
    app.run_server(debug=True)
