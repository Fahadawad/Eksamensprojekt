# SWT.py
import os
import pandas as pd
from dash import Dash
from dashboard_layout import create_layout
from dashboard_callbacks import initialize_callbacks

# Find hjemmekataloget for brugeren
fil = os.path.expanduser("~")

# Sammensæt stien til filen på skrivebordet
sti_til_fil = os.path.join(fil, "Desktop", "data i excel.xlsx")

# Indlæs data fra den lokale fil
df = pd.read_excel(sti_til_fil)

# Initialize the Dash app
app = Dash(__name__)

# Set layout
app.layout = create_layout(df)

# Initialize callbacks
initialize_callbacks(app, df)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
