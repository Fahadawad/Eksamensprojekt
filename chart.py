# chart.py
import plotly.express as px
import dashboard_layout
import dashboard_callbacks

def create_bar_chart(data_frame, x_column, y_column, title, color_sequence, hover_data):
    fig = px.bar(
        data_frame,
        x=x_column,
        y=y_column,
        title=title,
        color_discrete_sequence=color_sequence,
        hover_data=hover_data
    )
    fig.update_layout(height=250, plot_bgcolor='#d4f2e7')
    return fig
