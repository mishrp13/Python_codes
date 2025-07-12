
# Search for a file in a directory recursively

import os

# def search_file(filename, search_path):
#     for root, dir, files in os.walk(search_path):
#         if filename in files:
#             full_path = os.path.join(root, filename)
#             print(f"Found: {full_path}")
#             return full_path
#     print("File not found.")
#     return None

# # Example usage
# search_file("example.txt", r"C:\Users\praba\OneDrive\Documents\ras")


def serach_files(filename,search_path):
    for root,dir,files in os.walk(search_path):
        if filename in files:
            full_path=os.path.join(root,filename)
            print(f"file found :  full path is:  '{full_path}")
            return full_path
        
    print(f"file not found")
    return None


serach_files("example.txt",r"C:\Users\praba\OneDrive\Documents\ras")
