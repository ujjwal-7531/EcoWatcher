import sqlite3
from datetime import datetime

DB_NAME = "data.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    # Ensure featured exists (1 for true, 0 for false)
    c.execute('''CREATE TABLE IF NOT EXISTS zones 
                 (id INTEGER PRIMARY KEY, name TEXT, lat REAL, lon REAL, featured INTEGER DEFAULT 0)''')
    c.execute('''CREATE TABLE IF NOT EXISTS alerts 
                 (id INTEGER PRIMARY KEY, timestamp TEXT, zone_name TEXT, 
                  temp REAL, humidity REAL, wind REAL, aqi INTEGER, uv REAL, noise REAL, reason TEXT)''')
    conn.commit()
    conn.close()
    
# app/database.py

def seed_zones():
    # 1. Use your existing get_zones function to check if empty
    existing_zones = get_zones() 
    
    if not existing_zones:
        default_zones = [
            {"name": "Mumbai Central", "lat": 18.96, "lon": 72.82},
            {"name": "Delhi Tech Zone", "lat": 28.61, "lon": 77.20},
            {"name": "Bangalore SEZ", "lat": 12.97, "lon": 77.59},
            {"name": "Kolkata Hub", "lat": 22.57, "lon": 88.36},
            {"name": "Chennai Port", "lat": 13.08, "lon": 80.27},
            {"name": "Hyderabad Hitech", "lat": 17.38, "lon": 78.48},
            {"name": "Pune Smart City", "lat": 18.52, "lon": 73.85},
            {"name": "Ahmedabad West", "lat": 23.02, "lon": 72.57},
            {"name": "Jaipur North", "lat": 26.91, "lon": 75.78},
            {"name": "Surat Industrial", "lat": 21.17, "lon": 72.83}
        ]
        
        for z in default_zones:
            # Use your existing add_zone function
            add_zone(z['name'], z['lat'], z['lon'])
            
        print(f"✅ Successfully seeded {len(default_zones)} default zones.")
    else:
        print("ℹ️ Database already contains data. Skipping seed.")

# Add this function to toggle the pin status
def toggle_zone_featured(zone_id):
    conn = sqlite3.connect(DB_NAME)
    # Get current state of this zone
    current = conn.execute("SELECT featured FROM zones WHERE id = ?", (zone_id,)).fetchone()[0]
    
    if current == 0: # Trying to PIN
        count = conn.execute("SELECT COUNT(*) FROM zones WHERE featured = 1").fetchone()[0]
        if count >= 5:
            conn.close()
            return False # Limit reached
            
    conn.execute("UPDATE zones SET featured = 1 - featured WHERE id = ?", (zone_id,))
    conn.commit()
    conn.close()
    return True

def add_zone(name, lat, lon):
    conn = sqlite3.connect(DB_NAME)
    # Check how many are currently pinned
    count = conn.execute("SELECT COUNT(*) FROM zones WHERE featured = 1").fetchone()[0]
    # If less than 5, this new one is automatically pinned
    is_featured = 1 if count < 5 else 0
    
    conn.execute("INSERT INTO zones (name, lat, lon, featured) VALUES (?, ?, ?, ?)", 
                 (name, lat, lon, is_featured))
    conn.commit()
    conn.close()

def log_alert(zone_name, m, reason):
    conn = sqlite3.connect(DB_NAME)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Changed m['wind'] to m['wind_speed'] to match main.py
    conn.execute("INSERT INTO alerts VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
              (timestamp, zone_name, m['temp'], m['humidity'], 
               m['wind_speed'], m['aqi'], m['uv'], m['noise'], reason))
    conn.commit()
    conn.close()
    
def get_zones():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    zones = conn.execute("SELECT * FROM zones").fetchall()
    conn.close()
    return [dict(z) for z in zones]

def get_recent_alerts(n):
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    res = conn.execute("SELECT * FROM alerts ORDER BY id DESC LIMIT ?", (n,)).fetchall()
    conn.close()
    return [dict(r) for r in res]

def remove_zone(zone_id):
    conn = sqlite3.connect(DB_NAME)
    conn.execute("DELETE FROM zones WHERE id = ?", (zone_id,))
    conn.commit()
    conn.close()