import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Initialize the Dash app
app = dash.Dash(__name__)
server = app.server
# Sample data
df = px.data.gapminder()

# Layout of the app
app.layout = html.Div([
    html.H1("Simple Dash App with Filter"),
    
    # Dropdown for filtering the data
    dcc.Dropdown(
        id='continent-filter',
        options=[{'label': continent, 'value': continent} for continent in df['continent'].unique()],
        value='Asia',  # Default value
        clearable=False,
        style={'width': '50%'}
    ),
    
    # Graph to show the data
    dcc.Graph(id='scatter-plot')
])

# Callback to update the graph based on the dropdown filter
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('continent-filter', 'value')]
)
def update_graph(selected_continent):
    # Filter data based on selected continent
    filtered_df = df[df['continent'] == selected_continent]
    
    # Create scatter plot
    fig = px.scatter(filtered_df, x='gdpPercap', y='lifeExp', size='pop', color='country',
                     hover_name='country', log_x=True, size_max=60,
                     title=f'GDP vs Life Expectancy ({selected_continent})')

    return fig

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
