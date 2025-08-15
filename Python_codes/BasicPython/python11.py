# Find disk usage of the root filesystem.


import psutil

# Get disk usage of root filesystem
disk = psutil.disk_usage('/')

print(f"Disk Usage for / (Root Filesystem):")
print(f"  Total: {disk.total / (1024**3):.2f} GB")
print(f"  Used: {disk.used / (1024**3):.2f} GB")
print(f"  Free: {disk.free / (1024**3):.2f} GB")
print(f"  Percentage Used: {disk.percent}%")
