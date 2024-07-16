import time

def monitor_cpu_usage(interval=10):
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            print(f"CPU Usage: {cpu_usage}%")
            time.sleep(interval - 1)
    except KeyboardInterrupt:
        print("Monitoring stopped.")

monitor_cpu_usage()