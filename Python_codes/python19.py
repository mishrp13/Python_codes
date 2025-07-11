
# Reading from json file

import json

# Read from a file
with open("data.json", "r") as file:
    loaded_data = json.load(file)

print("Data loaded from JSON:")
print(loaded_data)
