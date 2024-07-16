import psutil

def get_disk_statistics():
    disk_usage = psutil.disk_usage('/')
    total = disk_usage.total // (2**30)  # Convert to GB
    used = disk_usage.used // (2**30)    # Convert to GB
    free = disk_usage.free // (2**30)    # Convert to GB
    return total, used, free

total, used, free = get_disk_statistics()
print(f"Disk Total: {total} GB, Used: {used} GB, Free: {free} GB")