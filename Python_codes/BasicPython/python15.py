

# Delete all the files in the folder older than 7 days

# import os
# import time

# def delete_old_files(folder, days=7):
#     cutoff = time.time() - days * 86400

#     for file in os.listdir(folder):
#         path = os.path.join(folder, file)
#         if os.path.isfile(path) and os.path.getmtime(path) < cutoff:
#             os.remove(path)
#             print(f"Deleted: {path}")

# # Example usage
# delete_old_files("path/to/your/folder")

import os
import time


def delete_file(folder,days):
    cutoff=time.time()- days*86400

    for file in os.listdir(folder):
        path=os.path.join(folder,file)
        if os.path.isfile(path) and os.path.getmtime(path) < cutoff:
            os.remove(path)
            print(f" Deleted: {path}")


delete_file("-----",7)



