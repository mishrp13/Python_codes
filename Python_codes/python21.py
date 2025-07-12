
# Set a cron job via script.

import subprocess

cron_job = "0 9 * * * /usr/bin/python3 /path/to/your/script.py\n"

try:
    current_crontab = subprocess.check_output(["crontab", "-l"], text=True)
except subprocess.CalledProcessError:
    current_crontab = ""

if cron_job not in current_crontab:
    new_crontab = current_crontab + cron_job
    process = subprocess.run(["crontab", "-"], input=new_crontab, text=True)
    print("Cron job added.")
else:
    print("Cron job already exists.")
