
# Get system hostname and IP.

import socket

# Get the hostname
hostname = socket.gethostname()

# Get the IP address
ip_address = socket.gethostbyname(hostname)

# Print the results
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")


