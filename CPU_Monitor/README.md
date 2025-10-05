# CPU Usage Monitor

A Python script that monitors system CPU usage in real-time and provides alerts when usage exceeds 80%.

## Features
- Real-time CPU usage monitoring
- Alert system for high CPU usage (>=80%)
- Timestamp for each reading
- Graceful handling of user interruption (Ctrl+C)
- Exception handling for robustness

## Requirements
- Python 3.x
- psutil library

## Installation
1. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # For Unix/Linux
# or
venv\Scripts\activate     # For Windows
```

2. Install required package:
```bash
pip install psutil
```

## Usage
Run the script:
```bash
python cpu_monitor.py
```

To stop monitoring, press `Ctrl+C`.

## Output Format
- Normal reading:
  ```
  [2025-10-05 14:30:45] CPU Usage: 25.6%
  ```
- High CPU alert:
  ```
  ⚠️ ALERT! High CPU Usage at 2025-10-05 14:35:12
  Current CPU Usage: 85.3%
  ```