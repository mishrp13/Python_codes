#  Script: Archive a Folder as a .zip File


import shutil

# Folder to be zipped
folder_to_zip = "my_folder"

# Output zip file name (without .zip extension)
output_zip = "my_folder_backup"

# Create the zip archive
shutil.make_archive(output_zip, 'zip', folder_to_zip)

print(f"Folder '{folder_to_zip}' has been zipped as '{output_zip}.zip'")
