import psutil
import time
from datetime import datetime

def monitor_cpu():
    """
    Continuously monitors CPU usage and alerts if usage exceeds 80%.
    Handles keyboard interruption gracefully.
    """
    try:
        # Print starting message
        print("Monitoring CPU usage... Press Ctrl+C to stop.")
        print("-" * 50)

        # Continuous monitoring loop
        while True:
            # Get current CPU usage percentage
            cpu_percent = psutil.cpu_percent(interval=1)
            
            # Get current timestamp
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Check if CPU usage exceeds threshold (80%)
            if cpu_percent >= 80:
                print(f"⚠️ ALERT! High CPU Usage at {current_time}")
                print(f"Current CPU Usage: {cpu_percent}%")
                print("-" * 50)
            else:
                # Print normal monitoring message
                print(f"[{current_time}] CPU Usage: {cpu_percent}%")
            
            # Small delay to prevent excessive resource usage
            time.sleep(1)

    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\nMonitoring stopped by user.")
    except Exception as e:
        # Handle other potential errors
        print(f"\nAn error occurred: {str(e)}")
    finally:
        # Clean up message
        print("CPU monitoring terminated.")

if __name__ == "__main__":
    monitor_cpu()