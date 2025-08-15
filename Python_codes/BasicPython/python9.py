# Get CPU and memory usage (using psutil).

import psutil

# Get CPU usage
cpu_percent = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu_percent}%")

# Get memory usage
memory = psutil.virtual_memory()
print(f"Memory Usage: {memory.percent}%")
print(f"Total Memory: {memory.total / (1024 ** 3):.2f} GB")
print(f"Available Memory: {memory.available / (1024 ** 3):.2f} GB")



