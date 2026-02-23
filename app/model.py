import random

# --- Threshold Configuration ---
# Centralized limits used for both evaluation and AI prompts
THRESHOLDS = {
    "temp": 40.0,       # °C
    "aqi": 150,         # Index
    "uv": 8.0,          # Index
    "noise": 85.0,      # dB
    "wind_speed": 20.0  # km/h
}

def generate_synthetic_data():
    """
    Generates the 6 required environmental parameters using random distribution.
    Used by the dashboard and the AI context builder.
    """
    return {
        "temp": round(random.uniform(0, 41), 2),
        "humidity": round(random.uniform(0, 90), 2),
        "wind_speed": round(random.uniform(1, 21), 2),
        "aqi": random.randint(0, 151),
        "uv": round(random.uniform(0, 9), 1),
        "noise": round(random.uniform(0, 86), 1)
    }

def evaluate_alerts(data):
    """
    Compares telemetry data against THRESHOLDS.
    Returns a comma-separated string of issues or None if safe.
    """
    alerts = []
    
    if data["aqi"] > THRESHOLDS["aqi"]: 
        alerts.append("High Pollution")
    if data["temp"] > THRESHOLDS["temp"]: 
        alerts.append("Extreme Heat")
    if data["uv"] > THRESHOLDS["uv"]: 
        alerts.append("High UV Radiation")
    if data["noise"] > THRESHOLDS["noise"]: 
        alerts.append("Noise Violation")
    if data["wind_speed"] > THRESHOLDS["wind_speed"]: 
        alerts.append("High Wind Speed")
    
    return ", ".join(alerts) if alerts else None