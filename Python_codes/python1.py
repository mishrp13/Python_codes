

# Write a script to print all files in a directory.


import os   

directory = r"C:\python_for_devops\python-for-devops\Day-04"

for filename in os.listdir(directory):
    file_path=os.path.join(directory, filename)
    if os.path.isfile(file_path):
        print(filename) 

# #### ✅ What it does:
# - This imports the **`os` module**, which provides a way to interact with the operating system.

# #### 🧠 Why it's needed:
# - You need `os` to:
#   - Access directory contents (`os.listdir`)
#   - Join paths safely (`os.path.join`)
#   - Check if a path is a file or directory (`os.path.isfile`)

# ---

# ### ```python
# directory = r"C:\python_for_devops\python-for-devops\Day-03"


#Git commands
#git init
#git remote add origin "url"
# git add .
# git commit -m ""

