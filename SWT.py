# SWT.py
import os
import pandas as pd
from dash import Dash
from dashboard_layout import create_layout
from dashboard_callbacks import initialize_callbacks
import mysql.connector

# Find hjemmekataloget for brugeren
fil = os.path.expanduser("~")

# Connection to MySQL database
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '',
    'database': 'SWT_sundhedstrivsel_DB'
}

# Establish the MySQL connection
connection = mysql.connector.connect(**db_config)

# Query to fetch data from the database
query_person = "SELECT * FROM person"
query_healthdata = "SELECT * FROM healthdata"
query_sleepdata = "SELECT * FROM sleepdata"
query_activitydata = "SELECT * FROM activitydata"
query_stressdata = "SELECT * FROM stressdata"

# Fetch data from the tables
df_person = pd.read_sql(query_person, connection)
df_healthdata = pd.read_sql(query_healthdata, connection)
df_sleepdata = pd.read_sql(query_sleepdata, connection)
df_activitydata = pd.read_sql(query_activitydata, connection)
df_stressdata = pd.read_sql(query_stressdata, connection)

# Close the database connection
connection.close()

# Initialize the Dash app
app = Dash(__name__)

# Initialize callbacks
initialize_callbacks(app, df_person, df_healthdata, df_sleepdata, df_activitydata, df_stressdata)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

