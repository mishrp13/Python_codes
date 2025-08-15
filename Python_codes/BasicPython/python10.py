
# checking cpu and memory every second


import psutil
import time

while True:
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    print(f"CPU: {cpu}% | Memory: {mem}%")
    time.sleep(1)
