import platform
import socket
import requests
import psutil
import os
import time

def get_os_details():
    os_details = platform.uname()
    return os_details

def get_private_ip():
    try:
        hostname = socket.gethostname()
        private_ip = socket.gethostbyname(hostname)
        return private_ip
    except socket.error:
        return "Not available"

def get_public_ip():
    try:
        public_ip = requests.get('https://api.ipify.org').text
        return public_ip
    except requests.RequestException:
        return "Not available"

def get_default_gateway():
    return "Not available"

def get_disk_statistics():
    disk_usage = psutil.disk_usage('/')
    total = disk_usage.total // (2**30)  # Convert to GB
    used = disk_usage.used // (2**30)    # Convert to GB
    free = disk_usage.free // (2**30)    # Convert to GB
    return total, used, free

def get_size(start_path='.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def find_largest_directories(path='.'):
    try:
        directories = [(d, get_size(os.path.join(path, d))) for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
        largest_directories = sorted(directories, key=lambda x: x[1], reverse=True)[:5]
        return largest_directories
    except OSError:
        return []

def monitor_cpu_usage(interval=10):
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            print(f"CPU Usage: {cpu_usage}%")
            time.sleep(interval - 1)
    except KeyboardInterrupt:
        print("Monitoring stopped.")

# Display OS details
print("OS Details:", get_os_details())

# Display network information
print("Private IP:", get_private_ip())
print("Public IP:", get_public_ip())
print("Default Gateway:", get_default_gateway())

# Display disk statistics
total, used, free = get_disk_statistics()
print(f"Disk Total: {total} GB, Used: {used} GB, Free: {free} GB")

# Display largest directories
largest_dirs = find_largest_directories()
print("Largest Directories by Size:")
for directory, size in largest_dirs:
    print(f"{directory}: {size // (2**20)} MB")

# Monitor CPU usage
monitor_cpu_usage()