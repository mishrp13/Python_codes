
# Take a backup of a file before modifying it.


import shutil

file = 'example.txt'
shutil.copy(file, file + '.bak')  # Backup

with open(file, 'a') as f:        # Modify
    f.write('\n# Modified\n')
