# 🌍 EcoWatcher: Real-Time Environmental Monitoring Console

> **🌐 Live Demo:** [View EcoWatcher Live on Render](https://hack-for-green-bharat-3.onrender.com)

EcoWatcher is a comprehensive environmental risk analysis platform designed to monitor and visualize atmospheric data across geographic zones. It combines real-time telemetry simulation with advanced AI-driven risk assessment to help users navigate environmental hazards.

## 🚀 Key Features
* **Live Monitoring Dashboard**: High-fidelity visualization of AQI, Temperature, Humidity, Wind Speed, UV, and Noise.
* **Geospatial Integration**: Interactive map built with Leaflet.js showcasing zone distributions.
* **Automated Alert Engine**: Instant detection of threshold breaches (e.g., Extreme Heat, High Pollution).
* **Eco-AI Advisor**: A context-aware AI assistant (powered by Qwen/Hugging Face) that analyzes specific sensor incidents to provide safety recommendations.
* **System Management**: Full CRUD capabilities for monitoring zones and a "Factory Reset" feature for fresh deployments.


## 🛠️ Local Setup & Installation
Follow these steps to set up EcoWatcher on your local machine.

### 1. Prerequisites
* **Python 3.9+** installed on your system.
* A **Hugging Face API Key** (Free) to power the Eco-AI Advisor.

### 2. Clone and Navigate
```bash
git clone //github.com/ujjwal-7531/EcoWatcher.git
cd EcoWatcher
```
### 3.Create a virtual envirenment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. install dependencies
```bash
pip install -r requirements.txt
```

### 5.Environment Configuration
```bash
Create a .env file in the root directory and paste your API key:
HF_API_KEY=your_huggingface_token
```

### 6.Launch the engine
```bash
python main.py
```