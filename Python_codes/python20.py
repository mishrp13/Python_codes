
# Get current date and time

from datetime import datetime

# Get current date and time
now = datetime.now()

# Format nicely
print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))
