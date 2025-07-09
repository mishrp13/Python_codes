# Copy contents of one file to another.

def copy_file(source_file,destination_file):
    try:
        with open(source_file,'r') as source:
            content=source.read()

        with open(destination_file,'w') as destination:
            destination.write(content)

    except FileNotFoundError:
        print(f"file '{source_file}' is not present ")


copy_file('source.txt','destination.txt')

    