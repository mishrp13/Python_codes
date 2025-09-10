file_path='book.txt'

with open(file_path,'r') as open_file:
    text=open_file.readlines()
    print(text)

print(open_file.closed)  # False