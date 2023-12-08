# dashboard_callbacks.py
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import chart
import dashboard_layout

def initialize_callbacks(app, df):
    # Define callback to update the graphs based on filters
    @app.callback(
        [Output('physical-activity-bar', 'figure'),
         Output('sleep-duration-bar', 'figure'),
         Output('stress-level-bar', 'figure')],
        [Input('occupation-filter', 'value'),
         Input('age-filter', 'value'),
         Input('gender-filter', 'value')]
    )
    def update_graphs(selected_occupations, selected_age_range, selected_genders):
        # Apply filters to the DataFrame
        filtered_df = df[
            (df['Occupation'].isin(selected_occupations)) &
            (df['Age'].between(selected_age_range[0], selected_age_range[1])) &
            (df['Gender'].isin(selected_genders))
        ]

        # Group by Occupation and calculate the mean of the numerical columns
        grouped_df = filtered_df.groupby('Occupation').agg({
            'Physical Activity Level': 'mean',
            'Sleep Duration': 'mean',
            'Stress Level': 'mean'
        }).reset_index()

        # Calculate the count of people for each occupation
        count_df = filtered_df['Occupation'].value_counts().reset_index()
        count_df.columns = ['Occupation', 'Count']

        # Merge the count_df with the grouped_df
        final_df = pd.merge(grouped_df, count_df, on='Occupation')

        # Create bar charts
        physical_activity_fig = px.bar(
            final_df,
            x='Occupation',
            y='Physical Activity Level',
            title='Physical Activity Level',
            color_discrete_sequence=['green'],
            hover_data=['Count']
        )
        physical_activity_fig.update_layout(height=250, plot_bgcolor='#d4f2e7')

        sleep_duration_fig = px.bar(
            final_df,
            x='Occupation',
            y='Sleep Duration',
            title='Sleep Duration',
            color_discrete_sequence=['blue'],
            hover_data=['Count']
        )
        sleep_duration_fig.update_layout(height=250, plot_bgcolor='#d4f2e7')

        stress_level_fig = px.bar(
            final_df,
            x='Occupation',
            y='Stress Level',
            title='Stress Level',
            color_discrete_sequence=['red'],
            hover_data=['Count']
        )
        stress_level_fig.update_layout(height=250, plot_bgcolor='#d4f2e7')

        return physical_activity_fig, sleep_duration_fig, stress_level_fig
