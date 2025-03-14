import psutil
import time

while True:  # Keeps running forever
    cpu_usage = psutil.cpu_percent(interval=1)  # Get CPU usage (waits 1 second)
    memory_info = psutil.virtual_memory()  # Get memory details
    memory_usage = memory_info.percent  # Extract memory usage percentage

    print(f"CPU Usage: {cpu_usage}%  Memory Usage: {memory_usage}%")  # Print to screen
    
    time.sleep(3)  # Wait for 3 seconds before running again

