 # Step-by-Step: Write & Read JSON File


import json

data = {
    "name": "Alice",
    "age": 30,
    "is_employee": True,
    "skills": ["Python", "DevOps", "Docker"]
}

# Write to a file
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

print("Data written to data.json")
