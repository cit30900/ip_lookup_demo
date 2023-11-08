# Convert a domain name into an IP address
import socket

domain = "amazon.com"
try:
    ip_address = socket.gethostbyname(domain)
except socket.gaierror as e:
    print("The domain could not be resolved.")
else:
    print(f"The IP address of {domain} is {ip_address}.")