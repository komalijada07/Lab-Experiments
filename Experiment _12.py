import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html


def main():

    # 1. Sample Dataset (From Lab Manual)
    data = {
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
        'Sales':,
        'Profit':,
        'Region': ['East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West']
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    print("Dataset:")
    print(df)

    # 2. INTERACTIVE LINE GRAPH
    line_fig = px.line(
        df,
        x='Month',
        y='Sales',
        title='Monthly Sales Trend',
        markers=True
    )

    # 3. INTERACTIVE BAR GRAPH
    bar_fig = px.bar(
        df,
        x='Month',
        y='Profit',
        color='Region',
        title='Monthly Profit by Region'
    )

    # 4. INTERACTIVE SCATTER PLOT
    scatter_fig = px.scatter(
        df,
        x='Sales',
        y='Profit',
        color='Region',
        title='Sales vs Profit Scatter Plot'
    )

    # 5. DASHBOARD USING DASH
    app = Dash(__name__)

    app.layout = html.Div(children=[
        html.H1(
            children='Sales Dashboard',
            style={'textAlign': 'center'}
        ),

        dcc.Graph(
            id='line-chart',
            figure=line_fig
        ),

        dcc.Graph(
            id='bar-chart',
            figure=bar_fig
        ),

        dcc.Graph(
            id='scatter-chart',
            figure=scatter_fig
        )
    ])

    # Run Dashboard (Starts a local web server)
    app.run(debug=True)


if __name__ == "__main__":
    main()
  
