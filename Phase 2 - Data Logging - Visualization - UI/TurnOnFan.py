import dash
from dash import html, Output, Input
import RPi.GPIO as GPIO

# === GPIO Setup ===
RELAY_PIN = 17  # GPIO17 = physical pin 11
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)
GPIO.output(RELAY_PIN, GPIO.LOW)  # Start with relay OFF

# === Dash App ===
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Fan Control Dashboard"),
    
    html.Div([
        html.Button('Turn ON Fan', id='on-button', n_clicks=0),
        html.Button('Turn OFF Fan', id='off-button', n_clicks=0),
    ], style={'display': 'flex', 'gap': '20px'}),

    html.Div(id='status', style={'marginTop': '20px', 'fontSize': '24px'})
])

@app.callback(
    Output('status', 'children'),
    Input('on-button', 'n_clicks'),
    Input('off-button', 'n_clicks')
)
def control_fan(n_on, n_off):
    if n_on > n_off:
        GPIO.output(RELAY_PIN, GPIO.HIGH)  # Turn ON relay
        return "✅ Fan is ON"
    elif n_off >= n_on:
        GPIO.output(RELAY_PIN, GPIO.LOW)   # Turn OFF relay
        return "⛔ Fan is OFF"

# === Clean up GPIO on shutdown ===
if __name__ == '__main__':
    try:
        app.run(debug=True, host='0.0.0.0')
    finally:
        GPIO.cleanup()
