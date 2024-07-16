import socket
import requests
import netifaces as ni

def get_private_ip():
    hostname = socket.gethostname()
    private_ip = socket.gethostbyname(hostname)
    return private_ip

def get_public_ip():
    public_ip = requests.get('https://api.ipify.org').text
    return public_ip

def get_default_gateway():
    gws = ni.gateways()
    default_gateway = gws['default'][ni.AF_INET][0]
    return default_gateway

print("Private IP:", get_private_ip())
print("Public IP:", get_public_ip())
print("Default Gateway:", get_default_gateway())