import platform

def get_os_details():
    os_details = platform.uname()
    return os_details

print("OS Details:", get_os_details())