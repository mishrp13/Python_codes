
# Rename all .txt files in a folder to .log.

import os

# Set your folder path
folder_path = r"C:\python_for_devops\python-for-devops\Day-04"

# Loop through all items in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        # Create full original and new file paths
        old_path = os.path.join(folder_path, filename)
        new_filename = filename[:-4] + ".log"  # remove '.txt' and add '.log'
        new_path = os.path.join(folder_path, new_filename)

        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_filename}")
