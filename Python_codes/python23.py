# Python script to fetch logs from a log website and print all logs with 404: not found

import requests

# Publicly available Apache log sample
log_url = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/apache_logs/apache_logs'

try:
    # Fetch the log content
    response = requests.get(log_url)
    #response.raise_for_status()
    logs = response.text.splitlines()

    print("Log lines with 404 Not Found:\n")

    # Search for lines with HTTP 404
    for line in logs:
        if ' 404 ' in line:
            print(line)

except requests.exceptions.RequestException as e:
    print(f"Error fetching logs: {e}")