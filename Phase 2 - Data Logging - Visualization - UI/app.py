# === Import necessary libraries ===
import os                      # For file system operations
import glob                    # For pattern matching file paths
import time                    # For delays and timing
import csv                     # For writing to CSV files
import datetime                # To get current timestamps
import dash                    # Dash web framework
from dash import dcc, html     # Dash components
from dash.dependencies import Output, Input  # For callbacks
import plotly.graph_objs as go  # For plotting graphs

# === DS18B20 Temperature Sensor Setup ===
base_dir = '/sys/bus/w1/devices/'  # Location where sensor data appears in Pi OS
device_folder = glob.glob(base_dir + '28*')[0]  # Get the folder that starts with 28 (DS18B20 ID)
device_file = device_folder + '/w1_slave'       # File that contains the sensor reading

# === Read raw data from sensor file ===
def read_temp_raw():
    with open(device_file, 'r') as f:      # Open the file
        lines = f.readlines()              # Read all lines
    return lines

# === Parse and extract temperature in °C ===
def read_temp():
    lines = read_temp_raw()                # Read lines from sensor file
    while lines[0].strip()[-3:] != 'YES':  # First line must end in 'YES' (data valid)
        time.sleep(0.2)                    # Wait before retrying
        lines = read_temp_raw()            # Read again
    temp_pos = lines[1].find('t=')         # Look for temperature string in line 2
    if temp_pos != -1:
        temp_string = lines[1][temp_pos+2:]       # Extract temperature digits after 't='
        temp_c = float(temp_string) / 1000.0       # Convert from milli-degrees to °C
        return temp_c
    return None

# === Setup for CSV Logging ===
csv_file = 'temperature_log.csv'           # File name for logging data

# === Create the CSV file if it doesn't exist ===
if not os.path.isfile(csv_file):
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp', 'Temperature_C'])  # Header row

# === Create Dash App ===
app = dash.Dash(__name__)  # Initialize the Dash app

# === Store readings in memory for graph ===
times = []   # List of timestamps
temps = []   # List of temperatures

# === Define the layout of the Dash UI ===
app.layout = html.Div([
    html.H1("Temperature Monitor"),         # Page title
    dcc.Graph(id='live-graph', animate=True),  # Graph that updates
    dcc.Interval(                           # Timer that triggers graph updates
        id='graph-update',
        interval=2*1000,                    # Interval in milliseconds (2 seconds)
        n_intervals=0
    ),
    html.Div(id='current-temp'),            # Shows current temperature as text
    html.H3("Temperature Log File Location:"),
    html.P(os.path.abspath(csv_file))       # Show absolute path to log file
])

# === Update Graph & Text Every Interval ===
@app.callback(
    [Output('live-graph', 'figure'),        # Output: Updated graph
     Output('current-temp', 'children')],   # Output: Updated temperature text
    [Input('graph-update', 'n_intervals')]  # Input: Number of times interval fired
)
def update_graph_scatter(n):
    temperature = read_temp()               # Read the temperature
    current_time = datetime.datetime.now()  # Get current timestamp

    if temperature is not None:
        temps.append(temperature)           # Add to temperature list
        times.append(current_time)          # Add to time list

        # Log temperature to CSV
        with open(csv_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                current_time.strftime("%Y-%m-%d %H:%M:%S"), 
                f"{temperature:.2f}"
            ])
    else:
        # If failed reading, still update time with None temp
        temps.append(None)
        times.append(current_time)

    # Keep only the last 30 points for plotting
    times_trimmed = times[-30:]
    temps_trimmed = temps[-30:]

    # Create line+marker plot
    data = go.Scatter(
        x=times_trimmed,
        y=temps_trimmed,
        name='Temperature',
        mode='lines+markers'
    )

    # Create the graph layout
    figure = {
        'data': [data],
        'layout': go.Layout(
            xaxis=dict(range=[min(times_trimmed), max(times_trimmed)]),
            yaxis=dict(
                range=[
                    min(filter(None, temps_trimmed)) - 1,
                    max(filter(None, temps_trimmed)) + 1
                ]
            ),
            title='Live Temperature Data'
        )
    }

    # Format the text display
    temp_display = (
        f"Current Temperature: {temperature:.2f} °C" 
        if temperature is not None 
        else "Failed to read temperature"
    )

    return figure, temp_display

# === Run the Dash App on all IP addresses, port 8050 ===
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Accessible from any device on same network
