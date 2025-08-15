# Copy contents of one file to another.


def copy_file(source_file,destination_file):

    try:
        with open (source_file,'r') as src:
            content=src.read()

        with open (destination_file,'w') as dest:
            dest.write(content)

        print(f"file has been copied from '{source_file}' to '{destination_file}'")

    except FileNotFoundError:

        print(f" '{source_file}' is not available")


copy_file('source.txt','destination.txt')



    