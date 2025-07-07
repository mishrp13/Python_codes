
#python script for checking the process.

# import os

# os.system("ps -ef | grep python")

import psutil

for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
    try:
        if proc.info['cmdline'] and 'python' in proc.info['cmdline'][0].lower():
            print(f"PID: {proc.info['pid']} | CMD: {' '.join(proc.info['cmdline'])}")
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        continue

